#include<iostream>
#include<algorithm>
#include<set>
#include<map>
#include<vector>
#include<string>
#include<queue>
#include<deque>
using namespace std;

const int inf = 1000000000;

int p, q, t[20];
bool done[200];
int best, wyn;

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("C-small-attempt0.out", "w", stdout);
	int tests;
	cin >> tests;
	for(int c = 0; c < tests; c++)
	{
		cin >> p >> q;
		for(int i = 0; i < q; i++)
			cin >> t[i];
		best = inf;
		do{
			wyn = 0;
			for(int i = 0; i < q; i++)
			{
				done[t[i]] = 1;
				int wl = t[i]-1;
				int wp = t[i] + 1;
				while(wl > 0 && !done[wl])
				{
					wyn++;
					wl--;
				}
				while(wp <= p && !done[wp])
				{
					wyn++;
					wp++;
				}
			}
			if(wyn < best)
				best = wyn;
			for(int i = 0; i < 200; i++)
				done[i] = 0;
		}while(next_permutation(t,t+q));
		cout << "Case #" << c+1 <<": " << best << "\n";		
	}
	return 0;
}