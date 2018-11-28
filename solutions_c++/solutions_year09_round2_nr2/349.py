#include <iostream>
#include <cmath>
#include <algorithm>
#include <cstring>
#include <cstdio>



using namespace std;

char s[30];
int a[30];
int c[30];
int t, n;

int main(){
    cin >> t;
    gets(s);
    for (int _i = 0; _i < t; ++_i){
        memset(c, 0, sizeof(c));
        gets(s);
        n = strlen(s);
        for (int i = 0; i < n; ++i){
            a[i] = s[i] - '0';
            c[s[i] - '0']++;
        }

        bool flag = true;
        for (int i = 0; i < n - 1; ++i){
            if (a[i] < a[i + 1]){
               flag = false;
               break;
            }
        }
//        for (int i = 1; i < 10; ++i) cout << c[i] << endl;
        if (flag){
           a[n] = 0;
           ++n;
           int q = 0;
           for (int i = 1; i < 10; ++i) if (c[i]){
               --c[i];
               a[q] = i;
               ++q;
               break;
           }
           ++c[0];
           while(c[0]){
                  --c[0];
                  a[q] = 0;
                  ++q;

           }
           for (int i = 1; i < 10; ++i){

               while(c[i]){
                  --c[i];
                  a[q] = i;
                  ++q;
               }
           }

          
        }
        cout << "Case #" << _i + 1 << ": ";
        if (!flag)next_permutation(&a[0], &a[n]);
        for (int i = 0; i < n; ++i) cout << a[i];
        cout << endl;
    }
    return 0;
}