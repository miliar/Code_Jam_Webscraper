#include <iostream>
#include <algorithm>
#include <string>
#include <cstring>
using namespace std;
int n,m;
string map[100];
bool flag[100][100];
bool isused(int i,int j)
{
    if(!flag[i][j] && !flag[i+1][j] &&!flag[i][j+1] &&!flag[i+1][j+1] &&
        map[i][j]=='#' &&map[i+1][j]=='#' &&map[i][j+1]=='#' &&map[i+1][j+1]=='#'
       )
        return true;
    else return false;

}
int main()
{
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    int tt;
    cin>>tt;
    for(int t=1;t<=tt;t++)
    {
        cin>>n>>m;
        for(int i=0;i<n;i++)
                cin>>map[i];
        memset(flag,0,sizeof(flag));
        for(int i=0;i<n-1;i++)
            for(int j=0;j<m-1;j++)
            {
                if(isused(i,j))
                {
                    map[i][j]='/',flag[i][j]=true;
                    map[i][j+1]='\\',flag[i][j]=true;
                    map[i+1][j]='\\',flag[i][j]=true;
                    map[i+1][j+1]='/',flag[i+1][j+1]=true;
                }
            }
        bool flag1=true;
        for(int i=0;i<n;i++)
            for(int j=0;j<m;j++)
            {
                if(map[i][j]=='#')
                    flag1=false;
            }
        cout<<"Case #"<<t<<":"<<endl;
        if(flag1)
        {
            for(int i=0;i<n;i++)
                cout<<map[i]<<endl;
        }
        else cout<<"Impossible"<<endl;
    }
    return 0;
}
