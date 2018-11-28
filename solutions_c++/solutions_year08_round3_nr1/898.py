#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
using namespace std;
#define SZ(x) (int)(x.size())
#define F0(i,n) for(i=0;i<n;i++)
#define F1(i,n) for(i=1;i<=n;i++)

int i, j, k, m, n, l,x,p, ount;
int a[1000][1000];
multimap<int,int> freq_alpha;

int main() 
{
  	freopen("A-small-attempt0.in", "r", stdin);
  	freopen("out.txt", "w", stdout);
//  freopen("input.txt", "r", stdin);
  int tt, tn;
  cin >> tn;

  F1(tt,tn) 
  {
    freq_alpha.clear();
    memset(a,0,sizeof(a));
    ount = 0;
    
    cin >> p >> k >> l; 
    F1(i,l) 
    {
      cin >> x ;
      freq_alpha.insert(pair<int,int>(x,i));
    }
    printf("Case #%d:", tt);
    multimap<int,int>::iterator pos;
    pos = freq_alpha.end();
    pos--;
    for (;; --pos)
    {
      F0(x,p) 
      {
        F0(j,k) 
        {
          if(a[j][x]==0)
          {
            ount+=(pos->first*(x+1));
            a[j][x]=1;
            goto outt;
          }
        }
      }
outt:
      if(pos == freq_alpha.begin())
        break;
    }
    printf(" %d\n", ount);
  }

  return 0;
}
