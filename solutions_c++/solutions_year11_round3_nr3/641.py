#include <iostream>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <fstream>
#include <algorithm>
#include <memory.h>

using namespace std;

vector<int> vi;

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("cSout.txt", "w", stdout);
	int cas;
	cin >> cas;
	for(int ca=1; ca<=cas; ca++)
	{
		vi.clear();
		int l, h, n;
		int i;
		cin >> n >> l >> h;
		for(i=0;i<n; i++)
		{
			int t;
			cin >> t;
			vi.push_back(t);
		}
		cout << "Case #" << ca << ": ";

		for(i=l; i<=h; i++)
		{
			int j;
			for(j=0; j<vi.size(); j++)
				if(!(vi[j] >= i && vi[j] % i == 0 || vi[j] < i && i % vi[j]  ==0))
					break;
			if(j != vi.size())
				continue;
			else
			{
				cout << i << endl;
				break;
			}
		}
		if(i > h)
			cout << "NO" << endl;
	}
	return 0;
}
