#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

#define MST(a,b) (memset(a,b,sizeof(a)))
#define DB(x) (cout<<#x<<": "<<x<<endl)
#define PB push_back
#define MP make_pair
#define REP(i,n) for(i=0;i<(n);++i)
#define FOR(i,l,h) for(i=(l);i<=(h);++i)
#define FORD(i,h,l) for(i=(h);i>=(l);--i)
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<double> VD;
typedef long long LL;
typedef pair<int,int> PII;


char str[64];
int t, n;
vector<string> v;

int main()
{
	freopen("A_L.in","r", stdin);
	freopen("A_L.out", "w", stdout);

	scanf("%d", &t);
	int i, j, k;
     string S;
     
	for(int Case = 1; Case <= t; Case++)
	{
		scanf("%d", &n);
		v.clear();
		for(i = 0; i < n; i++)
		{
			scanf("%s", &str);
			v.push_back(string(str));
		}
		int ret = 0;
		for(i = 0; i < n; i++)
		{
			for(j = i; j < n; j++)
			{
				for(k = i + 1; k < n; k++)
				{
					if(v[j][k] == '1')
					{
						break;
					}
				}
				if(k >= n)
					break;
			}
			S = v[j];
			for(; j > i; j--)
				v[j] = v[j - 1], ++ret;
			v[i] = S;
		}

		printf("Case #%d: %d\n", Case, ret);
	}


	return 0;
}
