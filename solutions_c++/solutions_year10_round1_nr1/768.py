#include <iostream>
#include <string>
using namespace std;
string grid[100];
string ngrid[100];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-large.out","w",stdout);
    int T;cin>>T;

    for(int tc=1;tc<=T;tc++) {
        int n,K;
        cin>>n>>K;

        for(int i = 0; i < n; i++)
            cin>>ngrid[i];

        for(int i = 0; i < n; i++) grid[i]=string(n,'.');

        for(int i = 0; i < n; i++) {
            string str = "";
            for(int j = 0; j < n; j++) {
                int ni = j, nj = n-1-i;

                grid[ni][nj]=ngrid[i][j];
            }
        }

      //  for(int i = 0; i < n; i++) cout<<grid[i]<<endl;

        //gravity

        for(int j = 0; j < n; j++) {
            for(int i = n-1;i>=1;i--) {
                if(grid[i][j]=='.') {
                    int k = i;
                    for(;k>=0;k--) {
                        if(grid[k][j]!='.')break;
                    }
                    //cout<<k<<endl;
                    if(k==-1) continue;
                    for(int p=k;p<i;p++) {
                        //cout<<p<<endl;
                        swap(grid[p][j],grid[p+1][j]);

                    }
                }
            }
        }



        int red=0,blue=0;
        for(int i = 0; i < n; i++) {
            for(int j = 0; j < n; j++) {
                //horizontal
                if(grid[i][j]=='.') continue;
                if(j+K-1<=n-1) {
                    int ok = 1;
                    for(int k=1;k<K;k++) {
                        if(grid[i][j+k]!=grid[i][j+k-1]) ok=0;
                    }
                    if(ok) {
                        if(grid[i][j]=='R')red=1;
                        else blue=1;
                    }
                }
                //vertical
                if(i+K-1<=n-1) {
                    int ok = 1;
                    for(int k=1;k<K;k++) {
                        if(grid[i+k][j]!=grid[i+k-1][j]) ok=0;
                    }
                    if(ok) {
                        if(grid[i][j]=='R')red=1;
                        else blue=1;
                    }
                }
                //left diagonal
                if(i+K<=n&&j-K>=-1) {
                    int ok = 1;
                    char c = grid[i][j];
                    for(int k = 0; k < K; k++) {
                        if(grid[i+k][j-k]!=c) ok = 0;
                    }
                    if(ok) {
                        if(grid[i][j]=='R')red=1;
                        else blue=1;
                    }
                }
                if(i+K<=n&&j+K<=n) {
                    int ok = 1;
                    char c = grid[i][j];
                    for(int k = 0; k < K; k++) {
                        if(grid[i+k][j+k]!=c) ok = 0;
                    }
                    if(ok) {
                        if(grid[i][j]=='R')red=1;
                        else blue=1;
                    }
                }


            }
        }
        string ans = "Neither";
        if(red&&blue) ans="Both";
        else if(red)ans="Red";
        else if(blue)ans="Blue";
        cout<<"Case #"<<tc<<": "<<ans<<endl;

    }
    return 0;
}
