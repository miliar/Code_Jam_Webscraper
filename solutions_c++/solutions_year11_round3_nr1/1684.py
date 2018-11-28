//
#include <stdio.h>
#include <iostream>
#include <math.h>
#include <vector>
#include <string>
#include <map>
#include <queue>
#include <algorithm>

#define foreach(i,c)for(__typeof((c).end())i=(c).begin();i!=(c).end();++i)

using namespace std;
typedef unsigned long long ull;

int main()
{
    int cases;
    cin>>cases;
    for (int casenum=1; casenum<=cases; casenum++) {
        int r,c;
        cin>>r>>c;
        char temp,a[r][c];
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                cin>>temp;
                if(temp==' '||temp=='\n') continue;
                a[i][j]=temp;
            }
        }
        
                                
        
        for (int i = 0; i <= r-2; i++) {
            for (int j = 0; j <= c-2; j++) {
                if (a[i][j]=='#' && a[i][j+1]=='#' && a[i+1][j+1]=='#' && a[i+1][j]=='#'){
                    //cout << i<<" "<<j<<endl;
                    //cout<<a[i][j]<<a[i+1][j]<<a[i][j+1]<<a[i+1][j+1]<<endl;
                    a[i][j]='/'; a[i+1][j]='\\';a[i][j+1]='\\';a[i+1][j+1]='/';
                    //cout<<a[i][j]<<a[i+1][j]<<a[i][j+1]<<a[i+1][j+1]<<endl;
                }
            }
        }
        
        bool bad = false;
        for (int i = 0; i < r; i++) {
            for (int j = 0; j < c; j++) {
                if (a[i][j]=='#') {
                    bad=true;
                    break;
                }
            }
            if (bad) break;
        }
        
        cout << "Case #"<<casenum<< ":" << endl;
        if (bad) cout<<"Impossible"<<endl;
        else {
            for (int i = 0; i < r; i++) {
                for (int j = 0; j < c; j++)
                    cout << a[i][j];
                cout << endl;
            }
        }

    }
}
