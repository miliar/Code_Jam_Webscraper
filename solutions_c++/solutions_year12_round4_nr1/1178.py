#include <string>
#include <map>
#include <deque>
#include <queue>
#include <stack>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cmath>
#include <algorithm>
#include <vector>
#include <set>
#include <list>

using namespace std;

bool solve(vector<int> &d, vector<int> &l, vector<int> &m, int k, int &L)
{
	//if (m[k] == -1)
	//{
	//	cout << "MUERTE" << endl;
	//	return false;
	//}
	//cout << "L= " << L << endl;
	//cout << "m+l= " << m[k]+d[k] << endl;
	if (m[k]+d[k] >= L) return true;
	for (int i = k+1 ; i < d.size() ; i ++)
	{
		if (m[k]+d[k] >= d[i])
		{
			//cout << "i= " << i << endl;
			if (m[i] == -1 || m[i] < min(d[i]-d[k], l[i]))
			{
				m[i] = min(d[i]-d[k], l[i]);
				if (solve(d, l, m, i, L))
					return true;
			}
		}
	}
	return false;
}

int main()
{
	ios_base::sync_with_stdio(false);
	int T;
	int N, L;
	cin >> T;
	for (int i = 0 ; i < T ; i ++)
	{
		cin >> N;
		vector<int> d(N);
		vector<int> l(N);
		vector<int> m(N, -1);
		for (int j = 0 ; j < N ; j ++)
		{
			cin >> d[j] >> l[j];
		}
		m[0] = d[0];
		cin >> L;
		cout << "Case #" << i+1 << ": " << (solve(d, l, m, 0, L)?"YES":"NO") << endl;
	}

	return 0;
}
