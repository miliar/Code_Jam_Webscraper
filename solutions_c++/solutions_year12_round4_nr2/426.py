#include <cstdio>
#include <algorithm>
#include <cassert>
#include <utility>
#include <vector>

using namespace std;

#define N 1010

int x[N], y[N], finalx[N], finaly[N];
vector <pair <int, int> > a;
bool placed[N];

int main()
{
	int T;
	freopen("B-large.in", "r", stdin);
	freopen("bout.txt", "w", stdout);
	scanf(" %d", &T);
	for(int z = 0; z < T; z ++)
	{
        a.clear();
		int n, w, l;
		scanf(" %d %d %d", &n, &w, &l);
		for(int i = 0; i < n; i ++)
		{
		    int temp;
            scanf(" %d", &temp), a.push_back(make_pair(temp, i));
            a[i].first = - (a[i].first);
            placed[i] = false;
		}
		//printf("Read input\n");
		sort(a.begin(), a.end());
		for(int i = 0; i < n; i ++)
			a[i].first = -(a[i].first);
		int currx = a[0].first, curry = 0;
		int toplace = 1;
		int MAX = a[0].first;
		x[0] = 0, y[0] = 0;
		placed[0] = true;
		//printf("WTF?\n");
		while(1)
		{
                //printf("Looping\n");
                for(int i = 0; i < n; i ++)
                    if(!placed[i])
                    {
                        if(currx + a[i].first <= w)
                        {
                            x[i] = currx + a[i].first;
                            y[i] = curry;
                            currx += 2 * a[i].first;
                            placed[i] = true;
                        }
                    }
                for(int i = 0; i < n; i ++)
                {
                    if(!placed[i])
                    {
                        x[i] = 0;
                        y[i] = curry + MAX + a[i].first;
                        currx = a[i].first;
                        curry += MAX + a[i].first;
                        placed[i] = true;
                        MAX = a[i].first;
                        break;
                    }
                }
                int counts = 0;
                for(int i = 0; i < n; i ++)
                    counts += !placed[i];
                if(counts == 0)
                    break;
                //printf("Counts: %d\n", counts);
		}
		printf("Case #%d:", z + 1);
		for(int i = 0; i < n; i ++)
		{
		    finalx[a[i].second] = x[i];
		    finaly[a[i].second] = y[i];
		}
		for(int i = 0; i < n; i ++)
            printf(" %d %d", finalx[i], finaly[i]);
		printf("\n");
	}
	return 0;
}
