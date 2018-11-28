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

int gcd(int a, int b)
{
	 if(b == 0)return a;
	 else return gcd(b, a % b);
}

int main()
{
	freopen("A-small-attempt2.in", "r", stdin);
	freopen("outsa2.txt", "w", stdout);
	 long long n, pd, pg;
	 int t, cno = 1;
	 scanf("%d",&t);
	 while(t--)
	 {
				  
				  cin >> n >> pd >> pg;
				  printf("Case #%d: ",cno++);
				  if(pd != 100 && pg == 100){printf("Broken\n");continue;}
				  if(pd != 0 && pg == 0){printf("Broken\n"); continue;}
				  int den = 100;
				  int D;
				  if(pd != 0)
				  {
				  int g1 = gcd(pd, den);
				  pd /= g1;
				  den /= g1;
				  if(pd != 100)
				  D = den;
				  else
				  D = n;
				  if(D > n){printf("Broken\n");continue;}
				  }
				  else
				  {
						D = n;
						if(pg == 0){printf("Possible\n");continue;}
						else
						{
                      int den2 = 100;
  			 	  			 int g3 = gcd(pg, den2);
  			 	  			 pg /= g3;
  			 	  			 den2 /= g3;
  			 	  			 int G = den2;
  			 	  			 if(D > G){printf("Broken\n"); continue;}
  			 	  			 else
  			 	  			 printf("Possible\n");
			 	 		}
		  		  }
  			 	  		 	 int den2 = 100;
  			 	  			 int g3 = gcd(pg, den2);
  			 	  			 pg /= g3;
  			 	  			 den2 /= g3;
  			 	  			 int G = den2;
  			 	  if(D > G){printf("Broken\n");continue;}
				  long long x = (pd * D) / 100;
				  long long y = (pg * G) / 100;
				  if(x > y){printf("Broken\n"); continue;}
				  else printf("Possible\n");
  	 }
	return 0;
}
