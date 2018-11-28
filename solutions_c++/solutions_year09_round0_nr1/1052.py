/*#include<iostream>
#include<cstring>
#include<string>
#include<algorithm>
using namespace std;

char keyword[5005][20];     //输入的单词
char in[1000001];    //模式串
string s[20];

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin);
	//freopen("A-small-attempt0.out", "w", stdout);
	int l, d, n, i, j, k, t;
	while(3 == scanf("%d %d %d", &l, &d, &n))
	{
		for(i=0; i<d; i++)
			scanf("%s", keyword[i]);
		for(i=0; i<n; i++)
		{
			scanf("%s", in);
			int num = -1;
			for(j=0; in[j]!='\0'; j++)
			{
				if(in[j] >= 'a' && in[j] <= 'z')
				{
					if(num == -1)
						num ++;
					s[num] = s[num] + in[j];
				}
				else if(in[j] == '(')
				{
					if(s[num].empty() && num >= 0)
						continue;
					num ++;
					s[num].clear();
				}
				else if(in[j] == ')')
				{
					if(s[num].empty() && num >= 0)
						continue;
					num ++;
					s[num].clear();
				}
			}
			if(!s[num].empty())
			{
				num ++;
			}
			if(num == 1 && l != 1)
			{
				for(j=0; in[j]!='\0'; j++)
				{
					s[j].clear();
					s[j] = s[j] + in[j];
				}
			}
			int ans = 0;
			for(j=0; j<d; j++)
			{
				for(k=0; k<l; k++)
				{
					for(t=0; t<s[k].size(); t++)
					{
						if(keyword[j][k] == s[k][t])
							break;
					}
					if(t == s[k].size())
						break;
				}
				if(k == l)
					ans ++;
			}
			printf("Case #%d: %d\n", i + 1, ans);
		}
	}
	return 0;
}*/
#include<iostream>
#include<cstring>
#include<set>
#include<algorithm>
using namespace std;

char keyword[5005][20];
set<char> se[505][20];
char in[1000005];

int main()
{
	//freopen("A-large.in", "r", stdin);
	//freopen("A-large.out", "w", stdout);
	int l, d, n, i, j, k;
	scanf("%d %d %d", &l, &d, &n);
	for(i=0; i<d; i++)
		scanf("%s", keyword[i]);
	for(i=0; i<n; i++)
	{
		scanf("%s", in);
		int num = -1;
		bool leap = false;
		for(j=0; in[j]!='\0'; j++)
		{
			if(in[j] == '(')
			{
				num ++;
				se[i][num].clear();
				leap = true;
			}
			else if(in[j] == ')')
			{
				leap = false;
			}
			else 
			{
				if(!leap)
				{
					num ++;
					se[i][num].clear();
				}
				se[i][num].insert(in[j]);
			}
		}
	}
	for(i=0; i<n; i++)
	{
		int ans = 0;
		for(j=0; j<d; j++)
		{
			for(k=0; k<l; k++)
			{
				if(se[i][k].find(keyword[j][k]) == se[i][k].end())
					break;
			}
			if(k == l)
				ans ++;
		}
		printf("Case #%d: %d\n", i + 1, ans);
	}
	return 0;
}
