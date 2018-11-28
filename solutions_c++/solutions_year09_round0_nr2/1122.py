#include<cstdio>
#include<vector>
#include<algorithm>
#include<cmath>
#include<queue>

#define ffor(i,n) for(int i=0; i<n; i++)
#define rep(i,n) for(int i=1; i<=n; i++)
#define forit(it,n) for(typeof(n.begin()) it=n.begin(); it!=n.end(); it++)
#define scf(n) scanf("%d", &n);
#define psh push_back
#define mkp make_pair
#define frs first
#define sec second
#define pii pair<int,int>
#define INF 1000000000
#define LL long long
#define LD long double

using namespace std;
const int xam=110;
const int liter=96;

int dane[xam][xam];
pii aim[xam][xam];
int vis[xam][xam][xam];
int height,width;

vector<pii > graf[xam][xam][xam];

void set_aim(int t,int h, int w)
{
    pii a=mkp(INF,INF);
    int mini=dane[h][w];
    if(dane[h-1][w]<mini && h-1>0) {mini=dane[h-1][w]; a=mkp(h-1,w);}
    if(dane[h][w-1]<mini && w-1>0) {mini=dane[h][w-1]; a=mkp(h,w-1);}
    if(dane[h][w+1]<mini && w+1<=width) {mini=dane[h][w+1]; a=mkp(h,w+1);}
    if(dane[h+1][w]<mini && h+1<=height) {mini=dane[h+1][w]; a=mkp(h+1,w);}
    
    if(a.frs!=INF) {graf[t][h][w].psh(a); graf[t][a.frs][a.sec].psh(mkp(h,w));}
}

void bfs(int t,int h, int w, int count)
{
    pii temp;
    queue<pii > q;
    q.push(mkp(h,w));
    vis[t][h][w]=count;
    
    while(q.size())
    {
	temp=q.front(); q.pop();
	forit(it,graf[t][temp.frs][temp.sec])
	{
	    if(vis[t][it->frs][it->sec]) continue;
	    vis[t][it->frs][it->sec]=count;
	    q.push(*it);
	}
    }
}

void play(int t)
{
    scanf("%d%d", &height,&width);
    rep(i,height)
    {
	rep(j,width) scanf("%d", &dane[i][j]);
    }
    
    rep(i,height)
    {
	rep(j,width) set_aim(t,i,j);
    }
    
    int count=1;
    rep(i,height)
    {
	rep(j,width) {if(!vis[t][i][j]) {bfs(t,i,j,count); count++;}}
    }
    
    /*rep(i,height)
    {
	rep(j,width) 
	{
	    printf("%d,%d: ", i,j);
	    forit(it,graf[t][i][j]) printf("(%d,%d) ", it->frs, it->sec);
	}
	printf("\n");
    }*/
    
    rep(i,height)
    {
	rep(j,width) printf("%c ", vis[t][i][j]+liter); printf("\n");
    }
}

int main()
{
    
    int t;
    scanf("%d", &t);
    rep(i,t)
    {
	printf("Case #%d:\n", i);
	play(i);
    }

    return 0;
}