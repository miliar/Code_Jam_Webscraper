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

using namespace std;

int a[11] = {1,3,7,15,31,63,127,255,511,1023,2047};

int main()
{
  freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
  int testcase;
  scanf("%d",&testcase);
  for (int caseId=1;caseId<=testcase;caseId++)
	{
		printf("Case #%d: ",caseId);
		long long n,m;
		scanf("%lld%lld",&n,&m);
                //std::cout << n << m << std::endl;
		if (m == 0) {
		  printf("OFF\n");
		  continue;
		} else {
		  long long tmp = (1<<n)-1;
		  if ((tmp&m)==tmp) {
		  printf("ON\n");
		    continue;
		  } else {
		    //std::cout << m<<n << std::endl;
		    printf("OFF\n");
		    continue;
		  }
		}
		
		/*
		else if (n > m) {
		  printf("OFF\n");
		  continue;
		} else {
		  int f = 1;
		  for (int i = 0; i < n; ++i){
		    if (((m>>i) & 1) == 0) f = 0; 
		  }
		  if (f == 1) {
		    printf("ON\n");
		    continue;
		  } else {
		    //std::cout << m<<n << std::endl;
		    printf("OFF\n");
		    continue;
		  }
		*/
	
		fflush(stdout);
	}
  return 0;
}
