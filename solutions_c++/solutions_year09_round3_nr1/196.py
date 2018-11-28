#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;
int T;
map <char ,int> all;
int main()
{
	freopen("..\\A-large.in","r",stdin);
	freopen("..\\A33.out","w",stdout);
	cin>>T;
	char s[100];
	bool check[40];
	for(int i = 1;i <= T;i++)
	{
		cin>>s;
		int n = strlen(s);
		memset(check,false,sizeof(check));
		all.clear();
		int count = 0;
		for(int j = 0;j < n;j++)
		{
			int qq;
			if(s[j] >= 'a' && s[j] <= 'z') qq = s[j] - 'a' + 10;
			else qq = s[j] - '0';
			if(!check[qq]) {count++;check[qq] = true;}
		}
		if(count == 1) count = 2;
		all[s[0]] = 2;
		int pp = 1;
		for(int j = 1;j < n;j++)
		{
			if(all[s[j]] == 0)
			{
				if(pp == 2) pp++;
				all[s[j]] = pp++;
			}
		}
		long long res = (long long)(all[s[n - 1]] - 1);
		long long cc = (long long)count;
		for(int j = n - 2;j >= 0;j--)
		{
			res += (long long)(all[s[j]] - 1) * cc;
			cc *= (long long)count;
		}
		printf("Case #%d: %lld\n",i,res);
	}
	return 0;
}