#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>
#include <vector>
using namespace std;

int ans(vector<char>[], int);

string arr[5010];
int L, D, N;
int main()
{
	int t, i;
	freopen("A.in", "r", stdin);
	freopen("A.txt", "w", stdout);
	scanf("%d%d%d", &L, &D, &N);
	string str;
	
	{ 
		for(i = 0; i < D; ++i)
		{
			cin >> arr[i];
		}
		for(i = 0; i < N; ++i)
		{
			cin >> str;
			int cnt = 0;
			int p = 0;
			vector<char> v[20];

			while(p < (int) str.size())
			{
				if(str[p] != '(' && str[p] != ')') 
				{
					v[cnt].push_back(str[p]);
					++p, ++cnt;
					continue;
				}
				if(str[p] == '(')
				{
					++p;
					while(str[p] != ')') 
					{
						v[cnt].push_back(str[p]);
						++p;
					}
					++p;
					++cnt;
				}
				else ++p;
			}
			/*for(p = 0; p < cnt; ++p)
			{
				cout << "v[" << p << "]" << endl;
				for(int k = 0; k < v[p].size(); ++k) cout << v[p][k];
				cout << endl;
			}*/
			int a = ans(v, cnt);
			printf("Case #%d: %d\n", i + 1, a);

		}
	}
	return 0;
}

int ans(vector<char>v[], int len)
{
	int i = 0, ans = 0, pos, j;
	for(i = 0; i < D; ++i)
	{
		bool valid = true;
		for(pos = 0; pos < len; ++pos)
		{
			for(j = 0; j < v[pos].size(); ++j){
				if(arr[i][pos] == v[pos][j]) break;
			}
			if(j == v[pos].size()){
				valid = false;
				break;
			}
		}
		if(valid) ++ans;
		
	}
	return ans;
}