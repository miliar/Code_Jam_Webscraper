#include <iostream>
#include <vector>
#include <string>
#include <set>
#include <stack>
#include <queue>
#include <deque>
#include <algorithm>
#include <cmath>
#include <map>
#include <cstdio>

using namespace std;

void init()
{
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
}

struct vine
{
	int d;
	int l;
	int niz;
};


int main()
{
	init();
	int T;
	cin >> T;
	for (int t = 0; t < T; ++t)
	{
		int N;
		cin >> N;
		vector <vine> vines(N);
		for (int i = 0; i < N; ++i)
		{
			cin >> vines[i].d >> vines[i].l;
			vines[i].niz = 0;
		}
		int D;
		cin >> D;
		vines[0].niz = vines[0].d;
		bool yes = false;
		for (int  i = 0; i < N; ++i)
		{
			if ((vines[i].niz + vines[i].d) >= D)
			{
				yes = true;
			}
			for (int j = i + 1; j < N; ++j)
			{
				if ((vines[i].niz + vines[i].d >= vines[j].d))
				{
					int l = min(vines[j].d - vines[i].d, vines[j].l); 
					vines[j].niz = max(vines[j].niz, l);
				}
			}			
		}
		cout << "Case #" << t + 1 << ": ";
		if (!yes)
		{
			cout << "NO";
		}
		else
		{
			cout << "YES";
		}
		cout << endl;
		
			
		
		
	}
	return 0;
}
