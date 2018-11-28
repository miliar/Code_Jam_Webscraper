/*

 E-Mail : mayank.ry@gmail.com
 Just For You :)

 */

#include <cstring>
#include <string.h>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <vector>
#include <set>
#include <complex>
#include <list>

using namespace std;


#define SMALL
//#define LARGE
int main() 
{
int T,A,B,n,m,i,j,k,l,p,pairs,carry;
#ifdef SMALL
	freopen("C-small-attempt0.in","rt",stdin);
	freopen("C-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("C-large-practice.in","rt",stdin);
	freopen("C-large.out","wt",stdout);
#endif
    cin>>T;
    for(j =1;j<=T;j++)
    {
          
          cin>>A>>B;
          pairs=0;
          printf("Case #%d: ",j);
          for(n =max(A,10);n<=B;n++)
           {    
                if(n/1000!=0)
                p=3;
                else if(n/100!=0)
                p=2;
                else if(n/10!=0)
                p=1;
                else
                p=0;
                k=10;
                for(i=1;i<=p;i++)
                {
                       carry=(n%k)*(int(pow(10.0,(p+1))))/k;
                       m=n/k+carry;                   
                       if(m!=n&&m>=A&&m<=B)
                       {
                       pairs++;
                       // cout<<n<<' '<<int(m)<<"   "<<carry<<'\n';
                        }
                        k=k*10;
                }
           }   
           
           cout<<pairs/2<<"\n";
    }
    
    return 0;

}

