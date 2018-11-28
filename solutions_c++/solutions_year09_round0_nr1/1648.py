#include<iostream>
#include<vector>
#include<cstring>
using namespace std;

int l,dd,n;
vector<char> d[5010];
char a[5010][20];
char b[100000];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	scanf("%d%d%d",&l,&dd,&n);
	int i,j,k,m;
	bool flag;
	for(i=0;i<dd;i++)
		scanf("%s",a[i]);
	for(k=0;k<n;k++)
	{
		scanf("%s",b);
		for(i=0;i<l;i++) d[i].clear();
		int c=0;
		for(i=0;i<strlen(b);i++)
		{
			if(b[i]=='(')
			{
			  j=i+1;
			  while(b[j]!=')')
			  {
				 d[c].push_back(b[j]);
				 j++;
			  }
			  i=j;
			  c++;
			}
			else d[c++].push_back(b[i]);
		}
		int s=0;
	for(i=0;i<dd;i++)
	{
		flag=true;
		for(j=0;j<l;j++)
		{
			for(m=0;m<d[j].size();m++)
				if(a[i][j]==d[j][m]) break;
			if(m==d[j].size()) 
			{
				flag=false;
				break;
			}
		}
		if(flag) s++;
	}
	printf("Case #%d: %d\n",k+1,s);
	}
	return 0;
}
