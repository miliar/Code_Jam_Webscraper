#define _CRT_SECURE_NO_DEPRECATE
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <string>
#include <cstring>
#include <cstdio>
#include <set>
#include <cmath>
#include <queue>
#include <sstream>
#include <iostream>
using namespace std;

//////////////////// Defines ////////////////////

#pragma comment(linker, "/STACK:67108864")

#define inf      2147483647
#define inf64    9223372036854775807
#define eps      1e-6
#define pi      3.14159265358
#define sqr(a) (a)*(a)
#define rall(a) a.rbegin(),a.rend()
#define all(a) a.begin(),a.end()
#define sz(a) (a).size()
#define mset(a,v) memset(a, v, sizeof(a))
#define pb push_back 
typedef long long ll;
typedef vector<int> VI;
typedef vector<double> VD;
typedef vector<string> VS;

#define ContinueIf(x) if ((x)) continue
#define ContinueUnless(x) if(!(x)) continue

#define BreakIf(x) if ((x)) break
#define BreakUnless(x) if(!(x)) break

#define ReturnUnless(x) if (!(x)) return
#define ReturnIf(x) if ((x)) return

#define ReturnUnless2(x, ret) if (!(x)) return ret
#define ReturnIf2(x, ret) if ((x)) return ret

//////////////////// Problem Code ////////////////////

struct Directory
{
	string name;
	Directory(){};
	Directory(string _name) : name(_name) {}
	set<Directory> entries;

	bool operator < (const Directory& d) const
	{
		return name < d.name;
	}

	int add(string path)
	{
		if(name == path)
		{
			return 0;
		}
		if (!name.empty())
		{
			path = path.substr(name.size() + 1);
		}
		
		string curr;
		int pos = 0;
		while (pos < path.size() && path[pos] != '/')
		{
			curr.push_back(path[pos]);
			++pos;
		}
		int ret = 0;
		if (entries.find(curr) == entries.end())
		{
			++ret;
			entries.insert(Directory(curr));
		}
		return ret + entries.find(Directory(curr))->add(path);
	}
};

int main()
{
	int k, T;
	freopen("input.txt", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	scanf("%d", &T);
	for(k = 1 ; k <= T ; ++k)
	{
		int N, M;
		scanf("%d%d\n", &N, &M);

		Directory root;
		for (int i = 0 ; i < N ; ++i)
		{
			char buff[128];
			scanf("%s", buff);
			root.add(string(buff).substr(1));
		}

		int ans = 0;
		for (int i = 0 ; i < M ; ++i)
		{
			char buff[128];
			scanf("%s", buff);
			ans += root.add(string(buff).substr(1));
		}
		printf("Case #%d: %d\n", k, ans);
	}
	return 0;
}

