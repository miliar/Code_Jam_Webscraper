#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;

int calc(int x)
{
	for (int bb=1;;bb*=10)
		if (bb>x) return bb;
}
vector <int> v;
int main()
{
	freopen("C-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for (int cas=1;cas<=T;cas++)
	{
		int A,B;
		scanf("%d%d",&A,&B);
		int res=0;
		for (int i=A;i<=B;i++)
		{
			v.clear();
			int bas=1;
			for (;;bas*=10)
			{
				if (bas>i) break;
				int now=i%bas;
				int now1=i/bas;
				int tt=calc(now1);
				int x=now*tt+now1;
				if (i<x && x>=A && x<=B)
					v.push_back(x);
			}
			int z=v.size();
			if (z>=1) sort(v.begin(),v.end());
			if (z>=1) res++;
			for (int j=1;j<z;j++)
				if (v[j]!=v[j-1]) res++;
		}
		printf("Case #%d: %d\n",cas,res);
	}
}
