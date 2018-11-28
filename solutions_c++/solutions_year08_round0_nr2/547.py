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
typedef unsigned long long ull; 
#define pb push_back  
#define sz(v) ((int)(v).size()) 

int tel[2][26*60];



int main()
{
  int i,j,k,m,n,s,q,a1,a2,a3,a4; 
  int N,S,Q,NA,NB,T,t1,t2;

  scanf("%d",&N);
  for(n=1;n<=N;n++)
  {
    memset(tel,0,sizeof(tel));
    scanf("%d %d %d",&T,&NA,&NB);
    for(j=0;j<NA;j++)
    {
      scanf("%d:%d %d:%d",&a1,&a2,&a3,&a4);
      t1=a1*60+a2; t2=a3*60+a4+T;
      tel[0][t1]--;
      tel[1][t2]++;
    }
    for(j=0;j<NB;j++)
    {
      scanf("%d:%d %d:%d",&a1,&a2,&a3,&a4);
      t1=a1*60+a2; t2=a3*60+a4+T;
      tel[1][t1]--;
      tel[0][t2]++;
    }
    int som[2]={0,0};

    for(k=0;k<2;k++)
    {
      int rest=0;
      for(j=0;j<24*60;j++)
      {
        rest+=tel[k][j];
        if(rest<0)
        {
          som[k]-=rest;
          rest=0;
        }
      }
    }

    printf("Case #%d: %d %d\n",n,som[0],som[1]);
  }

  return 0;
}
