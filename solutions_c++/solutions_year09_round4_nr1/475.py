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




int main()
{
  int i,j,k;
  char a,b,c;
  char buf[1000];
  int runs,run;
  scanf("%d",&runs);
  for(run=1;run<=runs;run++)
  {
    int N;
    scanf("%d",&N);
    vi C(N,0);
    for(j=0;j<N;j++) 
    {
      scanf("%s",buf);
      for(i=0;i<N;i++)
        if(buf[i]=='1') C[j]=i;
    }
//for(k=0;k<N;k++) printf("%d ",C[k]); printf("\n");

    int tel=0;


    for(j=0;j<N;j++)
    {
      for(k=j;k<N;k++) if(C[k]<=j)
      {
        tel+=k-j;
        for(i=k;i>j;i--) swap(C[i],C[i-1]);
        break;
      }
//for(k=0;k<N;k++) printf("%d ",C[k]); printf("\n");
    }












    printf("Case #%d: %d\n",run,tel);
  }





  return 0;
}

