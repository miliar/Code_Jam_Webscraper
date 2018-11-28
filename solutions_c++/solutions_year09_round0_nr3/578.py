#define  _CRT_SECURE_NO_DEPRECATE
#include<iostream>
#include<string>
#include<sstream>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<time.h>
#include<numeric>
#include<set>
#include<stack>
#include<deque>
#include<math.h>
#define epsilon 0.000000001
using namespace std;
//
int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int numtests;
	cin >> numtests;
	vector<vector<int> > r(256);
	string str = "welcome to code jam";
	r['w'].push_back(0);
	for(int i = 1; i < str.size(); i++)
		r[str[i]].push_back(i);
	getline(cin, str);
	for(int o = 0; o < numtests; o++)
	{
		printf("Case #%d: ", o + 1);
		string str;
		getline(cin, str);
		vector<int> p(20, 0);
		p[0] = 1;
		for(int i = 0; i < str.size(); i++)
		{
			vector<int> newp(p);
			for(int k = 0; k < r[str[i]].size(); k++)
			{
				newp[r[str[i]][k] + 1] = (p[r[str[i]][k]] + newp[r[str[i]][k] + 1]) % 10000;
			}
			p = newp;
		}
		printf("%04d\n", p[19]);
	}
	return 0;
}
