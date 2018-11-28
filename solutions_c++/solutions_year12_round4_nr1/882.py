#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;
int n;
int D;
vector<int> p;
vector<int> l;

bool bt(int x, int y = 0)
{
	//cout << x << ' ' << y << endl;
	if (p[x] <= y)
		return false;
	if (p[x] + p[x]-y >= D)
		return true;
	int it = upper_bound(p.begin(), p.end(), p[x]+p[x]-y) - p.begin();
	//cout << '#' << it <<endl;
	it --;
	while(it > x)
	{
		if (bt(it, max(p[it]-l[it], p[x]) ))
			return true;
		it --;
	}
	return false;
}

int main()
{
	cin.sync_with_stdio(false);
	int tn;
	int pn;
	cin >> tn;
	while(tn--)
	{
		pn ++;
		cout << "Case #" << pn << ": ";
		p.clear();
		l.clear();
		cin >> n;
		for(int i = 0; i < n; i ++)
		{
			int t;
			cin >> t;
			p.push_back(t);
			cin >> t;
			l.push_back(t);
		}
		cin >> D;
		bool ret = bt(0);
		if (ret)
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}

	return 0;
}
