#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
using namespace std;
const int MAXN = 101;

vector<string> dir[MAXN];
string str1, str2;
int T, N, M, ans;
int i, j, k, l, c;
int main()
{
	vector<string>::iterator res;
	cin>>T;
	for (c = 1; c <= T; c++)
		{
		for (i = 0; i < MAXN; i++)
			{
			dir[i].clear();
			}
		ans = 0;
		cin>>N>>M;
		while (N--)
			{
			cin>>str1;
			i = 0;
			l = str1.length();
			j = 0;
			str2 = "";
			while (str1[i++] == '/' && i < l)
				{					
				str2 += str2;
				while (str1[i] != '/' && i < l)
					{
					str2 += str1[i++]; 
					}
				dir[j++].push_back(str2);
				}
			}
		while (M--)
			{
			cin>>str1;
			i = 0;
			l = str1.length();
			j = 0;
			str2 = "";
			while (str1[i++] == '/' && i < l)
				{
				str2 += str2;
				while (str1[i] != '/' && i < l)
					{
					str2 += str1[i++];
					}
				res = find(dir[j].begin(), dir[j].end(), str2);
				if (res == dir[j].end())
					{
					ans++;
					dir[j].push_back(str2);
					}
				j++;
				}
			}
		cout<<"Case #"<<c<<": "<<ans<<endl;
		}
}
