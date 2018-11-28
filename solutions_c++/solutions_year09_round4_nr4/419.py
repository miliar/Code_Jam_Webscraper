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

int X[10000],Y[10000],R[10000];


double bereken(int i,int j)
{
  double d=sqrt((X[i]-X[j])*(X[i]-X[j])+(Y[i]-Y[j])*(Y[i]-Y[j]));

  double r1=R[i];
  double r2=R[j];

  return (d+r1+r2)/2;
}


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
    for(j=0;j<N;j++) scanf("%d %d %d",&X[j],&Y[j],&R[j]);


    if(N==1)
      printf("Case #%d: %.7lf\n",run,double(R[0]));
    else if(N==2)
      printf("Case #%d: %.7lf\n",run,double(max(R[0],R[1])));      
    else
    {
      double best=1e10;
      best=min(best,max(double(R[0]),bereken(1,2)));
      best=min(best,max(double(R[1]),bereken(0,2)));
      best=min(best,max(double(R[2]),bereken(0,1)));
      printf("Case #%d: %.7lf\n",run,best);  
    }

  }



  return 0;
}

