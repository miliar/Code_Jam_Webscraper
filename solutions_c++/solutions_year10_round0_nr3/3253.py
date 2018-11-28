#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
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
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <time.h>



int main()
{
	freopen("C-small-attempt2.in","r",stdin);freopen("test1.out","w",stdout);
	int testcase;
	///clock_t start,end;
//  double dif;
  int num_in;
  int r;
  int j=0;
  int k;
  int gn;
  int g[9];
  float n1;
  int result=0;
  int temp =0;
  int lastm=0;
  int templ =0;
   // int64 test_time = 62000000000LL;
	scanf("%d",&testcase);

	
	for (int caseId=1;caseId<=testcase;caseId++)
	{    
           scanf("%d",&r);
           scanf("%d",&k) ; 
          scanf("%d",&gn) ;
          for ( int i=0;i<gn;i++)
          scanf("%d",&g[i]);
                j=0;
          for (int i=0;i<r;i++)
          {
                      lastm=0; 
                 
             //    printf("Round %d\n",i); 
              while(1)
              {
                 
              // printf("Count %d\n",j);
                      
                  templ = temp+g[j];
                
                  if(templ>k||lastm>gn-1)
                   {
                             templ=0;
                                   
                             break;
                              
                   }
                  else 
                  {
                       temp += g[j];
                 
                  }
                  lastm++;
                  j++;
                  if(j>gn-1)
                  j=0; 
                  templ = 0;
                  
              }
          
             // printf("Round count %d\n",temp);
              result += temp;
              temp=0;
              
          }
          
        
          temp=0;
          
         printf("Case #%d: %d\n",caseId,result);
          
          
		result=0;
	}


return 0;

}

