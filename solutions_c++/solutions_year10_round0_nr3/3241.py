#include <cstdio>
#include <vector>
#include <queue>
#define FOR(x,y,z) for(int x=y;x<z;x++)
#define R 1001000
#define LLD long long int
using namespace std;
LLD tab[R];
LLD sumki[1000010];
LLD n;
inline bool cykl(LLD p)
{
  FOR(i,0,n)
  {
    if(!(tab[p%n]==tab[i]))
      return false;
    p++;
  }
  return true;   
}
int main()
{
  int Z;
  scanf("%d",&Z);
  FOR(j,1,Z+1)
  {
    LLD r,k;
    scanf("%lld%lld%lld",&r,&k,&n);
    FOR(i,0,n)
      scanf("%lld",tab+i);
    LLD p=0;
    LLD suma=0;
    FOR(i,0,r)
    {
      LLD sum=0;
      LLD li=0;
      while(sum+tab[p%n]<=k&&li<n)
      {
        sum+=tab[p%n];p++; 
        li++;
        p=p%n;
      }
      /*if(i<100000000)
      {
        sumki[i]=(i>0?sumki[i-1]:0)+sum;
        if(cykl(p)){if(i>0)suma+=((r-i)/(i))*sumki[i]+sumki[(r-i)%(i)];
          else
          suma+=r*sumki[i];
       // printf("SEKS\nLOL %d\n",i);
        break;
        }
      }*/
      suma+=sum;
    }
    printf("Case #%d: %lld\n",j,suma);
    FOR(i,0,n){tab[i]=sumki[i]=0;}
  }
  return 0;
}

