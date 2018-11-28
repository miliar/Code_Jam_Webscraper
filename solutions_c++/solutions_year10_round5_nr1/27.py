#include <cstdio>
#include <iostream>
#include <set>
using namespace std;
#define oo 15
#define mm 1000005
typedef long long LL;
set<int> hash;
int K,P,D;
int a[oo];
int p[mm],M,MAX;
bool mk[mm];

inline void Prepare()
{
	mk[1]=true;
	for (int i=2;i<=1000000;++i)
		if (!mk[i])
			for (int j=i+i;j<=1000000;j+=i)
				mk[j]=true;
}

inline void Readin()
{
	int d;
	scanf("%d%d",&d,&K);
	D=1;
	for (int i=1;i<=d;++i)
		D*=10;
	MAX=2;
	for (int i=1;i<=K;++i)
	{
		scanf("%d",a+i);
		MAX>?=a[i]+1;
	}
}

inline LL Pow(int x,int y)
{
	LL res=1;
	while (y)
	{
		if (y&1) res=res*x%P;
		x=(LL)x*x%P;
		y>>=1;
	}
	
	return res;
}

inline void Solve()
{
	if (K<=1) puts("I don't know.");
	else
	if (K==2)
	{
		if (a[1]==a[2])
		{
			for (P=MAX;P<=D;++P) if (!mk[P])
			{
				printf("%d\n",a[1]);
				return;
			}
		}
		
		puts("I don't know.");
	}
	else{
		hash.clear();
		int Ans=-1,cnt=0;
		for (P=MAX;P<=D;++P) if (!mk[P])
		{
			int A=Pow((a[1]-a[2]+P)%P,P-2)*(a[2]-a[3]+P)%P,B;
			for (int i=1;i<=K-2;++i)
				if (Pow((a[i]-a[i+1]+P)%P,P-2)*(a[i+1]-a[i+2]+P)%P!=A) goto End;
			
			B=(a[2]-a[1]*(LL)A%P+P)%P;
			
			for (int i=2;i<=K;++i)
				if (B!=(a[i]-a[i-1]*(LL)A%P+P)%P) goto End;
			
			Ans=(a[K]*(LL)A+B)%P;
			if (!hash.count(Ans)) hash.insert(Ans);
			
			End:;
		}
		if (hash.size()>=2) Ans=-1;
		
		if (Ans==-1) puts("I don't know.");
		else printf("%d\n",Ans);
	}
}

int main()
{
	//freopen("i.txt","r",stdin);

	int Test,Case=0;
	Prepare();
	for (scanf("%d",&Test);Test--;)
	{
		printf("Case #%d: ",++Case);
		Readin();
		Solve();
	}
	
	return 0;
}
