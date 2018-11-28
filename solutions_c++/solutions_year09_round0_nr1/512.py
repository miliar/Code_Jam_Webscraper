#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cstdlib>
using namespace std;

int l,d,n;
char ch[5003][20];

bool flag[20][30];

char pat[400];

inline bool check(int k)
{
	for(int i = 0;i < l;i ++)
	{
		if(flag[i][ch[k][i] - 'a'] == false)
			return false;
	}
	return true;
}

FILE * fp;
FILE * out;

int main()
{
	fp = fopen("A-large.in","r");
	out = fopen("A-large.out","w");


	fscanf(fp,"%d%d%d",&l,&d,&n);
	for(int i = 0;i < d;i ++)
		fscanf(fp,"%s",ch[i]);


	for(int i = 0;i < n;i ++)
	{
		
		int ans = 0;
		memset(flag,false,sizeof(flag));
		fscanf(fp,"%s",pat);
		int pos = 0;
		int len = strlen(pat);
		int k = 0;
		while(k < len)
		{
			if(pat[k] == '(')
			{
				k ++;
				while(pat[k] != ')')
				{
					flag[pos][pat[k] - 'a'] = true;
					k ++;
				}
				pos ++;
				k ++;
				continue;
			}
			flag[pos][pat[k] - 'a'] = true;
			k ++;
			pos ++;
		}
		for(int j = 0;j < d;j ++)
		{
			if(check(j))
				ans ++;
		}
		fprintf(out,"Case #%d: ",i + 1); 
		fprintf(out,"%d\n",ans);
	}
	
	return 0;
}