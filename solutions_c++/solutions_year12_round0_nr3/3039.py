#include <algorithm>
#include <iostream>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <map>
#include <string>
using namespace std;

#define zero(a) memset(a,0,sizeof(a))
#define one(a) memset(a,1,sizeof(a))
#define fone(a) memset(a,-1,sizeof(a))

int cmp(char *s,char *t)
{
	if(strlen(s)!=strlen(t))
		return strlen(s)-strlen(t);
	return strcmp(s,t);
	/*
	int i;
	for(i=0;i<strlen(s);i++)
	{
		if(s[i]==t[i])
			continue;
		return s[i]-t[i];
	}
	return 0;
	*/
}
map<string ,bool>hash;
int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	int T,TT=1;
	scanf("%d",&T);
	while(T--)
	{
		int a,b,i,j,k;
		scanf("%d%d",&a,&b);
		char s[10]={0};
		char t[10]={0};
		char sb[10]={0};
		sprintf(sb,"%d",b);
		int sum=0;
		for(i=a;i<b;i++)
		{
			sprintf(s,"%d",i);
			int l=strlen(s);
			hash.clear();
			for(j=1;j<l;j++)
			{
				strcpy(t,s+j);
				strncat(t,s,j);
				int num;
				string tj=t;
				if((!hash.count(tj))&&cmp(t,s)>0&&cmp(t,sb)<=0)
				{
					//cout<<s<<' '<<t<<' '<<sb<<endl;
					sum++;
				}
				hash[tj]=true;
			}
		}
		printf("Case #%d: %d\n",TT++,sum);
	}
	return 0;
}