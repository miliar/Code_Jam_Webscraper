#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

#define FOR(zzz,a) for(int zzz=0; zzz<(int)(a); zzz++)
#define FORE(zzzz,a) for(int zzzz=1; zzzz<=(int)(a); zzzz++)
#define All(v) (v).begin(), (v).end()
#define zfill(a) memset(&a, 0 , sizeof(a))
#define nfill(a) memset(&a, -1, sizeof(a))
#define S(aaa) scanf("%d",&aaa)

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef unsigned int uint;

int main()
{
  int p,q,pris[105],cell[10];
  int t,x,i;
  S(t);
  FOR(x,t)
  {
          S(p),S(q);
          nfill(pris);
          int gold;
          
          FOR(i,q)
          S(cell[i]);
          
          int mi=100000000;
          
          do
          {
              gold = 0;
              nfill(pris);
                FOR(i,q)
                {
                        //cout<<"q : "<<q<<"  cell : "<<cell[i]<<endl;
                        pris[cell[i]]=0;                        
                        int j;
                        for(j=cell[i]+1;j<=p && pris[j]!=0;j++)
                        gold++;
                        for(j=cell[i]-1;j>0 && pris[j]!=0;j--)
                        gold++;                        
                }    
                mi = min(gold,mi); 
                //cout<<"gold : "<<gold<<endl;
          }          
          while( next_permutation(cell,cell+q) );  
          
          cout<<"Case #"<<x+1<<": "<<mi<<endl;                   
  }
return 0;
}
