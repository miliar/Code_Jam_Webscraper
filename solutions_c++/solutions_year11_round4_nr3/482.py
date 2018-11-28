#include <iostream>
#include <sstream>  
#include <cstring>
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
  int a,b,c;

  int run,runs;
  scanf("%d",&runs);

  vi priem;
  for(j=2;j<=1000;j++)
  {
    bool isp=true;
    for(int d=2;d*d<=j;d++)
      if(j%d==0) { isp=false; break; }
    if(isp) priem.pb(j);
  }



  for(int kees=1;kees<=runs;kees++)
  {
    printf("Case #%d:",kees);
    long long n;
    scanf("%lld",&n);

    int som=0;
    for(i=0;i<sz(priem)&&priem[i]<n;i++)
    {
      int macht=1;
      while(macht*priem[i]<=n) { macht*=priem[i]; som++; }
      som--;
    }

    if(n==1) printf(" 0\n"); else printf(" %d\n",som+1);
  }




  return 0;
}
