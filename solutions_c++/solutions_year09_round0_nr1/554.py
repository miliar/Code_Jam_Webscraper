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

int main()
{
	freopen("google.in", "r", stdin);
	freopen("google.out", "w", stdout);
	int l, d, n;
	cin >> l >> d >> n;
	vector<string> v(d);
	for(int i = 0; i < d; i++)
		cin >> v[i];
	for(int o = 0; o < n; o++)
	{
		printf("Case #%d: ", o + 1);
		string str;
		cin >> str;
		bool mat[26];
		vector<bool> can(d, true);
		int idx = 0;
		for(int i = 0; i < l; i++)
		{
			memset(mat, false, sizeof(mat));
			if(islower(str[idx]))
			{
				mat[str[idx++] - 'a'] = true;
			}
			else
			{
				while(str[idx++] != ')')
				{
					if(islower(str[idx]))
						mat[str[idx] - 'a'] = true;
				}
			}
			for(int j = 0; j < d; j++)
			{
				if(!mat[v[j][i] - 'a'])
					can[j] = false;
			}
		}
		int cnt = 0;
		for(int i = 0; i < d; i++)
			if(can[i])
				cnt++;
		cout << cnt << endl;
	}
	return 0;
}
