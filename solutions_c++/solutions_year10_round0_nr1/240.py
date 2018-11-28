/*      
 *      Author: Lokesh Agarwal
 */

#include<cstdio>
#include<cstring>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<iomanip>
#include<vector>
#include<list>
#include<set>
#include<algorithm>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
#define sq(x) ((x)*(x))
#define MM 6110
#define min1(p,q) (p>q?q:p)
#define max1(p,q) (p>q?p:q)
int main()
{freopen("A-large.in","rt",stdin);
	freopen("A.txt","wt",stdout);
    int N,c=0;
    long n,k;
    scanf("%d",&N);
    while(N--)
    {cin>>n>>k;
    c++;
     k++;
     n=1<<n;         
     printf("Case #%d: ",c);
     if(k%n==0)
      printf("ON\n");
      else
      printf("OFF\n");        
              
              
              
    
    }
    //while(1);
return 0;
}
