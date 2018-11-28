#include <iostream>
#include <string>
#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <string.h>

#define MAX 100000

using namespace std;
 
const int BASE  = 10000;  //Vielfaches von 10, BASE*(BASE+1) kein Ueberlauf!
const int PLUS  = 1;
const int MINUS = -1;
 
struct BigInt {
    int digits[MAX];    //Ziffern (Basis BASE); [0] ist LSD
    int last;           //Index des MSD
    int sign;           //PLUS oder MINUS
};
 
//BigInt normalisieren (fuehrende Nullen abschneiden und -0 verhindern)
//Ergebnisse aller folgenden Funktionen sind normalisiert
void normalize(BigInt &a) {
    while (a.last > 0 && a.digits[a.last] == 0) a.last--;
    if (a.last == 0 && a.digits[0] == 0) a.sign = PLUS;
}
 
//Inaitialisierung mit normalem int; a = val
void init(long long val, BigInt &a) {
    if (val >= 0) {
        a.sign = PLUS;
    } else {
        a.sign = MINUS;
        val = -val;
    }
    if (val == 0) { a.last = 0; a.digits[0] = 0; return; }
    a.last = -1;
    while (val > 0) {
        a.last++;
        a.digits[a.last] = val % BASE;
        val /= BASE;
    }
}
 
//Wertzuweisung; b = a
void assign(BigInt &a, BigInt &b) {
    b.sign = a.sign;
    b.last = a.last;
    memcpy(b.digits, a.digits, (a.last + 1) * sizeof(int));
}
 
//Vergleich zweier BigInt; Rueckgabe: >0, falls a > b
//                                    =0, falls a = b
//                                    <0, falls a < b
int compare(BigInt &a, BigInt &b) {
    if (a.sign == PLUS && b.sign == MINUS) return 1;
    if (a.sign == MINUS && b.sign == PLUS) return -1;
    if (a.last > b.last) return a.sign;
    if (a.last < b.last) return -a.sign;
    for (int i = a.last; i >= 0; i--) {
        int d = a.digits[i] - b.digits[i];
        if (d != 0) return d * a.sign;
    }
    return 0;
}
 
//Negation; a = -a
void negate(BigInt &a) {
    if (a.last > 0 || a.digits[0] > 0) a.sign = -a.sign;
}
 
void subtract(BigInt &, BigInt &, BigInt &);
 
//Addition; c = a + b
void add(BigInt &a, BigInt &b, BigInt &c) {
    static BigInt tmp;
    if (a.sign == PLUS && b.sign == MINUS) {
        assign(b, tmp);
        tmp.sign = PLUS;
        subtract(a, tmp, c);
    } else if (a.sign == MINUS && b.sign == PLUS) {
        assign(a, tmp);
        tmp.sign = PLUS;
        subtract(b, tmp, c);
    } else {
        c.sign = a.sign;
        int clast = max(a.last, b.last) + 1;
        memset(a.digits + a.last + 1, 0, (clast - a.last) * sizeof(int));
        memset(b.digits + b.last + 1, 0, (clast - b.last) * sizeof(int));
        c.last = clast;
        int carry = 0;
        for (int i = 0; i <= c.last; i++) {
            c.digits[i] = a.digits[i] + b.digits[i] + carry;
            carry = c.digits[i] / BASE;
            c.digits[i] %= BASE;
        }
        normalize(c);
    }
}
 
//Subtraktion; c = a - b
void subtract(BigInt &a, BigInt &b, BigInt &c) {
    static BigInt tmp;
    if (a.sign == MINUS || b.sign == MINUS) {
        assign(b, tmp);
        tmp.sign = -tmp.sign;
        add(a, tmp, c);
    } else if (compare(a, b) < 0) {
        subtract(b, a, c);
        c.sign = MINUS;
    } else {
        c.sign = PLUS;
        int clast = max(a.last, b.last);
        memset(a.digits + a.last + 1, 0, (clast - a.last) * sizeof(int));
        memset(b.digits + b.last + 1, 0, (clast - b.last) * sizeof(int));
        c.last = clast;
        int borrow = 0;
        for (int i = 0; i <= c.last; i++) {
            c.digits[i] = a.digits[i] - b.digits[i] - borrow;
            if (c.digits[i] >= 0) {
                borrow = 0;
            } else {
                borrow = 1;
                c.digits[i] += BASE;
            }
        }
        normalize(c);
    }
}
 
//Multiplikation; c = a * b
void multiply(BigInt &a, BigInt &b, BigInt &c) {
    static BigInt res;
    res.sign = a.sign * b.sign;
    res.last = a.last + b.last + 1;
    memset(res.digits, 0, (res.last + 1) * sizeof(int));
    for (int i = 0; i <= a.last; i++) {
        int carry = 0;
        for (int j = 0; j <= b.last; j++) {
            res.digits[i+j] += a.digits[i] * b.digits[j] + carry;
            carry = res.digits[i+j] / BASE;
            res.digits[i+j] %= BASE;
        }
        res.digits[i + b.last + 1] = carry;
    }
    normalize(res);
    assign(res, c);
}
 
//Einlesen von stdin; funktioniert nur richtig, wenn wirklich eine Zahl
//in der Eingabe kommt, also nur Ziffern oder '-' gefolgt von Ziffern
//Rueckgabe: true, falls BigInt gelesen; false bei EOF
bool scan(BigInt &a) {
    string num;
    if (cin >> num) {
        if (num[0] == '-') {
            a.sign = MINUS;
            num.erase(0, 1);
        } else {
            a.sign = PLUS;
        }
        a.last = -1;
        int pos = (int) num.size() - 1;
        while (pos >= 0) {
            a.digits[++a.last] = 0;
            for (int b = 1; b < BASE && pos >= 0; b *= 10, pos--) {
                a.digits[a.last] += b * (num[pos] - '0');
            }
        }
        normalize(a);
        return true;
    }
    return false;
}
 
//Ausgabe auf stdout
void print(BigInt &a) {
    if (a.sign == MINUS) cout << '-';
    cout << a.digits[a.last];
    for (int i = a.last - 1; i >= 0; i--) {
        for (int j = BASE / 10; j > a.digits[i]; j /= 10) cout << '0';
        if (a.digits[i]) cout << a.digits[i];
    }
}

using namespace std;

long long N,P,K,L;
long long ord[1005];
long long max_per_key, key_cnt, alphabet;

vector <long long> nums;

int main ( int argc, char ** argv ) {
	long long nr,y,x;
	BigInt sum;

	scanf("%lld", &N);
	for (nr=0; nr<N; nr++) {
		
		scanf("%lld %lld %lld", &P, &K, &L);
		max_per_key = P;
		key_cnt = K;
		alphabet = L;

		for (x=0; x<alphabet; x++) {
			scanf("%lld", &y);
			nums.push_back(y);
		}

		sort( nums.begin(), nums.end() );
		reverse( nums.begin(), nums.end() );

		init(0, sum);
		BigInt toAdd;
		BigInt res;
		for (y=0; y<nums.size(); y+=key_cnt) {
			for (x=y; x<y+key_cnt; x++) {
				if ( x >= alphabet ) continue;
				long long temp = (y/key_cnt+1) * nums[x];
				init( temp, toAdd );
				add( sum, toAdd, res);
				assign(res, sum);

				//sum = sum + (y/key_cnt+1) * nums[x];
			}
		}
		printf("Case #%lld: ", nr+1);
		print( sum );
		printf("\n");

		nums.clear();
		
	}


	return 0;
}

