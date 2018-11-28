#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <math.h>
#include <ctype.h>
#include <queue>
using namespace std;

int ans;
int cnt;
struct Node
{
	map <string, int> dirs;
	void Add(vector <string> &a, bool cost, int now = 0);

	void Clear()
	{
		dirs.clear();
	}
};

vector <Node> arr;


void Node::Add(vector <string> &a, bool cost, int now )
{
	if (a.size() == now)
		return;
	if (dirs.find(a[now]) == dirs.end())
	{
		if (cost)
			ans ++;
		dirs[a[now]] = cnt ++;
	}
	arr[dirs[a[now]]].Add(a, cost, now+1);
}

vector <string> Convert(string s)
{
	int i = 1;
	vector <string> a;
	string t;
	while (i <= s.length())
	{
		if (i == s.length() || s[i] == '/')
		{
			a.push_back(t);
			t = "";
		}
		else
			t += s[i];
		i ++;
	}
	return a;
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("out.txt", "w", stdout);
	int t ;
	cin >> t;

		arr.resize(100000);
	for (int test = 0; test < t ; test ++)
	{
		ans = 0;
		cnt = 1;
		for (int i =0; i < arr.size(); i ++)
			arr[i].Clear();
		int n,m;
		cin >> n >> m;
		for (int i = 0; i < n; i ++)
		{
			string s;
			cin >> s;
			arr[0].Add(Convert(s),false);
		}
		for (int i = 0; i < m; i ++)
		{
			string s;
			cin >> s;
			arr[0].Add(Convert(s),true);
		}
		cout << "Case #" << test+1 << ": " << ans << endl;
	}
	return 0;
}
