#include <iostream>
#include <sstream>
#include <cstring>
#include <vector>
#include <queue>
#include <deque>
#include <stack>
#include <set>
#include <map>
#include <cstdlib>
#include <cstdio>
#include <cctype>
#include <cmath>
#include <list>
#include <numeric>
#include <algorithm>
using namespace std;

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<string> vs;
typedef vector<vs> vvs;
#define pb push_back
#define sz(v) (int)(v.size())

int Q[1000000]; int b,e;
int boom[15*50000][26];


int main()
{ 
  int i,j,k;
  int L,D,N; char buf[10000];
  scanf("%d %d %d",&L,&D,&N);

  memset(boom,-1,sizeof(boom));
  int sijs=1;

  for(j=0;j<D;j++)
  {
    scanf("%s",buf);
    int wijs=0;
    for(int p=0;p<L;p++)
      if(boom[wijs][buf[p]-'a']!=-1)
        wijs=boom[wijs][buf[p]-'a'];
      else
        wijs=boom[wijs][buf[p]-'a']=sijs++;
  }
        
  
  for(j=0;j<N;j++)
  {
    scanf("%s",buf);
    Q[0]=0; int bufwijs=0; b=0; e=0; int qs=1;
    for(k=0;k<L;k++)
    {
      b=e; e=qs; 
      bool wacht=buf[bufwijs]=='(';
      if(buf[bufwijs]=='(') bufwijs++;
      for(;buf[bufwijs]!=')';bufwijs++)
      {
        for(int w=b;w<e;w++)
        {
          if(boom[Q[w]][buf[bufwijs]-'a']!=-1)
            Q[qs++]=boom[Q[w]][buf[bufwijs]-'a'];
        }
        if(!wacht) { bufwijs++; break; }
      }
      if(wacht) bufwijs++;
//printf("b=%d e=%d qs=%d bufwijs=%d\n",b,e,qs,bufwijs);
    }

//for(k=0;k<qs;k++) printf("[%d]",Q[k]); printf("\n");
  
    printf("Case #%d: %d\n",j+1,qs-e);
  }






  return 0;
}
