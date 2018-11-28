#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
#include<algorithm>
#include<stdlib.h>
#include<math.h>
using namespace std;

bool n[2000001];

int int_lenth(int a) {
    int lenth = 0;
    if(!a) return 1;
    while(a) {
        a /= 10;
        lenth++;
    }
    return lenth;
}


int main() {
    FILE* f = fopen("PC.txt", "w");
    int ans, tmp;
    int T, A, B;
    int i, j, count = 1, lenth;
    string s;
    int a;
    char c;
    int k;
    int p;

    cin >> T;
    while(T--) {
        memset(n, 0, sizeof(n));
        ans = 0; p = 1;
        cin >> A >> B;
        /*
        if(A == B) {
            cout << "Case #" << count++ << ": " << ans << endl;
            continue;
        }
        */
        //lenth = int_lenth(B);
        for(i = A;i <= B;i++) {
            lenth = int_lenth(A);
            if(!n[i]) {
                n[i] = true;
                tmp = 1;
                a = i;
                for(j = 0;j < lenth - 1;j++) {
                    a = a / 10 + (a % 10) * pow(10, lenth - 1);
                    /*s = int_string(a, lenth);
                    c = s[0];
                    s.erase(0, 1);
                    s += c;
                    a = string_int(s);*/
                    if(a <= B && a >= A) {
                        if(!n[a]) {
                            n[a] = true;
                            tmp++;
                        }
                    }
                }
                ans += tmp * (tmp - 1) / 2;
            }
            /*if(tmp != 1) {
                for(k = A;k <= B;k++) {
                    if(n[k] && !t[k]) {
                        t[k] = true;
                        cout << k << endl;
                    }
                }
                //system("pause");
            }
            else t[i] = true;*/
        }
        cout << "Case #" << count << ": " << ans << endl;
        fprintf(f, "Case #%d: %d\n", count++, ans);
    }
}
