#include<iostream>
#include<stdio.h>
#include<string.h>
#include<string>
using namespace std;
int a[26][26],b[26][26];
int main()           
{
	freopen("B-large.in","r",stdin);
	freopen("B-large.out","w",stdout);
	int t,c,d,n;
	char s[111];
	scanf("%d",&t);
	for(int tt = 0; tt < t; tt++)
	{
		memset(a,-1,sizeof(a));
		memset(b,0,sizeof(b));
		scanf("%d",&c);
		for(int i = 0; i < c; i++)
		{
			scanf("%s",&s);
			a[int(s[0] - 'A')][int(s[1] - 'A')] = int(s[2] - 'A');
			a[int(s[1] - 'A')][int(s[0] - 'A')] = int(s[2] - 'A');
		}
		scanf("%d",&d);
		for(int i = 0; i < d; i++)
		{
			scanf("%s",&s);
			b[int(s[0] - 'A')][int(s[1] - 'A')] = 1;
			b[int(s[1] - 'A')][int(s[0] - 'A')] = 1;
		}
		string res = "";
		scanf("%d%s",&n,&s);
		for(int i = 0; i < n; i++)
		{
			if (res.length() > 0 && a[int(res[res.length() - 1] - 'A')][int(s[i] - 'A')] != -1)
			{
				char f = char(a[int(res[res.length() - 1] - 'A')][int(s[i] - 'A')] + 'A');
				res = res.substr(0,res.length() - 1);
				res = res + f;
				continue;
			}
			int ok = 0;
			for(int j = 0; j < res.length(); j++)
				if (b[int(res[j] - 'A')][int(s[i] - 'A')])
				{
					res = "";
					ok = 1;
					break;
			     }
			if (ok) continue;
			res = res + s[i];
		}
		printf("Case #%d: [",tt + 1);
		for(int i = 0; i < res.length(); i++)
		{
			if (i) printf(", ");
			printf("%c",res[i]);
		}
		printf("]\n");
	}
	return 0;
}
