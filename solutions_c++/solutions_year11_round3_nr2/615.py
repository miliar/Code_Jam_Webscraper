#include <cstdio>
#include <cmath>
#include <ctime>
#include <memory.h>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <assert.h>
#include <string>
#include <limits.h>

using namespace std;

#define FOR(i, e) for(int i = 0; i < (e); i++)
#define FORS(i, s, e) for(int i = (s); i < (e); i++)
typedef long long ll;
typedef vector<int> ivec;
typedef vector<double> dvec;
typedef vector<string> svec;

int ri(){ int value; scanf("%d", &value); return value; }
ll rl(){ ll value; scanf("%lld", &value); return value; }
double rd(){ double value; scanf("%lf", &value); return value; }
string rs(){ char buf[10000]; scanf("%s", buf); return buf; }
template<class T> void sort(T& c){ sort(c.begin(), c.end()); }
template<class T> void rsort(T& c){ sort(c.begin(), c.end()); reverse(c.begin(), c.end()); }

/*
		printf("%d\n", c);
*/

int solve2(int t, int n, int* dists, int distsSize, int boost1, int boost2)
{
  int elp = 0;

  FOR(i, n)
  {
    int dist = dists[i % distsSize];
    if(boost1 == i || boost2 == i)
    {
      int comp_t = t - elp;
      if(comp_t < 0)
        comp_t = 0;

      int no_boost_len = comp_t / 2;

      if(no_boost_len > dist)
        no_boost_len = dist;
      
      int boost_len = dist - no_boost_len;

      elp += no_boost_len * 2 + boost_len;
    }
    else
    {
      elp += dist * 2;
    }
  }

  return elp;
}

int main()
{
	time_t start;
	time(&start);
	// –{•¶ --------------------------------------

	int t = ri();
	FOR(i, t)
	{
		int l = ri();
		int t = ri();
		int n = ri();
		int c = ri();
		int dists[1000];

		FOR(j, c)
			dists[j] = ri();
		
		int min_t = INT_MAX;
		
		switch(l)
		{
			case 0:
				min_t = solve2(t, n, dists, c, -1, -1);
				break;
				
			case 1:
				FOR(j, n)
				{
					int ret = solve2(t, n, dists, c, j, -1);
					if(ret < min_t)
						min_t = ret;
				}
				break;
			case 2:
				FOR(j, n)
				{
					FOR(k, n)
					{
						if(j >= k)
							continue;
						
						int ret = solve2(t, n, dists, c, j, k);
						if(ret < min_t)
							min_t = ret;
					}
				}
				break;
			default:
				assert(0);
		}

		printf("Case #%d: %d\n", i+1, min_t);
	}

	return 0;
}
