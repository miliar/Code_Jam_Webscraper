

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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>



int main()
{
	long unsigned int  R,k,N;
	long unsigned int  g;
	printf("\nHello GCJ");

		freopen("C-small-attempt0.in","r",stdin);
		freopen("Output.out","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	vector<long unsigned int> v1;
	bool all_filled_in_queue = false;
	scanf("%d",&testcase);
	
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		scanf("%u%u%u",&R,&k,&N);
		long unsigned int earnings = 0;

		for(int grp_no = 1; grp_no <= N; grp_no++)
		{
			scanf("%u",&g);
			v1.push_back(g);
		}
		long unsigned int trip_cntr = 0; 
		unsigned int main_ptr = 0;
		while(trip_cntr < R )
		{
			long unsigned int this_trip = 0;
			long unsigned int no_of_groups = 0;
			while(1)
			{
				if((this_trip + v1[main_ptr]) <= k)
				{
					if(no_of_groups >= N)
					{
						earnings += this_trip;
						break;
					}

					this_trip += v1[main_ptr];
					no_of_groups++;
					if(main_ptr == N-1)
						main_ptr = 0;
					else
						main_ptr++;

				}
				else
				{
					earnings += this_trip;
					break;
				}
			}

			trip_cntr++;
			

		}

		printf("Case #%d: %u\n",caseId,earnings);
		v1.clear();
		

	}
	return 0;
}

