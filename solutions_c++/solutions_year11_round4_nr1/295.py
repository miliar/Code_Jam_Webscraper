#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <limits>
#include <vector>
#include <queue>
#include <map>
#include <set>
#include <list>
#include <string>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
const int INF = numeric_limits<int>::max();

int main(int argc,char* argv[])
{
    int num_test_cases;
    scanf("%d",&num_test_cases);
    for(int test_case=1; test_case<=num_test_cases; test_case++)
    {
		vector< pii > walkways;
		int x, s, r, t, n;
		scanf("%d%d%d%d%d", &x, &s, &r, &t, &n);
		double rt = t;
		int wt = 0;
		for(int i=0;i<n;i++)
		{
			int b, e, w;
			scanf("%d%d%d", &b, &e, &w);
			walkways.push_back(make_pair(w, e-b));
			wt += e-b;
		}
		walkways.push_back(make_pair(0, x-wt));
		sort(walkways.begin(), walkways.end());
		double T = 0;
		for(int i=0;i<walkways.size();i++)
		{
			int w = walkways[i].first;
			double d = walkways[i].second;
			if(rt>0)
			{
				double dt = min(d/(w+r), rt);
				rt -= dt;
				T += dt;
				//printf("run: %d %d %lf, %lf %lf\n", i, d, T, dt, rt);
				d -= dt*(w+r);
			}
			T += d/(w+s);
			//printf("%d %d %lf\n", i, d, T);
		}
		printf("Case #%d: %lf\n",test_case, T);
	
    }
    return 0;
}
