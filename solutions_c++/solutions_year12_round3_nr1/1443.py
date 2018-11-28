#include <iostream>
#include <queue>
#include <stack>
#include <string>
#include <map>
#include <vector>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
using namespace std;
const int MAX=1005,INF=1<<30;

int mat[MAX][MAX];
int n,m;
int vis[MAX];
int inDegree[MAX];
int goal;
int findFlag;
int color ;

void dfs(int u) {

    if(findFlag == 1)
        return ;

    for(int i=1;i<=n;i++){
        if(mat[u][i]){
            if(vis[i]!=color){
                vis[i]=color;;
                dfs(i);
            }
            else if (vis[i]==color)
                findFlag = 1;
        }

        if(findFlag == 1)
            break ;
    }

    return ;
}

int main()
{
#ifndef ONLINE_JUDGE
    freopen("i.txt", "r", stdin);
    //freopen("A-small-attempt0.in", "r", stdin);
    freopen("o.txt", "w", stdout);
#endif
    int T;

    int t;

    cin>>T;

    for(int num =1 ; num <=T ;num ++){
        memset(mat,0,sizeof(mat));
        memset(vis,0,sizeof(vis));
        memset(inDegree,0,sizeof(inDegree));
        color = 1;

        cin>>n;
//        cout<<n<<endl;
        for(int i=1;i<=n;i++){
            cin>>m;
//            cout<<m;
            for(int j=0;j<m;j++) {
                cin>>t;
//                cout<<" "<<t;
                mat[i][t]=1;
                ++inDegree[t];
            }
//            cout<<endl;
        }

        findFlag = 0;

        for(int i=1;i<=n;i++,color++) {
            if(inDegree[i]==0){
                //cout<<i<<endl;
                vis[i]=color;
                dfs(i);
            }

            if(findFlag == 1)
                break ;
        }

        cout<<"Case #"<<num<<": ";
        if(findFlag ==1 )
            cout<<"Yes"<<endl;
        else
            cout<<"No"<<endl;
    }

    return 0;
}

