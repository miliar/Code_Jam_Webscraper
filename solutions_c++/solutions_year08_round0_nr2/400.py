#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

#define nmax 200

struct route
{
	int t1,t2,dir;
	bool operator < (const route&a) const
	{
		return t1<a.t1;
	}
} x[nmax];

char s1[10],s2[10];
int l,train[nmax][2];

int tosec(char*s)
{
	return ((s[0]-'0')*10+(s[1]-'0'))*60+((s[3]-'0')*10+(s[4]-'0'));
}

int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int T,X,n1,n2,num[2],i,j;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&X);
		scanf("%d%d",&n1,&n2);
		for(i=0;i<n1;i++)
		{
			scanf("%s%s",s1,s2);
			x[i].dir=0;
			x[i].t1=tosec(s1);
			x[i].t2=tosec(s2);
		}
		for(i=n1;i<n1+n2;i++)
		{
			scanf("%s%s",s1,s2);
			x[i].dir=1;
			x[i].t1=tosec(s1);
			x[i].t2=tosec(s2);
		}
		sort(x,x+n1+n2);
		num[0]=num[1]=l=0;
		
		for(i=0;i<n1+n2;i++)
		{
			for(j=0;j<l;j++)
				if (train[j][0]==x[i].dir && train[j][1]<=x[i].t1) break;
			if (l==j) ++num[x[i].dir];
			else { train[j][0]=train[--l][0]; train[j][1]=train[l][1]; }
			train[l][0]=1-x[i].dir;
			train[l++][1]=x[i].t2+X;
		}

		printf("Case #%d: %d %d\n",t,num[0],num[1]);
	}
	return 0;
}