// cheburashka, bear-mouse, team template

#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <sstream>
#include <stack>
#include <cstring>
#include <cmath>
#include <queue>
#include <set>
using namespace std;

typedef long long ll;
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl;

#define pb(x) push_back(x)

#define mp(x, y) make_pair(x, y)

//string split given string a and delimiters
int D,I,N,M;
const int MAXN = 105;
int pix[MAXN];
int memo[256][MAXN];

int rec(int val, int p)
{
	int & ret = memo[val][p];
	if(ret != -1) return ret;
	if(p == N) return ret = 0;
	
	ret = D + rec(val,p+1);
	if(abs(val-pix[p]) <= M)
	{
		int neu = rec(pix[p],p+1);
		ret = min(ret,neu);
	}
	for(int i = 0; i <= 255; i++)
	{
		if(abs(val-i) <= M)
		{
			int neu = abs(i-pix[p]) + rec(i,p+1);
			ret = min(ret,neu);
		}
	}
	for(int i = 1; i <= M; i++)
	{
		if(val > pix[p]+M)
		{
			int neu = I + rec(val-i,p);
			ret = min(ret,neu);
		}
		if(val < pix[p]-M)
		{
			int neu = I + rec(val+i,p);
			ret = min(ret,neu);
		}
	}
	return ret;
}

int main()
{
	int T;
	cin >> T;
	for(int tcase = 1; tcase <= T; tcase++)
	{
		cin >> D >> I >> M >> N;
		for(int i = 0; i < N; i++) cin >> pix[i];
		memset(memo,-1,sizeof(memo));
		int ret = D*N,neu =0;
		for(int j = 0; j < N; j++)
		{
			neu = D*j + rec(pix[j],j+1);
			ret = min(neu,ret);
			for(int i = 0; i <= 255; i++)
			{
				neu = D*j + abs(i-pix[j]) + rec(i,j+1);
				ret = min(ret,neu);
				neu = D*j + I + rec(i,j);
			}
		}
		printf("Case #%d: %d\n",tcase,ret);
				
		
		
	}
	return 0;
}
