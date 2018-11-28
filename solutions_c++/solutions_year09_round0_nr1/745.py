#include<iostream>
#include<string>
#include<vector>
#include<map>
#include<queue>
#include<deque>
#include<set>
#include<stack>
#include<sstream>
#include<fstream>
#include<algorithm>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<cassert>
#include<cstring>
#define CLRM(x) memset(x,-1,sizeof(x))
#define CLR(x) memset(x,0,sizeof(x))
#define ALL(x) x.begin(),x.end()
#define PB push_back
#define MP make_pair
#define VI vector<int> 
#define VVI vector<vector<int> >
#define PII pair<int,int>
#define SZ(x) (int)x.size()
#define LL long long
#define MIN(a,b) (a)<(b)?(a):(b)
#define MAX(a,b) (a)>(b)?(a):(b)
#define LMAX 1000000000000000000LL
#define IMAX 100000000
using namespace std;

int l, d, n;
int vis[510][16][27];
vector<string> words;
vector<string> tofind;
int cnt[510];
void solve()
{
	int i, j, k;
	CLR(vis);
	CLR(cnt);
	for(i = 0; i < n; i++)
	{
		int pos = 0;
		int sz = tofind[i].size();
		int flag = 0;
		for(j = 0; j < sz; j++)
		{
			if(tofind[i][j] == '(')
			{
				flag = 1;
			}
			else if(tofind[i][j] == ')')
			{
				flag = 0;
				pos++;
			}
			else
			{
				vis[i][pos][tofind[i][j] - 'a'] = 1;
				if(flag == 0)
				{
					pos++;
				}
			}
		}	
	}
	for(i = 0; i < n; i++)
	{
		for(j = 0; j < d; j++)
		{
			for(k = 0; k < l; k++)
			{
				if(vis[i][k][words[j][k] - 'a'] != 1)
					break;
			}
			if(k == l)
			{
				cnt[i]++;
			}
		}
	}
	for(i = 0; i < n; i++)
	{
		printf("Case #%d: %d\n", i + 1, cnt[i]);
	}
}
				
int main()
{
	
	int i, j, k;
	cin >> l >> d >> n;
	string s;
	for(i = 0; i < d; i++)
	{
		cin >> s;
		words.PB(s);
	}
	for(i = 0; i < n; i++)
	{
		cin >> s;
		tofind.PB(s);
	}
	solve();
	return 0;
}
	
