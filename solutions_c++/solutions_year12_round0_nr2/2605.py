
#include <vector>
#include <cstdio>
#include <cstdlib>
#include <cassert>

using namespace std;

int main(int argc, char* argv[])
{
	int T;

	scanf(" %d", &T);
	for(int t = 1; t <= T; t++)
	{
		int N, S, p;
		scanf(" %d %d %d", &N, &S, &p);
		//printf("N=%d S=%d p=%d\n", N, S, p);

		vector<int> total_pts;
		total_pts.resize(N);
		for(int n = 0; n < N; n++)
		{
			scanf(" %d", &total_pts[n]);
		}

		
		//int total_surprising = 0, total_surprising_or_not_surprising = 0, max_above = 0;
		int above_s_only = 0, above_ns_only = 0, above_either = 0;
		for(int i = 0; i < N; i++)
		{
			bool s_below = false, s_above = false, ns_below = false, ns_above = false;
			//printf("total pts: %d\n", total_pts[i]);
			// find surprising, two #'s differ by 2
			for(int x = max(0, (total_pts[i]-12)/2); x <= (total_pts[i]-2)/2 && (x/*+2*/)<= min(10, total_pts[i] - 2*x - 2); x++)
			{
			assert(x >= 0);
			assert(x <= 10);
			if ((abs(x - (total_pts[i] - 2*x - 2)) <=2) && abs((x+2) - (total_pts[i] - 2*x - 2)) <=2)
			{
				//printf("SP(%d, %d, %d) = %d\n", x, x + 2, total_pts[i] - 2*x - 2, total_pts[i]);
				if (max(x+2, total_pts[i] - 2*x - 2) >= p)
				//if (x >= p)
					s_above = true;
				else
					s_below = true;
				if (s_above && s_below) break;
			}
			}
			// find not surprising differ by 0
			for(int x = max(0, (total_pts[i]-10)/2); x <= total_pts[i]/2 && x<= min(10, total_pts[i] - 2*x); x++)
			{
			    assert(x >= 0);
			     assert(x <= 10);
				 if (abs(x - (total_pts[i] - 2*x)) <= 1)
				 {
				 //printf("NP0(%d, %d, %d) = %d\n", x, x, total_pts[i] - 2*x, total_pts[i]);
				 //assert((total_pts[i] - 2*x) >= 0);
				 //assert((total_pts[i] - 2*x) <= 10);
				// differ by 0:
				if (max(x, total_pts[i] - 2*x) >= p)
				//if (x >= p)
					ns_above = true;
				else
					ns_below = true;
				if (ns_above && ns_below) break;
				}
				
			}
			// find not surprising differ by 1
			for(int x = max(0, (total_pts[i]-11)/2); x <= (total_pts[i]-1)/2 && (x/*+1*/)<=min(10 , total_pts[i] - 2*x - 1); x++)
			{
			assert(x >= 0);
			assert(x <= 10);
			if ((abs((x+1) - (total_pts[i] - 2*x - 1)) <= 1) && abs(x - (total_pts[i] - 2*x - 1)) <= 1)
			{
				//printf("NP1(%d, %d, %d) = %d\n", x, x+1, total_pts[i] - 2*x - 1, total_pts[i]);
			//assert((total_pts[i] - 2*x - 1) >= 0);
			//assert((total_pts[i] - 2*x - 1) <= 10);
				if (max(x+1, total_pts[i] - 2*x - 1) >= p)
				//if (x >= p)
					ns_above = true;
				else
					ns_below = true;
				if (ns_above && ns_below) break;
			}
			}

			
			
			//printf("s_below=%d, s_above=%d, ns_below=%d, ns_above=%d\n", s_below, s_above, ns_below, ns_above);
			
			if (s_above && !ns_above)
				above_s_only++;
			if (ns_above && !s_above)
				above_ns_only++;
			if (ns_above || s_above)
				above_either++;
		
	
		}
		
		above_either -= above_s_only;
		above_either -= above_ns_only;
		//printf("above_s_only: %d, above_ns_only: %d, above_either: %d\n", above_s_only, above_ns_only, above_either);
		
		int count = 0, s_left = S, ns_left = N-S;
		if (above_s_only >= S)
		{
			count = S;
			s_left -= S;
		}
		else
		{
			s_left -= above_s_only;
			count = above_s_only;	
		}
			
		assert(count >= 0 && count <= N);
		//printf("count s_above only: %d\n", count);
		
		if (above_ns_only >= (N-S))
		{
			ns_left -= (N-S);
			count = min(count + (N-S), N);
		}
		else
		{
			ns_left -= above_ns_only;
			count = min(N, count + above_ns_only);
		}
			
		assert(count >= 0 && count <= N);
		//printf("count: %d, sleft=%d, ns_left=%d\n", count, s_left, ns_left);

		while(above_either > 0 && ns_left > 0)
		{
			above_either--;
			count++;
			ns_left--;
		}
		while(above_either > 0 && s_left > 0)
		{
			above_either--;
			count++;
			s_left--;
		}
		
		assert(count >= 0 && count <= N);
		printf("Case #%d: %d\n", t, count);

	}


	return 0;
}
