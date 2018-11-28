
#define _CRT_SECURE_NO_DEPRECATE 

#include <string> 
#include <vector> 
#include <map> 
#include <list> 
#include <set> 
#include <queue> 
#include <iostream> 
#include <sstream> 
#include <stack> 
#include <deque> 
#include <cmath> 
#include <memory.h> 
#include <cstdlib> 
#include <cstdio> 
#include <cctype> 
#include <algorithm> 
#include <utility> 

using namespace std; 

#define FOR(i, a, b) for(int i = a; i < b; ++i)
#define RFOR(i, b, a) for(int i = b - 1; i >= a; --i)
#define REP(i, N) FOR(i, 0, N)
#define RREP(i, N) RFOR(i, N, 0)

#define MIN(A, B) ((A) < (B) ? (A) : (B))
#define MAX(A, B) ((A) > (B) ? (A) : (B))
#define ABS(A) ((A) < 0 ? (-(A)) : (A))
#define ALL(V) V.begin(), V.end()
#define SIZE(V) (int)V.size()
#define pb push_back
#define mp make_pair
#define EPS 1e-7
#define Pi 3.14159265358979

typedef long long Long;
typedef unsigned long long ULong;
typedef unsigned int Uint;
typedef unsigned char Uchar;
typedef vector <int> VI;
typedef pair <int, int> PI;

struct node
{
	string item;
	vector<node*> v;
};

int add(node* root, vector<string>& dirs)
{
	if(dirs.empty())
		return 0;
	REP(i, (int)root->v.size())
	{
		if(dirs.back() == root->v[i]->item)
		{
			dirs.pop_back();
			return add(root->v[i], dirs);
		}
	}
	root->v.pb(new node());
	root->v.back()->item = dirs.back();
	dirs.pop_back();
	return 1 + add(root->v.back(), dirs);
}

int tests;

int n, m;

node *root;

int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	scanf("%d", &tests);
	REP(I, tests)
	{
		scanf("%d%d", &n, &m);
		root = new node();
		string path;
		REP(i, n)
		{
			cin >> path;
			REP(j, (int)path.length())
				if(path[j] == '/')
					path[j] = ' ';
			istringstream iss(path);
			vector<string> v;
			string dir;
			while(iss >> dir)
				v.pb(dir);
			reverse(ALL(v));
			add(root, v);
		}
		int res = 0;
		REP(i, m)
		{
			cin >> path;
			REP(j, path.length())
				if(path[j] == '/')
					path[j] = ' ';
			istringstream iss(path);
			vector<string> v;
			string dir;
			while(iss >> dir)
				v.pb(dir);
			reverse(ALL(v));
			res += add(root, v);
		}
		printf("Case #%d: %d\n", I + 1, res);
	}
	return 0;
}