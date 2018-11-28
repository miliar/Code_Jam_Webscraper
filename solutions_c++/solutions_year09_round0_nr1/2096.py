#include <cstdio>
#include <string>

using namespace std;

string pattern[15];
char word[5000][16];
int l,d,n;
char temp[10000];

void input()
{
	for(int i = 0;i < 15;++i)
		pattern[i].clear();
	scanf("%s",temp);
	char *p = temp;
	int now = 0;
	bool flag = 0;
	while(*p)
	{
		if(*p == '(')
		{
			flag = 1;
			p++;
		}
		else if(*p == ')')
		{
			flag = 0;
			p++;
			now++;
		}
		else
		{
			pattern[now] += *p;
			if(!flag)
				++now;
			p++;
		}
	}
}

bool check(int j)
{
	int k;
	for(int i = 0;i < l;++i)
	{
		for(k = 0;k < pattern[i].length();++k)
			if(pattern[i][k] == word[j][i])
				break;
		if(k == pattern[i].length())
			return false;
	}
	return true;
}

int main()
{
	freopen("1test.out","w",stdout);
	int ans;
	scanf("%d%d%d",&l,&d,&n);
	for(int i = 0;i < d;++i)
		scanf("%s",word[i]);
	for(int i = 1;i <= n;++i)
	{
		ans = 0;
		input();
		for(int j = 0;j < d;++j)
			if(check(j))
				++ans;
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}