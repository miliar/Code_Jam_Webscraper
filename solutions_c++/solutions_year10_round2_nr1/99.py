#if 1
#include <iostream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <stack>
#include <cstdlib>
#include <cassert>
#include <cstring>
#include <functional>
#include <algorithm>
#include <cmath>
#include <bitset>
#include <cstdio>
using namespace std;

typedef long long LL;
typedef long double LD;
const LD eps = 1e-9;

typedef pair<int, int> pii;
#define mp make_pair
#define pb push_back
#define X first
#define Y second
#define iss istringstream
#define oss ostringstream
#define dbg(x) cerr << #x << " = " << x << endl;



int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for(int z = 0; z < t; ++z)
	{
		int n, m; scanf("%d%d", &n, &m);
		set<string> ex;
		ex.insert("");
		for(int i = 0; i < n; ++i)
		{
			string s;
			cin >> s;
			while(s.length())
			{
				ex.insert(s);
				s.erase(s.find_last_of('/'));
				//dbg(s);
			}
		}

		int cnt = 0;
		for(int i = 0; i < m; ++i)
		{
			string s;
			cin >> s;
			while(!ex.count(s))
			{
				cnt++;
				ex.insert(s);
				s.erase(s.find_last_of('/'));
				//dbg(s);
			}
			
		}

		printf("Case #%d: %d\n", z + 1, cnt);
	
	}
	return 0;
}
#endif