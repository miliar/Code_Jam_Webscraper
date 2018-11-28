#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <string>
#include <fstream>
using namespace std;
FILE * fp;
FILE * out;


int n;

//char ch[600];

string ch;

int g[600][27][600];
int len[600][27];


inline int get(char c)
{
	if(c == ' ')
		return 26;
	return c - 'a';
}

char pat[] = "welcome to code jam";


int dp[27][600];

int solv(int pos,int k)
{
	if(pos == 18)
	{
		return 1;
	}

	if(dp[pos][k] != -1)
		return dp[pos][k];

	int idx = get(pat[pos + 1]);
	int res = 0;
	for(int i = 0;i < len[k][idx];i ++)
	{
		res += solv(pos + 1,g[k][idx][i]);
		res %= 10000;
	}

	dp[pos][k] = res;
	return res;
}


void pr(int k)
{
	if(k >= 1000)
	{
		fprintf(out,"%d\n",k);
		return ;
	}
	if(k >= 100)
	{
		fprintf(out,"0%d\n",k);
		return ;
	}
	if(k >= 10)
	{
		fprintf(out,"00%d\n",k);
		return ;
	}
	fprintf(out,"000%d\n",k);
}





int main()
{
	fp = fopen("B-large.in","r");
	out = fopen("A-small.out","w");
	scanf("%d",&n);
	int cnt = 1;
	getline(cin,ch);
	ch.clear();
	while(--n >= 0)
	{
	//	scanf("%s",ch);
		getline(cin,ch);
		int l = ch.size();

		memset(len,0,sizeof(len));
		for(int i = 0;i < l;i ++)
		{
			for(int j = i + 1;j < l;j ++)
			{
				int idx = get(ch[j]);
				g[i][idx][len[i][idx] ++] = j;
			}
		}
		memset(dp,-1,sizeof(dp));

		int ans = 0;
		for(int i = 0;i < l;i ++)
		{
			if(ch[i] == 'w')
			{
				ans += solv(0,i);
				ans %= 10000;
			}
		}
		fprintf(out,"Case #%d: ",cnt);
		cnt ++;

		pr(ans);
	}









	


	
	return 0;
}