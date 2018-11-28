#include <iostream>  
#include <sstream>  
#include <string>  
#include <vector>  
#include <queue>  
#include <set>  
#include <map>  
#include <cstdio>  
#include <cstdlib>  
#include <cctype>  
#include <cmath>  
#include <list>  
#include <numeric> 
#include <ctime>
#include <algorithm>
using namespace std;  
  
typedef vector<int> vi;  
typedef vector<vi> vvi;  
typedef vector<string> vs;  
typedef vector<vs> vvs; 
#define pb push_back  
#define sz(v) ((int)(v).size()) 


const int EN=1,OF=0;
int poort[30];
int waarde[30];
bool aanpasbaar[30];

int poortkopie[30];
int waardekopie[30];

int inter,M;


int resultaat()
{
/*printf("\nvoor:\n"); int j;
    for(j=0;j<inter;j++)
      printf("%d",poortkopie[j]); printf("\n");
    for(j=0;j<M;j++)
      printf("%d",waardekopie[j]);printf("\n");
*/
  for(int k=inter-1;k>=0;k--)
  {
    if(poortkopie[k]==EN)
    {
      waardekopie[k]=0;
      if(waardekopie[2*k+1]==1&&waardekopie[2*k+2]==1) waardekopie[k]=1;
    }
    else
    {
      waardekopie[k]=1;
      if(waardekopie[2*k+1]==0&&waardekopie[2*k+2]==0) waardekopie[k]=0;
    }
  }

/*printf("\n na:\n"); 
    for(j=0;j<inter;j++)
      printf("%d",poortkopie[j]); printf("\n");
    for(j=0;j<M;j++)
      printf("%d",waardekopie[j]);printf("\n");
printf("--------------");*/
  return waardekopie[0];
}


int main()
{
  int c,i,j,k,l,m,n; int V;
  scanf("%d",&n);
  for(c=1;c<=n;c++)
  {
    memset(waarde,0,sizeof(waarde));
    memset(poort,0,sizeof(waarde));
    scanf("%d %d",&M,&V); 
    inter=(M-1)/2; int blad=M-inter;
    for(j=0;j<inter;j++)
      scanf("%d %d",&poort[j],&aanpasbaar[j]);
    for(j=inter;j<M;j++)
      scanf("%d",&waarde[j]);



    int best=50;
    for(int s=0;s<(1<<inter);s++)
    {
      bool magwel=true; int bits=0;
      for(i=0;i<inter;i++)
      {
        if((s&(1<<i))&&!aanpasbaar[i])
          magwel=false;
        if(s&(1<<i)) bits++;
      }
      if(!magwel) continue;

      for(i=0;i<M;i++)
      { poortkopie[i]=poort[i]; waardekopie[i]=waarde[i]; 
        if(s&(1<<i)) poortkopie[i]=1-poortkopie[i];
      }

      if(resultaat()==V)
        best=min(best,bits);
    }

    if(best==50)
      printf("Case #%d: IMPOSSIBLE\n",c);
    else
      printf("Case #%d: %d\n",c,best);      

  }
  
  return 0;
}

