#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
int n,m;
string map[51];
bool used[51][51];
bool ok(int i,int j)
{
    if(!used[i][j] && !used[i+1][j] &&!used[i][j+1] &&!used[i+1][j+1] &&
        map[i][j]=='#' &&map[i+1][j]=='#' &&map[i][j+1]=='#' &&map[i+1][j+1]=='#'
       )
        return true;
    else return false;

}
int main()
{
    freopen("ass.in","r",stdin);
    freopen("ass.out","w",stdout);
    int T;
    cin>>T;
    for(int t=1;t<=T;t++)
    {
        cin>>n>>m;
        for(int i=0;i<n;i++)
                cin>>map[i];
        memset(used,0,sizeof(used));
        for(int i=0;i<n-1;i++)
            for(int j=0;j<m-1;j++)
            {
                if(ok(i,j))
                {
                    map[i][j]='/',used[i][j]=true;
                    map[i][j+1]='\\',used[i][j]=true;
                    map[i+1][j]='\\',used[i][j]=true;
                    map[i+1][j+1]='/',used[i+1][j+1]=true;
                }
            }
        bool flag=true;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(map[i][j]=='#')
                    flag=false;
            }
        cout<<"Case #"<<t<<":"<<endl;
        if(flag)
        {
            for(int i=0;i<n;i++)
                cout<<map[i]<<endl;
        }
        else cout<<"Impossible"<<endl;
    }
    return 0;
}
