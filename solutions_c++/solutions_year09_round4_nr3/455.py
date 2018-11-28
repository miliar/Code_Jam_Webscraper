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

bool mag[16][16];

int data[16][25];

int n,k,best;

bool magsamen(int a, int b)
{
  int i,j,l,m;

  for(i=0;i<k-1;i++)
    if((data[a][i]>data[b][i]&&data[a][i+1]<data[b][i+1])||
       (data[a][i]<data[b][i]&&data[a][i+1]>data[b][i+1])||
       (data[a][i]==data[b][i]||data[a][i+1]==data[b][i+1]))
      return false;

  return true;

}

int groepen[16];

void dieper(int g,int d)
{
  if(g>=best) return;
  if(d==n) { best=min(g,best); return; }

  for(int groep=0;groep<g;groep++)
  {
    bool isok=true;
    for(int j=0;j<d&&isok;j++) if(groep==groepen[j])
      if(!mag[j][d])
        isok=false;
    if(isok) { groepen[d]=groep; dieper(g,d+1); }
  }
  groepen[d]=g;
  dieper(g+1,d+1);

}





int main()
{
  int i,j;
  char a,b,c;
  char buf[1000];
  int runs,run;
  scanf("%d",&runs);
  for(run=1;run<=runs;run++)
  {

    scanf("%d %d",&n,&k); memset(mag,true,sizeof(mag));
    best=n;

    for(j=0;j<n;j++)
      for(i=0;i<k;i++)
        scanf("%d",&data[j][i]);    

    for(j=0;j<n;j++)
      for(i=j+1;i<n;i++)
        mag[j][i]=mag[i][j]=magsamen(j,i);

    dieper(0,0);



    printf("Case #%d: %d\n",run,best);
  }



  return 0;
}

