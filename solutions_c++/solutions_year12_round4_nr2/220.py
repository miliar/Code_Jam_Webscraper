#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cassert>
#include<cmath>
#include<vector>
#include<set>
#include<map>
#include<list>
#include<deque>
#include<queue>
#include<stack>
#include<functional>
#include<sstream>
#include<iostream>
#include<ctime>
#include<algorithm>
using namespace std;

#define DEBUG(x...) printf(x)
#define allv(v) (v).begin(),(v).end()
#define rall(v) (v).begin(),(v).rend()
#define _foreach(it,b,e) for(__typeof__(b); it!=(e);++it)
#define foreach(x...) _foreach(x)

typedef long long int huge;

const int inf = 0x3f3f3f3f;
const huge hugeinf = 0x3f3f3f3f3f3f3f3fll;//dois L's
const double eps = 1e-9;
const int maxn = 1111;
int n,w,l;
pair<int,int> raio[maxn];
double ans[maxn][2];
int maior = 0;
bool ok;
void pack(){
  int x=0,y=-raio[0].first;
  int mai = 0;
  for(int i=0;i<n;i++){
    int v = raio[i].second;
    y+=raio[i].first;
    if(y>l){
      y=0;
      x = x + mai + maior;
    }
    if(x>w)return;
    ans[v][0]=x;
    ans[v][1]=y;
    y+=raio[i].first;
    mai=max(mai,raio[i].first);
  }
  bool dah = true;
  for(int i=0;i<n;i++){
    if(ans[i][0]>w)dah=false;
  }
  ok=dah;
}
int main ()
{
  int tt;
  scanf("%d",&tt);
  for(int pp=1;pp<=tt;pp++)
    {
      ok = false;
      maior = 0;
      scanf("%d %d %d",&n,&w,&l);
      for(int i=0;i<n;i++){
        scanf("%d",&raio[i].first);
        maior=max(raio[i].first, maior);
        raio[i].second=i;
      }
      int troca = 0;
      for(int ppp=0;ppp<2;ppp++){
        for(int vv=0;!ok && vv<1000000*n;vv++){
          random_shuffle(raio,raio+n);
          pack();
        }
        if(ok)break;
        swap(w,l);
        troca = 1;
      }
      assert(ok);
      //  printf("%d\n",ok);
      printf("Case #%d:",pp);
      for(int i=0;i<n;i++)
        printf(" %lf %lf",ans[i][troca],ans[i][1-troca]); 
      printf("\n");
    }
  return 0;
}
