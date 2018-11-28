#include <iostream>
#include <string>
#include <vector>
#include <map>
using namespace std;
string exist[111];
string deal[111];
char str[100001];
map<string, int>hash;
int main()
{
	int t, i, j, k, n, m, temp,cas = 0;
//	freopen("A-small.in","r", stdin);
	freopen("A-large.in","r", stdin);
	freopen("A.out", "w", stdout);
	scanf("%d", &t);
	int count = 0 ;
	while(t--)
	{
		count = 0;
		scanf("%d %d", &n, &m);
		hash.clear();
		for(i = 0; i < n; i ++)
		{
			scanf("%s", str);
			exist[i] = "";
			for(j = 0; str[j] != '\0'; j ++)
			{
				exist[i] += str[j];
			}
		}
		string s  = "";
		for(i = 0; i < n; i ++)
		{
			s = "";
			s += exist[i][0];
			for(j = 1; j < exist[i].length(); j ++)
			{
				if(exist[i][j] == '/')
				{
					hash[s] = 1;
				}
				s += exist[i][j];
			}
			hash[s] = 1;
		}
		for(i = 0; i < m; i ++)
		{
			scanf("%s", str);
			deal[i]  = "";
			for(j = 0; str[j] != '\0'; j ++)
			{
				deal[i] += str[j];
			}
		}
		for(i = 0; i < m ; i ++)
		{
			s = "";
			s += deal[i][0];
			for(j = 1; j < deal[i].length(); j ++)
			{
				if(deal[i][j] == '/')
				{
					if(hash.find(s) == hash.end())
					{
						hash[s] = 1;
						count ++;
					}	
				}
				s += deal[i][j];
			}
			if(hash.find(s) == hash.end())
			{
				hash[s] = 1;
				count ++;
			}
		}
		printf("Case #%d: %d\n", ++cas, count);
	}
}