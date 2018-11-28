#include<stdio.h>
#include<string.h>
#include<vector>
using namespace std;
struct node
{
	__int64 x,y;
};
vector<node>v;
int main()
{
	__int64 X,Y,x,y,A,B,C,D,M,ans,n,i,j,k;
	int t,o=0;
	scanf("%d",&t);
	freopen("gcjA.out","w",stdout);
	while(t--)
	{
		v.clear();
		scanf("%I64d %I64d %I64d %I64d %I64d %I64d %I64d %I64d",&n,&A,&B,&C,&D,&x,&y,&M);
		X=x;
		Y=y;
		node nd;
		nd.x=X;
		nd.y=Y;
		v.push_back(nd);
		for (i=1;i<=n-1;i++)
		{
			X=(A*X+B)%M;
			Y=(C*Y+D)%M;
			nd.x=X;
			nd.y=Y;
			v.push_back(nd);
		}
		ans=0;
		for (i=0;i+2<v.size();i++)
			for (j=i+1;j+1<v.size();j++)
				for (k=j+1;k<v.size();k++)
				{
					node na,nb,nc;
					na=v[i];
					nb=v[j];
					nc=v[k];
					if ((na.x+nb.x+nc.x)%3==0 && (na.y+nb.y+nc.y)%3==0 ) ans++; 
				}
				printf("Case #%d: %I64d\n",++o,ans);
	}
	fclose(stdout);
	return 0;
}
