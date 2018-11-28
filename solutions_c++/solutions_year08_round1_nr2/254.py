#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<int> v1[104],v2[104];
int w[11],m,n;

bool cal(int p)
{
	int i,j,k;
	for(i=0;i<m;i++)
	{
		if(v1[i].size()==0)
			continue;
		for(k=0;k<n;k++)
		{
			int h=p&w[k];
			if(h)h=1;
			else h=0;
			for(j=0;j<v1[i].size();j++)
			{
				if(v1[i][j]==k&&v2[i][j]==h)
					break;
			}
			if(j<v1[i].size())
				break;
		}
		if(k==n)	return 0;
	}
	return 1;
}

int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("11.out","w",stdout);

	int nca,ca,i,j,s,a,b,h,t;

	w[0]=1;
	for(i=1;i<=10;i++)
		w[i]=w[i-1]<<1;

	scanf("%d",&nca);
	for(ca=1;ca<=nca;ca++)
	{
		scanf("%d%d",&n,&m);
		for(i=0;i<m;i++)
		{
			v1[i].clear();
			v2[i].clear();
			s=0;
			scanf("%d",&s);
			for(j=0;j<s;j++)
			{
				scanf("%d%d",&a,&b);
				a--;
				v1[i].push_back(a);
				v2[i].push_back(b);
			}
		}

		h=1<<n;
		for(i=0;i<h;i++)
			if(cal(i))break;

		printf("Case #%d: ",ca);
		if(i<h)
		{
			for(j=0;j<n;j++)
			{
				if(i&w[j])	t = 1;
				else		t = 0;
				printf("%d",t);
				if(j==n-1)	printf("\n");
				else		printf(" ");
			}
		}
		else printf("IMPOSSIBLE\n");
	}
	return 0;
}