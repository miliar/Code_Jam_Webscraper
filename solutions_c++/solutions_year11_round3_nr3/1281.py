#include <iostream>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>
#include <complex>
#include <climits>
#include <cstdlib>
using namespace std;

#define pi (2 * acos(0))
#define eps 1e-9
#define li(v) v.begin(),v.end()
#define fo(i,j,n) for(i=j; i<n; ++i)

typedef long long int64;
typedef unsigned long long uint64;
typedef unsigned uint32;

int main()
{
    freopen("C-small-attempt2.in", "r", stdin);
	 freopen("freqs1.txt", "w", stdout);
	 int t,cno = 1;
	 scanf("%d",&t);
	 while(t--)
	 {
				  int n, l, h;
				  scanf("%d%d%d",&n,&l,&h);
				  int fr[n];
				  for(int i = 0; i < n; i++)
				          scanf("%d",&fr[i]);
				  int ans = -1;
				  for(int j = l; j <= h; j++)
				  {
							 int nfq = j;
							 bool flag[n];
							 for(int i = 0; i < n; ++i)flag[i] = false;
							 for(int i = 0; i < n; ++i)
							 {
										if(fr[i] % nfq == 0 || nfq % fr[i] == 0){flag[i] = true;}
			  				 }
							 bool f2 = true;
							 for(int i = 0; i < n; ++i)if(!flag[i])f2 = false;
			  				 if(f2){ans = nfq;break;}
  			 	  }
  			 	  printf("Case #%d: ", cno++);
  			 	  if(ans == -1)printf("NO\n");
  			 	  else
  			 	  {
						printf("%d\n", ans);
  				  }
  	 }
	 return 0;
}
