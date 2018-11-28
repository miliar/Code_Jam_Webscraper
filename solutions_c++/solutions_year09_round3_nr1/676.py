#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <set>
#include <map>
#include <queue>
#include <stack>
#include <cmath>
#define For(i,a,b) for(i=a;i<b;i++)
#define Forto(i,n) For(i,0,n)

using namespace std;

int main()
{
    int T, Case = 1;
    char str[11];
    char aux[11];
    int chars[150];
    int nchars;
    int i,j,k;

    cin >> T;

    while (T--) {
        cin >> str;

        nchars=0;
        Forto(i, 150) chars[i]=0;
        Forto(i, 11) aux[i]=0;

        Forto(i, strlen(str)) {
            if (!chars[(int)(str[i]-'0')]++)
                nchars++;
        }

        //cout << "nchars:" << nchars << endl;

        for(int j=1; j<=nchars; ) {
            char c=0;
            for(k=0; str[k]; k++) {
                if (aux[k]==0 && c==0) c=str[k];
                if ((str[k]==c) && aux[k]==0) {
                    str[k] = j+'0';
                    aux[k] = 1;
                }
            }
            if (j==1) j=0;
            else if (j==0) j=2;
            else j++;
        }

        //cout << "str:" << str << endl;

        char * p;
        long int n = strtol(str, &p, (nchars!=1)?nchars:2);

        cout << "Case #" << Case++ << ": ";
        cout << n << endl;
    }

    return 0;
}
