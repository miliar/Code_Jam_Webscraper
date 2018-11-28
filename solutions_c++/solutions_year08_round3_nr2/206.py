#include<stdio.h>
#include<string.h>
#include<algorithm>
#include<vector>
using namespace std;
vector<__int64>a[40];
int main()
{
	freopen("B-small.in","r",stdin);
	freopen("B-small.out","w",stdout);
	//freopen("A-large.in","r",stdin);
	//freopen("A-large.out","w",stdout);
	char s[40];
	int T,c,i,j,k;
	scanf("%d",&T);
	for(c=1;c<=T;c++)
	{
		scanf("%s",s);
		for(i=0;i<40;i++)
			a[i].clear();
		a[0].push_back(s[0]-'0');
		int len = strlen(s);
		for(i=1;i<len;i++)
		{
			for(k=0;k<i;k++)
			{
				__int64 val=0,ss=1;
				for(j=k+1;j<=i;j++)
					val = val*10 + s[j]-'0',ss*=10;
				for(j=0;j<a[k].size();j++)
				{
					a[i].push_back(a[k][j] + val);
					a[i].push_back(a[k][j] - val);
				}
			}
			__int64 val=0;
			for(j=0;j<=i;j++) val = val*10 + s[j]-'0';
			a[i].push_back(val);
		}
		int sum=0;
		for(j=0;j<a[len-1].size();j++)
		{
			if(a[len-1][j]%2 == 0 || a[len-1][j]%3==0 || a[len-1][j]%5==0 || a[len-1][j]%7==0)
				sum++;
		}
		printf("Case #%d: %d\n",c,sum);
	}
	return 0;
}
/*
4
1
9
011
12345
*/