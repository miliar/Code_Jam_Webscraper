#include <set>
#include <map>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <stack>
#include <string>
#include <cstdio>
#include <math.h>
#include <time.h>
#include <iomanip>
#include <stdlib.h>
#include <limits.h>
#include <string.h>
#include <iostream>
#include <fstream>
#include <algorithm>
using namespace std;

#define LL long long
#define MIN INT_MIN
#define MAX (1<<30)
#define pii pair<int,int>
#define bug cout<<"here!!!"<<endl
#define FRE freopen("input.txt","r",stdin)
#define FF freopen("output.txt","w",stdout)
#define eps 1e-6
#define pi acos(-1.0)
#define N 1111

/*
struct node{
    int to,w;
};
vector<node> v[N];
int a[N];
int d[N];
bool vis[N];
int cnt[N];
int n;
bool spfa(int s,int t){
    queue<int> q;
    int i;
    for(i=0;i<=t;i++){
        d[i] = MIN;
        vis[i] = 0;
        cnt[i] = 0;
    }
    d[s] = 0;
    vis[s] = 1;
    cnt[s]++;
    q.push(s);
    int to;
    while(!q.empty()){
        to = q.front();
        q.pop();
        vis[to] = 0;
        for(i=0;i<v[to].size();i++){
            int tt = v[to][i].to;
            if(d[to]<MAX && d[tt]<d[to]+v[to][i].w){
                d[tt] = d[to]+v[to][i].w;
                if(!vis[tt]){
                    cnt[tt]++;
                    if(cnt[tt]>=n){
                        return false;
                    }
                    q.push(tt);
                    vis[tt] = 1;
                }
            }
        }
    }
    return true;
}
bool g[N][N];
int main(){FRE;
    int t;
    int ca = 1;
    scanf("%d",&t);
    while(t--){
        int m;
        int i,j;
        scanf("%d%d",&n,&m);
        for(i=0;i<=n;i++)v[i].clear();
        a[0] = 0;
        for(i=1;i<=n;i++){
            int c;
            scanf("%d",&c);
            a[i] = a[i-1]+c;
        }
        node tmp;
        for(i=1;i<=n;i++){
            for(j=i;j<=n;j++){
                tmp.to = j;
                tmp.w = a[j] - a[i-1];
                v[i-1].push_back(tmp);
            }
            tmp.to = i-1;
            tmp.w = 0;
            v[i].push_back(tmp);
        }
        while(m--){
            int z;
            scanf("%d%d%d",&i,&j,&z);
            tmp.to = i-1;
            tmp.w = -z;
            v[j].push_back(tmp);
            //cout<<j<<" "<<i-1<<" "<<tmp.w<<endl;
        }
        printf("Case #%d: ",ca++);
        if(spfa(0,n))
        printf("%d\n",d[n]);
        else puts("Foolish BandBand!");//for(i=0;i<=n;i++)cout<<d[i]<<" ";cout<<endl;
    }
    return 0;
}
*/

char str[111];
char mp[256];
int main(){FRE;FF;
    mp['a'] = 'y';//
    mp['b'] = 'h';
    mp['c'] = 'e';
    mp['d'] = 's';//
    mp['e'] = 'o';//
    mp['f'] = 'c';
    mp['g'] = 'v';//
    mp['h'] = 'x';//
    mp['i'] = 'd';
    mp['j'] = 'u';//
    mp['k'] = 'i';
    mp['l'] = 'g';
    mp['m'] = 'l';//
    mp['n'] = 'b';
    mp['o'] = 'k';//
    mp['p'] = 'r';//
    mp['q'] = 'z';
    mp['r'] = 't';//
    mp['s'] = 'n';//
    mp['t'] = 'w';//
    mp['u'] = 'j';//
    mp['v'] = 'p';//
    mp['w'] = 'f';
    mp['x'] = 'm';//
    mp['y'] = 'a';
    mp['z'] = 'q';//

    int t;
    int ca = 1;
    scanf("%d",&t);
    getchar();
    while(t--){
        gets(str);//cout<<str<<endl;
        int len = strlen(str);
        int i,j;
        for(i=0;i<len;i++){
            if(str[i]==' ')continue;
            str[i] = mp[str[i]];
        }
        printf("Case #%d: %s\n",ca++,str);
    }
    return 0;
}



















