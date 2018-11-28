#include <cstdlib>
#include <cstdio>
#include <iostream>
#include <cstring>
#define LL long long 

using namespace std;
int Arr[10000];
int Mark[10000];
LL Ansi[10000];
inline void Solve(int KKK)
{
	int N,C,R;
	scanf("%d%d%d",&R,&C,&N);
	memset(Mark,0,sizeof(Mark));
	for (int i=1;i<=N;++i)
		scanf("%d",&Arr[i]);
	int p=1,K=0;
	LL Tmp;
	LL Ans=0;
	for (int i=1;i<=R;++i)
	{
		if (Mark[p]==0)
			Mark[p]=i;
		else
		{
			LL RR=i-Mark[p];
			LL RJ=R-Mark[p]+1;
			LL RK=RJ/RR;
			LL RY=RJ%RR;
			LL AnsR=Ans-Ansi[Mark[p]-1];
			Ans+=AnsR*(RK-1)+(Ansi[Mark[p]+RY-1]-Ansi[Mark[p]-1]);
			
			break;
		}
		Tmp=0;K=0;
		while (Tmp+Arr[p]<=C&&K<N)
		{
			++K;
			Tmp+=Arr[p];
			++p;
			if (p>N)	p=1;
		}
		Ans+=Tmp;
		Ansi[i]=Ans;
	}
	printf("Case #%d: %I64d\n",KKK,Ans);
}
		

int main()
{
	freopen("C.in","r",stdin);
	freopen("C.out","w",stdout);
	
	int Test;
	scanf("%d",&Test);
	for (int i=1;i<=Test;++i)
		Solve(i);
	return 0;
}