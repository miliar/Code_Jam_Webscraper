/* {{{ */
#include<cstdio>
#include<climits>
#include<cmath>
#include<cassert>
#include<cstdlib>
#include<cstring>
#include<ctime>
#include<algorithm>
#include<map>
#include<list>
#include<sstream>
#include<set>
#include<queue>
#include<vector>
#include<string>
#include<fstream>
#include<istream>
#include<iostream>
#include<bitset>
using namespace std;
/* }}}  */

typedef long long ll;
typedef unsigned long long ull;

const int MAX=202;
vector<int> v[MAX];
int dist[MAX][MAX];
int pre[MAX];

int dfs(int x)
{
    if(x==0) return 0;
    if(pre[x]!=-1) return pre[x];
    int i;
    int ans=0;
    for(i=0;i<v[x].size();i++){
        ans=max(ans,1+dist[v[x][i]][x] + dfs(v[x][i]));
    }
    return pre[x]=ans;
}

int main(int argc,char **argv){
    int no;
    scanf(" %d",&no);
    int tc;

    for(tc=1;tc<=no;tc++){
        int n;
        scanf(" %d",&n);
        vector<pair<int,int> > red,blue;
        memset(dist,0,sizeof(dist));
        memset(pre,-1,sizeof(pre));
        int node=1,i;
        for(i=0;i<n;i++){
                char ch;
                int k;
                scanf(" %c %d",&ch,&k);
                if(ch=='B') blue.push_back(make_pair(k,node));
                else        red.push_back( make_pair(k,node));
                node++;
        }

    int x=0,d1=0;

    if(blue.size())
    {
        x=blue[0].second;d1=blue[0].first;
        dist[0][x]=abs(d1-1);
        v[x].push_back(0);
    }

        for(i=0;i+1<blue.size();i++){
            int x=blue[i].second,d1=blue[i].first;
            int y=blue[i+1].second,d2=blue[i+1].first;
            dist[x][y]=abs(d1-d2);
            v[y].push_back(x);
        }

    if(red.size()){
        x=red[0].second;
        d1=red[0].first;
        dist[0][x]=abs(d1-1);
        v[x].push_back(0);
    }


        for(i=0;i+1<red.size();i++){
            int x=red[i].second,d1=red[i].first;
            int y=red[i+1].second,d2=red[i+1].first;
            dist[x][y]=abs(d1-d2);
            v[y].push_back(x);


        }

        for(i=1;i+1<node;i++){
            v[i+1].push_back(i);
        }

            printf("Case #%d: %d\n",tc,dfs(node-1));

            
    }

        return 0;
}
