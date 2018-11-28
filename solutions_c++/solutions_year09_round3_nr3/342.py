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


int di[4]={-1,0,1,0};
int dj[4]={0,1,0,-1};

int best; int Q,P;

void dfs(vi X,vi sit,int diep,int kost)
{
 

  if(diep==Q)
  { best=min(best,kost); return; }

  int i,j,k;

//for(j=0;j<sz(X);j++) cout << X[j] << endl; cout << endl;
//for(j=0;j<sz(sit);j++) cout << X[j] << endl; cout << endl;
//cout << diep << endl;
//cout << kost << endl;


  for(j=0;j<Q;j++) if(X[j]!=-1)
  {
    vi nuX=X;
    vi nusit=sit;
    int nukost=kost;
    nuX[j]=-1; nusit[X[j]]=0;

    int links=X[j]-1;
    while(links>=0&&nusit[links]) {nukost++; links--; }
    int rechts=X[j]+1;
    while(rechts<P&&nusit[rechts]) {nukost++; rechts++; }

    dfs(nuX,nusit,diep+1,nukost);



  }




}



int main()
{
  int i,j,k;
  char a,b,c;
  char buf[1000];
  int N;
  scanf("%d",&N);
  for(int run=1;run<=N;run++)
  {
    scanf("%d %d",&P,&Q);
    vi X;
    for(j=0;j<Q;j++)
    {  scanf("%d",&k); X.pb(k-1); }
    best=100000000;

    vi bsit(P,1);
    dfs(X,bsit,0,0);
    printf("Case #%d: %d\n",run,best);
  }


  return 0;
}

