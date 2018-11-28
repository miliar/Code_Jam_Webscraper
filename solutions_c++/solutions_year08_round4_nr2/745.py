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

char Opp[2501][51][51][6];


int main()
{
  int i,j,k,l,m,n;
  memset(Opp,-1,sizeof(Opp));
 
  int a,b,c,d,e,f;
  for(a=0;a<=0;a++)  //a= gewoon nul
  for(b=a;b<=50;b++)
  for(c=b;c<=50;c++)
  for(d=0;d<=50;d++)
  for(e=0;e<=50;e++)
  for(f=0;f<=50;f++)
  {
    if(d*e*f!=0) continue;   //iets van de y's is 0
    if(a==b&&d==e) continue;
    if(a==c&&d==f) continue;
    if(b==c&&e==f) continue;

    int breed=max(b,c);
    int hoog=max(max(d,e),f);

    long long ak=(a-b)*(a-b)+(d-e)*(d-e);
    long long bk=(b-c)*(b-c)+(e-f)*(e-f);
    long long ck=(a-c)*(a-c)+(d-f)*(d-f);

    long long o=(ak+ck-bk);
    o=(o*o)/4;
    o=ak*ck-o;
//if(
if(o<0) printf("%lld,%lld %lld -> %lld\n",ak,bk,ck,o);
    o=sqrt(o+0.1);

    
    for(m=breed;m<=50;m++)
      for(n=hoog;n<=50;n++)
      {
        Opp[o][m][n][0]=a;
        Opp[o][m][n][1]=d;
        Opp[o][m][n][2]=b;
        Opp[o][m][n][3]=e;
        Opp[o][m][n][4]=c;
        Opp[o][m][n][5]=f;
      }
  }

  scanf("%d",&n);
  for(j=1;j<=n;j++)
  {
    int N,M,A;
    scanf("%d %d %d",&N,&M,&A);
    if(A>2500||Opp[A][N][M][0]==-1)
      printf("Case #%d: IMPOSSIBLE\n",j);
    else
      printf("Case #%d: %d %d %d %d %d %d\n",j,Opp[A][N][M][0],Opp[A][N][M][1],
                                               Opp[A][N][M][2],Opp[A][N][M][3],
                                               Opp[A][N][M][4],Opp[A][N][M][5]);

  }


  
  return 0;
}

