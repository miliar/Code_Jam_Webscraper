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

int main()
{
	time_t start;
	time(&start);
	// –{•¶ --------------------------------------

	int t = ri();
	FOR(i, t)
	{
		int n = ri();
		int l = ri();
		int h = ri();
		
		int others[100];
		
		FOR(j, n)
		{
			others[j] = ri();
		}
		
		int ans = -1;
		for(int f=l; f<=h; f++)
		{
			bool ok = true;
			FOR(j, n)
			{
				if(others[j] == 0)
					continue;
			
				if(others[j] % f == 0 || f % others[j] == 0)
				{
					// ok
				}
				else
				{
					ok = false;
					goto skip;
				}
			}
skip:
			if(ok)
			{
				ans = f;
				break;
			}
		}

		if(ans != -1)
			printf("Case #%d: %d\n", i+1, ans);
		else
			printf("Case #%d: NO\n", i+1);
	}

	// –{•¶I‚í‚è --------------------------------
	time_t end;
	time(&end);
	printf("%ld sec.\n", end - start);
	return 0;
}
