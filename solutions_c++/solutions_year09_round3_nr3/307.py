#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAX_P = 104;

vector<int> a;
bool mark[MAX_P];

int main()
{
	int n;
	cin >> n;
	for (int run = 1; run <= n; ++run)
	{
		int p, q;
		cin >> p >> q;
		
		a.clear();
		a.assign(q, 0);
		
		for (int i = 0; i < q; ++i)
			cin >> a[i];
			
		int res = 1000000000;
		
		do 
		{
			int d = 0;
			memset(mark, true, sizeof(mark));
			for (int i = 0; i < q; ++i)
			{
				int k = a[i] - 1;
				mark[k] = false;
				for (int j = k - 1; j >= 0; --j)
					if (mark[j]) ++d;
					else break;
				for (int j = k + 1; j < p; ++j)
					if (mark[j]) ++d;
					else break;
			}
			res = min(res, d);
		} 
		while (next_permutation (a.begin(), a.end()));

		cout << "Case #" << run << ": " << res << endl;
	}
		
	
	return 0;
}
