#include <iostream>
using namespace std;

int m[111111];
int q[11][10000];
int val[11][10000];

int calc(int lev, int pos, int lft)
{
	int res=1000000111;
	if (lev==-1)
	{
		if (lft>m[pos])
			return res;
		return 0;
	}
	res=calc(lev-1,2*pos,lft-1)+calc(lev-1,2*pos+1,lft-1)+q[lev][pos];
	res=min(res,calc(lev-1,2*pos,lft)+calc(lev-1,2*pos+1,lft));
	if (res>1000000111)
		res=1000000111;
	return res;
}

int main()
{
	int t,p,e;
	freopen("B-large.in","r",stdin);
	freopen("out1.txt","w",stdout);
	scanf("%d",&t);
	for (int i=0;i<t;i++)
	{
		scanf("%d",&p);
		for (int j=0;j<(1<<p);j++)
			scanf("%d",m+j);
		for (int j=0;j<p;j++)
		{
			for (int h=0;h<(1<<p-j-1);h++)
				scanf("%d",q[j]+h);
		}
		int res = 0;
		res=calc(p-1,0,p);
		///*for (int j=0;j<p;j++)
		//{
		//	for (int h=0;h<p;h++)
		//	{
		//		for (int g=0;g<(1<<p-j-1);g++)
		//			val[j][h][g]=min(val[][][]+val[][][]);
		//	}
		//}
		//res=val[p][p][0];*/
		//for (int h=0;h<p;h++)
		//{
		//	for (int j=0;j<(1<<p-h);j+=2)
		//		if (m[j]&&m[j+1])
		//		{
		//			int v = min(m[j],m[j+1])-1;
		//			m[j]=m[j+1]=0;
		//			m[j/2]=v;
		//		}
		//		else
		//		{
		//			res++;
		//			m[j]=m[j+1]=0;
		//		}
		//}
		printf("Case #%d: %d\n",i+1,res);
	}
	return 0;
}