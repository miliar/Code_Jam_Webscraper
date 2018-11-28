#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
using namespace std;

vector<string> s;
vector<string> q;
set<string> ss;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int tt; scanf("%d\n", &tt);
	for(int t = 1; t <= tt; ++t)
	{
		int n; scanf("%d\n", &n);
		s.resize(n);
		for(int i = 0; i < n; ++i)
			getline(cin, s[i]);
		int m;	scanf("%d\n", &m);
		q.resize(m);
		for(int i = 0; i < m; ++i)
			getline(cin, q[i]);
		int cnt = 0;
		int i = 0;
		int sw = 0;
		while(i < m)
		{
			ss.clear();
			cnt = 0;
			while(i < m && cnt < n)
				if(ss.find(q[i]) != ss.end())
					i++;
				else
					ss.insert(q[i]), cnt++, i++;
			if(cnt == n) i--;
			sw++;
		}
		cout << "Case #" << t << ": " << max(0,sw - 1) << endl;
	}
	return 0;
}