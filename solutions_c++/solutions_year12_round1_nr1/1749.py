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
    int T,A,B,i,j,k,back;
    double arr[100000],correct=1,key,ans;
    arr[0]=1;
    #ifdef SMALL
	       freopen("A-small-attempt2.in","rt",stdin);
	       freopen("A-small.out","wt",stdout);
    #endif
    #ifdef LARGE
	       freopen("A-large-practice.in","rt",stdin);
	       freopen("A-large.out","wt",stdout);
    #endif
    cin>>T;
    for(i=1;i<=T;i++)
    {
          cin>>A>>B;
          ans=3*B;
          for(j=1;j<=A;j++)
          {
                  cin>>arr[j];
                  correct=correct*arr[j];
                  
          }

          for(back=0;back<=A;back++)
          {
                   
                   key=(correct)*(B+1+(2*back)) + (1-correct)*((2*B)+(2*back)+2);
                   //cout<<key<<' ';
                   correct=correct/arr[A-back];
                   if(ans>key)
                   ans=key;
         // keeptype=allcorrect*(B+1)+(1-allcorrect)*(B+1)*2;
         //back1=(allcorrect/arr[A])*(B+3)+(1-allcorrect/arr[A])((2*B)+4)
         //back2=()
         }
         if(ans>(A+B+2))
         ans=A+B+2;
         ans=ans-A;
         ans= floor(ans*1000000.0)/1000000.0;
         printf("Case #%d: %.6f\n",i,ans);
         
          
     }
    
	return 0;

}
