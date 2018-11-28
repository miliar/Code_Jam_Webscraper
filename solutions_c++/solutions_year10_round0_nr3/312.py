#include <stdio.h>
#include <queue>
using namespace std;
int T,R,k,n,P;
long long GS,CS;
vector<int> start,finish;
vector<long long> SUM;
vector<int> v;
void calc()
{
	CS=0;
	start.assign(n,-1);
	finish.assign(n,-1);
	SUM.assign(n,0);
	int time=0,i=0;
	while(1)
	{
		if (finish[i]!=-1)
			break;
		if (start[i] == -1)
		{
			start[i] = time++;
			SUM[i]=CS;
		}
		else
		{
			P=i;
			finish[i] = time++;
			break;
		}
		long long S=0;
		int Z=0;
		while (S+(long long)v[i] <= (long long)k && Z<n)
		{
			S+=v[i];
			i=(i+1)%n;
			Z++;
		}
		CS+=S;
	}
}
int main()
{
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d",&T);
	for (int i=0;i<T;i++)
	{
		GS=0;
		long long res = 0;
		scanf("%d%d%d",&R,&k,&n);
		v.resize(n);
		for (int j=0;j<n;j++)
		{
			scanf("%d",&v[j]);
			GS+=v[j];
		}
		calc();
		int p=0;
		while (p!=P)
		{
			int S=0;
			while (S+v[p] <= k)
			{
				S+=v[p];
				p=(p+1)%n;
			}
			res+=S;
			R--;
		}
		res+=(CS-SUM[P])*(R/(finish[P]-start[P]));
		R%=(finish[P]-start[P]);
		for (int j=0;j<R;j++)
		{
			long long S=0;
			while (S+v[p] <= k)
			{
				S+=v[p];
				p=(p+1)%n;
			}
			res+=S;
		}
		printf("Case #%d: %lld\n",i+1,res);
	}
	return 0;
}