#include<stdio.h>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
struct node
{
	string s;
	vector<int> v;
};
node a[100000];
int z,ans;
char s[1000];
void inst(char *s,int k)
{
	string ss;
	int i,temp;
	if (*s=='\0')
		return;
	ss="";
	s++;
	while ((*s>='a'&&*s<='z')||(*s>='0'&&*s<='9'))
	{
		ss+=(*s);
		s++;
	}
	for (i=0;i<a[k].v.size();i++)
	{
		temp=a[k].v[i];
		if (a[temp].s.compare(ss)==0)
		{
			inst(s,temp);
			break;
		}
	}
	if (i==a[k].v.size())
	{
		a[k].v.push_back(z);
		a[z].v.clear();
		a[z].s=ss;
		z++;
		inst(s,z-1);
		ans++;
	}
	return;
}
int main()
{
	int t,tt,m,n,i;
	scanf("%d",&t);
	for (tt=1;tt<=t;tt++)
	{
		scanf("%d %d",&m,&n);
		a[0].s="";
		a[0].v.clear();
		z=1;
		ans=0;
		for (i=0;i<m;i++)
		{
			scanf("%s",s);
			inst(s,0);
		}
		ans=0;
		for (i=0;i<n;i++)
		{
			scanf("%s",s);
			inst(s,0);
		}
		printf("Case #%d: %d\n",tt,ans);
	}
	return 0;
}