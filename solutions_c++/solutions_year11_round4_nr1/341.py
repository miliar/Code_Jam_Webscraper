#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 
#include <memory.h>

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

int X;
int S;
int R;
int t;

struct Walkway
{
	double len;
	double w;

	bool operator<(const Walkway& ww) const {

		double a = -(double)len / ((double)R + w) /((double)S + w);
		double b = -(double)ww.len / ((double)R + ww.w) /((double)S + ww.w);

		return a < b;

		//return len > ww.len;

	}
};

int main(int argc, char* argv[])
{
#ifndef ONLINE_JUDGE
	freopen("test.in", "r", stdin);
#endif
	int T;
	scanf("%d", &T);

	for (int nTest = 1; nTest <= T; nTest++)
	{		

		cin >> X;
		cin >> S;
		cin >> R;
		cin >> t;
		int N;
		cin >> N;

		int totalWalk = X;

		vector<Walkway> w;
		rep(i, N)
		{
			int b, e;
			int www;
			cin >> b>> e >> www;

			for (int j = 0; j < (e - b); j++)
			{
				Walkway ww;
				ww.len = 1;
				ww.w = www;
				w.push_back(ww);
			}
			totalWalk -= e - b;
		}
 
		for (int j = 0; j <  totalWalk; j++)
		{
			Walkway ww;
			ww.len = 1;
			ww.w = 0;

			w.push_back(ww);
		}

		sort(w.begin(), w.end());

#if 1
		double totalTime = 0;
		double timeRun = t;

		for (int i = 0; i < w.size(); i++)
		{
			Walkway cur = w[i];

			if (timeRun > 0)
			{
				double timeCover = (double)cur.len / (cur.w + R);
				if (timeCover <= timeRun)
				{
					timeRun -=timeCover;
					totalTime += timeCover;
				}
				else
				{
					double c = timeRun * (cur.w + R);

					totalTime += timeRun + (cur.len - c) / (cur.w + S);

					timeRun = 0;
				}
			}
			else
			{
				totalTime += ((double)cur.len) / (cur.w + S);
			}
		}	
#else

		double totalTime = 1e9;

		for (int needRun = 0; needRun < 1 << w.size(); needRun++)
		{
			double curTime = 0;
			double timeRun = t;

			for (int i = 0; i < w.size(); i++)
			{
				Walkway cur = w[i];

				if (timeRun > 0 && needRun & (1 << i))
				{
					double timeCover = (double)cur.len / (cur.w + R);
					if (timeCover <= timeRun)
					{
						timeRun -=timeCover;
						curTime += timeCover;
					}
					else
					{
						double c = timeRun * (cur.w + R);

						curTime += timeRun + (cur.len - c) / (cur.w + S);

						timeRun = 0;
					}
				}
				else
				{
					curTime += ((double)cur.len) / (cur.w + S);
				}
			}

			totalTime = min(totalTime, curTime);

		}
#endif



		printf("Case #%d: %.8lf\n", nTest, totalTime);
		fflush(stdout);
	} 


	return 0;
}


