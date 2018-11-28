#include <iostream>
#include <algorithm>
#include <cstdlib>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <stack>
#include <string>
#include <sstream>
#include <cmath>
#include <bitset>
#include <cctype>
#include <complex>
using namespace std;

#define gcd(a, b)					__gcd(a, b)
#define lcm(a, b)					((a / gcd(a, b)) * b)
#define popcount(a)					__builtin_popcount(a)
#define min(a, b)					((a) < (b) ? (a) : (b))
#define max(a, b)					((a) < (b) ? (b) : (a))

typedef pair<int, int> PII;

const int MAX_C = 1000;
const int INF = 1000000;

int N, C, ans;
map<string, int > m;
vector< PII > v[MAX_C];

void Read()
{
	cin >> N;
	
	C = 0;
	ans = INF;
	for(int i = 0; i < MAX_C; i ++) v[i].clear();
	m.clear();
	
	for(int i = 0; i < N; i ++)
	{
		string s;
		int a, b;
		
		cin >> s >> a >> b;
		
		if(!m[s]) m[s] = ++ C;
		
		v[m[s]].push_back(PII(a, b));
	}
}

bool cmp(PII a, PII b)
{
	if(a.first < b.first) return true;
	
	if(a.first == b.first && a.second < b.second) return true;
	
	return false;
}

bool ok(vector<PII> t)
{
int end = 0;
	
	sort(t.begin(), t.end(), cmp);
	
	for(int i = 0; i < t.size(); i ++)
	{
		if(t[i].first - 1 <= end)
		{
			end = max(end, t[i].second);
		}
	}
		
	return (end == 10000);
}

void Solve()
{
	for(int i = 1; i <= C; i ++)
	{
		for(int mask = 0; mask < 1 << v[i].size(); mask ++)
		{
			vector<PII> t;
			
			for(int j = 0; j < v[i].size(); j ++)
			{
				if(mask & (1 << j))
				{
					t.push_back(v[i][j]);
				}
			}
			
			if(ok(t)) ans = min(ans, popcount(mask));
		}
	}
	
	for(int i = 1; i <= C; i ++)
	{
		for(int j = i; j <= C; j ++)
		{
			for(int k = j; k <= C; k ++)
			{
				vector<PII> t;
				
				for(int l = 0; l < v[i].size(); l ++)
				{
					t.push_back(v[i][l]);
				}
				
				if(j != i)
				{
					for(int l = 0; l < v[j].size(); l ++)
					{
						t.push_back(v[j][l]);
					}
				}
				
				if(k != j)
				{
					for(int l = 0; l < v[k].size(); l ++)
					{
						t.push_back(v[k][l]);
					}
				}
				
				for(int mask = 0; mask < 1 << t.size(); mask ++)
				{
					vector<PII> q;
					
					for(int l = 0; l < t.size(); l ++)
					{
						if(mask & (1 << l))
						{
							q.push_back(t[l]);
						}
					}
					
					if(ok(q))
					{
						ans = min(ans, q.size());
					}
				}
			}
		}
	}
}

void Write(const int test_case)
{
	printf("Case #%d: ", test_case);
	
	if(ans == INF) printf("IMPOSSIBLE\n");
	else printf("%d\n", ans);
}

int main()
{
int TESTS;
	
	cin >> TESTS;
	
	for(int test_case = 1; test_case <= TESTS; test_case ++)
	{
		Read();
		
		Solve();
		
		Write(test_case);
	}
	
//	system("pause");
	
	return 0;    
}
