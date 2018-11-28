#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int MAXN = 1005;

const int MAX_LEN = 1005;
const int BASE = 100000000;
const int STAGE = 8;
const int ELE[]={ 1, 10, 100, 1000, 10000, 100000, 1000000, 10000000, 100000000 };

struct Bigint {
    int num[ MAX_LEN / 8 ], len;
    void Init() {
        memset( num, 0, sizeof(num) );
        len = 1;
    }
    bool operator<( const Bigint &k ) const {
        if ( len != k.len ) return len < k.len;
        else {
            for ( int i=len; i>=0; i-- ) {
                if ( num[i] != k.num[i] ) return num[i] < k.num[i];
            }
            return false;
        }
    }
    void ReLength() {
        if ( num[len] ) {
            while ( num[len] ) len++;
        } else {
            while ( len > 1 && !num[len-1] ) len--;
        }
    }
    bool Input() {
        char s[1005];
        int Len, i;
        Init();
        if ( scanf("%s", s) == EOF ) return false;
        Len = strlen( s );
        len = ( Len - 1 ) / STAGE + 1;
        reverse( s, s + Len );
        for ( i=0; i<Len; i++ ) {
            num[ i / STAGE ] += ( s[i] - '0' ) * ELE[ i % STAGE ];
        }
        ReLength();
        return true;
    }
    void Print() {
        printf("%d", num[len-1] );
        for ( int i=len-2; i>=0; i-- ) {
            printf("%08d", num[i] );
        }
        putchar('\n');
    }
    bool Is_Zero() {
        return len == 1 && num[0] == 0;
    }
    Bigint operator+( const Bigint k ) {
        Bigint res;
        int i, carry;
        res.Init();
        res.len = ( len > k.len ) ? len : k.len;
        for ( i=carry=0; i<=res.len; i++ ) {
            res.num[i] = num[i] + k.num[i] + carry;
            carry = 0;
            if ( res.num[i] >= BASE ) {
                res.num[i] -= BASE;
                carry = 1;
            }
        }
        res.ReLength();
        return res;
    }
    Bigint operator-( const Bigint k ) {
        Bigint res;
        int i, borrow;
        res.Init();
        res.len = ( len > k.len ) ? len : k.len;
        for ( i=borrow=0; i<res.len; i++ ) {
            res.num[i] = num[i] - k.num[i] - borrow;
            borrow = 0;
            if ( res.num[i] < 0 ) {
                res.num[i] += BASE;
                borrow = 1;
            }
        }
        res.ReLength();
        return res;
    }
    Bigint operator*( const Bigint k ) {
        Bigint res;
        long long tmp[ MAX_LEN / 8 ]={};
        int i, j;
        res.Init();
        res.len = len + k.len;
        for ( i=0; i<len; i++ ) {
            for ( j=0; j<k.len; j++ ) {
                tmp[i+j] += (long long)num[i] * k.num[j];
            }
        }
        for ( i=0; i<res.len; i++ ) {
            if ( tmp[i] >= BASE ) {
                tmp[i+1] += tmp[i] / BASE;
                tmp[i] %= BASE;
            }
            res.num[i] = (int)tmp[i];
        }
        res.ReLength();
        while ( res.num[res.len-1] >= BASE ) {
            res.num[res.len++] += res.num[res.len-1] / BASE;
            res.num[res.len-1] %= BASE;
        }
        return res;
    }
    void Mul10() {
        for ( int i=0; i<len; i++ ) num[i] *= 10;
        for ( int i=0; i<len; i++ ) {
            if ( num[i] >= BASE ) {
                num[i+1] += num[i]/BASE;
                num[i] %= BASE;
            }
        }
        ReLength();
    }
    void Div10() {
        for ( int i=len-1; i>=0; i-- ) {
            if ( i ) num[i-1] += num[i]%10 * BASE;
            num[i] /= 10;
        }
        ReLength();
    }
    Bigint operator/( Bigint k ) {
        Bigint curr = *this, res;
        res.Init();
        if ( curr < k ) return res;
        int i, tmp, mov = ( curr.len - k.len ) * STAGE + 1;
        if ( curr.len > k.len ) {/* K must be shifted */
            tmp = curr.len - k.len;
            for ( i=k.len-1; i>=0; i-- ) {
                k.num[i+tmp] = k.num[i];
                k.num[i] = 0;
            }
        }
        k.len = curr.len;
        while ( k < curr ) {
            k.Mul10();
            mov++;
        }
        res.len = mov / STAGE + 1;
        while ( mov-- ) {
            while ( !( curr < k ) ) {
                curr = curr - k;
                res.num[ mov / STAGE ] += ELE[ mov % STAGE ];
            }
            if ( mov ) k.Div10();
        }
        res.ReLength();
        return res;
    }
    Bigint operator%( Bigint k ) {
        Bigint curr = *this, res;
        res.Init();
        if ( curr < k ) return curr;
        int i, tmp, mov = ( curr.len - k.len ) * STAGE + 1;
        if ( curr.len > k.len ) {/* K must be shifted */
            tmp = curr.len - k.len;
            for ( i=k.len-1; i>=0; i-- ) {
                k.num[i+tmp] = k.num[i];
                k.num[i] = 0;
            }
        }
        k.len = curr.len;
        while ( k < curr ) {
            k.Mul10();
            mov++;
        }
        res.len = mov / STAGE + 1;
        while ( mov-- ) {
            while ( !( curr < k ) ) {
                curr = curr - k;
                res.num[ mov / STAGE ] += ELE[ mov % STAGE ];
            }
            if ( mov ) k.Div10();
        }
        res.ReLength();
        curr.ReLength();
        return curr;
    }
};

int N;
Bigint num[MAXN];

Bigint Gcd( Bigint a, Bigint b ) {
    Bigint r;
    while ( !b.Is_Zero() ) {
        r = a % b;
        a = b;
        b = r;
    }
    return a;
}

Bigint gcd, tmp, Unit, ans;

int main() {
    int t, casN, i;
    
    Unit.Init();
    Unit.num[0] = 1;
    
    scanf("%d", &t);
    for ( casN=1; casN<=t; casN++ ) {
        scanf("%d", &N);
        for ( i=0; i<N; i++ ) {
            num[i].Input();
        }
        sort( num, num + N );
        gcd = num[1] - num[0];
        for ( i=2; i<N; i++ ) {
            gcd = Gcd( gcd, num[i] - num[i-1] );
        }
        if ( ( num[0] % gcd ).Is_Zero() ) tmp = num[0];
        else tmp = ( num[0] / gcd + Unit ) * gcd;
        printf("Case #%d: ", casN);
        ans = tmp - num[0];
        ans.Print();
    }
    
    //system("Pause");
    return 0;
}
