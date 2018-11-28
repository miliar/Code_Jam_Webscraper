#include <cstdio>
#include <string>
#include <vector>
#include <algorithm>
#include <cmath>
#include <memory.h>
using namespace std;
int com(string a, string b)
{
	int du,vk,i,zn;
	if (b[0]!='(')
		du=0; else
		du=1;
	vk=0;
	for (i=0;i<a.length();i++)
	{
		zn=0;
		if (du)
		while (du)
		{
			vk++;
			if (b[vk]==')')
			{
				du=0;
				vk++;
			} else
			{
				if (b[vk]==a[i])
					zn=1;
			}
		} else
			if (a[i]==b[vk])
			{
				zn=1;
				vk++;
			}
		if (!zn)
			return 0;
		if (b[vk]=='(')
			du=1;
	}
	return 1;
}
int main(void)
{
	int l,d,n,i,j,c,b[1000];
	char s[10000];
	string a;
	vector <string> dict,ta;
	freopen("r2.in","r",stdin);
	scanf("%d%d%d",&l,&d,&n);
	for (i=0;i<d;i++)
	{
		scanf("%s",&s);
		a=string(s);
		dict.push_back(a);
	}
	for (i=0;i<n;i++)
	{
		scanf("%s",&s);
		a=string(s);
		ta.push_back(a);
	}
	memset(b,0,sizeof(b));
	for (i=0;i<d;i++)
	{
		for (j=0;j<n;j++)
		{
			c=com(dict[i],ta[j]);
			if (c)
				b[j]++;
		}
	}
	freopen("r2.out","w",stdout);
	for (i=0;i<n;i++)
		printf("Case #%d: %d\n",i+1,b[i]);
	fclose(stdout);
	return 0;
}