#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int N,D;
int d[100005],l[100005],A[100005];
bool Test()
{
	A[0]=2*d[0];
	if(A[0]>=D) return true;
	for(int i=0;i<N;i++)
	{
		if(A[i]==-1) continue;
		int j=i+1;
		while(d[j]<=A[i]&&j<N)
		{
			int tmp=min(d[j]-d[i]+d[j],d[j]+l[j]);
			if(tmp>A[j])
			{
				A[j]=tmp;
			}
			if(A[j]>=D) return true;
			j++;
		}
	}
	return false;
}
int main()
{
	freopen("F:\\in.txt","r",stdin);
	freopen("F:\\out.txt","w",stdout);
	int T;
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		printf("Case #%d: ",t);
		scanf("%d",&N);
		for(int i=0;i<N;i++)
		{
			scanf("%d%d",&d[i],&l[i]);
		}
		scanf("%d",&D);
		memset(A,-1,sizeof(A));
		if(Test()==false)
			printf("NO\n");
		else
			printf("YES\n");
	}
}