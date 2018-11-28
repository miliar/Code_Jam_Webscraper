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
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	///clock_t start,end;
//  double dif;
  int num_in;
  int n;
  int k;
  float n1;
   // int64 test_time = 62000000000LL;
	scanf("%d",&testcase);
	for (int caseId=1;caseId<=testcase;caseId++)
	{    
           scanf("%d",&n);
           scanf("%d",&k) ; 
          
          n1=(float)n;
        //  printf("%d",(int)pow(2,n1));
          
           if((k+1)%(int)pow(2,n1)==0)
           printf("Case #%d: ON\n",caseId);
           else
           printf("Case #%d: OFF\n",caseId);
          
		
	}


return 0;

}

