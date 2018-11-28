#include <iostream>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <string>
#include <cstdlib>
#include <sstream>
#include <vector>
#include <algorithm>
#include <functional>
using namespace std;

const double PI = acos(-1.0);
const int MAXINT = 0x7FFFFFFF;
typedef long long int64;
const int64 MAXINT64 = 0x7FFFFFFFFFFFFFFFLL;

#define PS(x) (cout<<#x<<": "<<endl)
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define MST(t,v) memset(t,v,sizeof(t))
#define SHOW1(a,n) (PS(a),_show1(a,n))
#define SHOW2(a,r,c) (PS(a),_show2(a,r,c))

template<class T>void _show1(T a, int n){for(int i=0; i<n; ++i) cout<<a[i]<<' '; cout<<endl;}
template<class T>void _show2(T a, int r, int l){for(int i=0; i<r; ++i)_show1(a[i],l);cout<<endl;}
template<class T> inline void CMAX(T &a,T b){if(b>a) a=b;} 
template<class T> inline void CMIN(T &a,T b){if(b<a) a=b;}

#define MAXE 4096
#define MAXN 1024

struct Node{int p,n;};
Node nd[MAXE*2];
int pos[MAXN], top=1;
#define Add(a,b) (nd[top].p=b,nd[top].n=pos[a],pos[a]=top++)
#define foreach(a,b) for(int _i=pos[a];(b=nd[_i].p),_i;_i=nd[_i].n)
#define Init() (memset(pos,0,sizeof(pos)),top=1)

int P, W, N;
int G[512][512];
int Dist[512];
bool S[512];
void DJ()
{
    memset(Dist, 63, sizeof(Dist));
    memset(S, 0, sizeof(S));
    Dist[1] = 0;
    int i, j;
    int mi;
    while(1)
    {
        mi = -1;
        for(i = 0; i < N; ++i)
        {
            if(!S[i] && (mi == -1 || Dist[i] < Dist[mi]))
                mi = i;
        }
        if(mi == -1) break;
        S[mi] = 1;
        
        foreach(mi, j)
        {
            if(!S[j] && Dist[mi] + 1 < Dist[j])
                Dist[j] = Dist[mi] + 1;
        }
    }
    //for(i = 0; i < N; ++i) printf("%d ", Dist[i]);printf("\n");
}
int res;
int cnt[512];
bool onPath[512];
int n;
void DFS(int p)
{
     int q;
     onPath[p] = 1;
     if(p) --n;
     foreach(p, q)
     {
         if(!onPath[q])
         {
             if(cnt[q] == 0) ++n;
             cnt[q]++;
         }
     }
     if(Dist[p] == 1)
     {
         if(n > res) res = n;
         
         
     }
     else
     {
         foreach(p, q)
         {
             if(Dist[q] == Dist[p] - 1)
                 DFS(q);
         }
     }
     foreach(p, q)
     {
         if(!onPath[q])
         {
             cnt[q]--;
             
             if(cnt[q] == 0) --n;
         }
     }
     onPath[p] = 0;
     if(p) ++n;
}
int main()
{
    freopen("D_S0.in", "r", stdin);freopen("D_S0.out", "w", stdout);
    //freopen("A-large.in", "r", stdin);freopen("A-large.out", "w", stdout);

	int i, j, k;
    int T, cs = 0;
    scanf("%d", &T);
    while(T--)
    {
       Init();
       scanf("%d%d", &P, &W);
       N = P;
       memset(G, 63, sizeof(G));
       
       while(W--)
       {
           scanf("%d,%d", &i, &j);
           Add(i, j);
           Add(j, i);
       }
       
       
       
       DJ();
       
       res = 0;
       n = 0;
       memset(cnt, 0, sizeof(cnt));
       memset(onPath, 0, sizeof(onPath));
       DFS(0);
       printf("Case #%d: %d %d\n", ++cs, Dist[0] - 1, res);
    }
	return 0;
}

