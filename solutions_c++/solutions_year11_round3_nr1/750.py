#include <iostream>
#include <vector>
#include <string>
#include <algorithm>
#include <set>

using namespace std;
const int MAXN = 100;
string grid[MAXN];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("A-small.out","w",stdout);
    int T;
    cin>>T;
    for(int tc = 1; tc <= T; tc++) {
        cout<<"Case #"<<tc<<": "<<endl;
        int R,C;
        cin>>R>>C;
        for(int i = 0; i < R; i++) {
            cin>>grid[i];
        }
        int ok=1;
        for(int i = 0; i < R; i++) {
            for(int j = 0; j < C; j++) {
                if(grid[i][j]!='#') continue;
                if(j+1<C&&grid[i][j+1]=='#'&&i+1<R&&grid[i+1][j]=='#'
                    &&grid[i+1][j+1]=='#') {
                    grid[i][j]='/';
                    grid[i][j+1]='\\';
                    grid[i+1][j]='\\';
                    grid[i+1][j+1]='/';
                }
                else ok = 0;
            }
        }
        if(!ok) {
            cout<<"Impossible"<<endl;
        }
        else
        for(int i = 0; i <R ;i++) {
            for(int j = 0; j < C; j++) {
                cout<<grid[i][j];
            }
            cout<<endl;
        }


    }
    return 0;
}
