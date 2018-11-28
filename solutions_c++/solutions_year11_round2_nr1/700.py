#include<iostream>
#include<cstdio>
#include<algorithm>
#include<vector>
#include<list>
#include<cmath>
#include<queue>
#include<set>
#include<stack>
#define FOR(x,y,z) for(int x=y;x<z;x++)
#define FORD(x,y,z) for(int x=y; x>=z;x--)
#define max3(a,b,c) max(a,max(b,c))
#define PB push_back
#define F first
#define ALL(x) x.begin(),x.end()
#define K(x) ((x)*(x))
#define mabs(x) max(x,-x)
#define S second
#define MP make_pair
#define e 0.00000000001
#define inf 2000000000
using namespace std;

int pl[110],w[110];
double WP[110];
double OWP[110];
double OOWP[110];
vector<int> V[110];
int win[110][110];
int main()
{
   int Z;
   scanf("%d",&Z);
   for(int z=1;z<=Z;z++)
   {
      int n;
      char c;
      scanf("%d",&n);getchar();
      FOR(i,1,n+1)
      {
         FOR(j,1,n+1)
         {
            c=getchar();
            if(c=='1'){win[i][j]=1;win[j][i]=0;w[i]++;}
            if(c!='.'){V[i].PB(j);pl[i]++;}
         }
         getchar();
      }
      FOR(i,1,n+1)
      {
         WP[i]=((1.0)*w[i])/pl[i];
      }
      FOR(i,1,n+1)
      {
         int l=0;
         double s=0;
         FOR(j,0,V[i].size())
         {
            if(win[V[i][j]][i]==1)s+=((1.0)*(w[V[i][j]]-1))/(pl[V[i][j]]-1);
            else if(win[V[i][j]][i]==0)s+=((1.0)*(w[V[i][j]]))/(pl[V[i][j]]-1);
            else  s+=((1.0)*w[V[i][j]])/pl[V[i][j]];
            l++;
         }
         OWP[i]=s/l;
      }
      FOR(i,1,n+1)
      {
         int l=0;
         double s=0;
         FOR(j,0,V[i].size()){l++;s+=OWP[V[i][j]];}
         OOWP[i]=s/l;
      }
      printf("Case #%d:\n",z);
      FOR(i,1,n+1)printf("%lf\n",0.25*WP[i]+0.5*OWP[i]+0.25*OOWP[i]);
      FOR(i,1,n+1)
      {
         FOR(j,1,n+1)win[i][j]=win[j][i]=-1;
         V[i].clear();
         WP[i]=0;
         OWP[i]=0;
         OOWP[i]=0;
         pl[i]=0;
         w[i]=0;
      }
   }
   return 0;
}
