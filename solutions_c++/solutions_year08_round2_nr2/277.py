#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <fstream>
#include <queue>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>


#define SZ size()
#define PB push_back
#define ALL(v) v.begin(),v.end()
#define MP make_pair
#define x first
#define y second

#define LL long long
#define UI unsigned int
#define ULL unsigned long long
#define PI pair<int,int>
#define PD pair<double,double>
#define PLL pair<LL,LL>
#define PULL pair<ULL,ULL>
#define VI vector<int>
#define VD vector<double>
#define VS vector<string>
#define SI set<int>
#define PQ priority_queue
#define VVI vector<vector<int> >
#define IT iterator

#define ABS(x) (((x)>0)?(x):(-(x)))
#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))
#define sign(a) ((a)>0)-((a)<0)
#define sqr(a) ((a)*(a))
#define Repi(n) for (int i=0; i<n; i++)
#define Repj(n) for (int j=0; j<n; j++)
#define Repk(n) for (int k=0; k<n; k++)

#define INF 2000000000
#define EPS 1e-6

#define Time ((double)clock()/CLOCKS_PER_SEC)
#define pause system("pause")

using namespace std;

#define MAXN 1001000
int C,A,B,P;
VI pr[MAXN];
bool sieve[MAXN];
int prime[MAXN],pc;

void eratosthenes(int Max)
{
    sieve[0]=sieve[1]=1; pc=0;
    for (int i=2;i<=Max;i++)
     if (!sieve[i])
      {
            prime[pc++]=i;
            for (int j=i*i;j>0 && j<=Max;j+=i) 
               sieve[j]=1;
      }
}


inline void factorize(int X,vector<int> &tmp)
{
    tmp.clear();
    for (int i=0;prime[i]*prime[i]<=X;i++)
     if (X%prime[i]==0)
      {
            if (prime[i]>=P) tmp.PB(prime[i]);
            while (X%prime[i]==0) X/=prime[i];
      }
    if (X>=P) tmp.PB(X);
}

map<int,VI> adj;

int allsets,N;
int rank[MAXN],par[MAXN];

int find(int x)
{  if (par[x]==x) return x;
   par[x]=find(par[x]);
   return par[x];
}

inline int unite(int x,int y)
{
    int xp=find(x),yp=find(y);
    if (rank[xp]>rank[yp])
     par[yp]=xp,allsets--;
    else
     if (rank[xp]<rank[yp])
      par[xp]=yp,allsets--;
    else
     if (xp!=yp)
      {
            allsets--;
            par[yp]=xp;
            rank[xp]++;
      }
}

int main()
{
    scanf("%d",&C);
    eratosthenes(1000001);
Repk(C)
{
            scanf("%d%d%d",&A,&B,&P);
            //cout<<P<<"\n";
            N=B-A+1;
            allsets=N;
            adj.clear();
            Repi(N)
             {
                    pr[i].clear();
                    factorize(A+i,pr[i]);
                    rank[i]=0,par[i]=i;
                   // cout<<"                   "<<A+i<<" ==> ";
                    Repj(pr[i].SZ)
                     {
                        //cout<<pr[i][j]<<" "; 
                       adj[pr[i][j]].PB(i);
                     } //cout<<endl;
             }
    for (map<int,VI>::IT it=adj.begin(); it!=adj.end(); it++)
     {
           // cout<<"   "<<it->x<<" -> "; Repi(it->y.SZ) cout<<A+it->y[i]<<" "; cout<<endl;
           Repi(it->y.SZ-1)
            unite(it->y[i],it->y[i+1]);
     }
    cout<<"Case #"<<k+1<<": "<<allsets<<"\n";


}
     
    return 0;
}
