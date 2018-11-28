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


//#define SMALL
#define LARGE
int main() {
int T,N,s,p,i,j,k,l,sur,nor,tot;
float t,avg,mini,normin;
#ifdef SMALL
	freopen("B-small-attempt0.in","rt",stdin);
	freopen("B-small.out","wt",stdout);
#endif
#ifdef LARGE
	freopen("B-large.in","rt",stdin);
	freopen("B-large.out","wt",stdout);
#endif
    cin>>T;
    for(j =1;j<=T;j++)
    {
          sur=0;
          nor=0;
          cin>>N>>s>>p;
          
          printf("Case #%d: ",j);
          normin=(p*3)-3;
          mini=max(((p*3)-4),0);
          if(p==1)
          mini=1;
          for(i =0;i<N;i++)
           {
                cin>>t;
                if(t>normin)
                nor++;
                else if(t>=mini)
                sur++;                              
           }
           tot=min(sur,s)+nor;
           
           cout<<tot<<"\n";
    }
    
    return 0;

}
