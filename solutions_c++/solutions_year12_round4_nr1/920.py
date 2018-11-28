#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <iostream>
#include <algorithm>
#include <math.h>
#include <vector>

using namespace std;

int t,n,d[20000],l[20000],len,a[20000],m[20000];
char can[20000];

int main(){
    freopen("input.txt","r",stdin);freopen("output.txt","w",stdout);
    cin >> t;
    for (int tt=0; tt<t; tt++){
        cout << "Case #" << tt+1 << ": ";
        cin >> n;
        memset(can,0,sizeof(can));
        memset(m,0,sizeof(m));
        for (int i=0; i<n; i++)
            cin >> d[i] >> l[i];
        cin >> len;
        can[0] = 1;
        m[0] = d[0];
        char ok = 0;

        for (int i=0; i<n; i++)
            if (can[i]){
                int next = d[i]+m[i];
                if (next>=len){
                    ok = 1;
                    break;
                }
                int j = i+1;
                while (j<n && d[j]<=next){
                    can[j] = 1;
                    m[j] = max(m[j],min(l[j],d[j]-d[i]));
                    j++;
                }
            }

        if (ok)
            cout << "YES" << endl;
        else
            cout << "NO" << endl;
    }

    return 0;
}
