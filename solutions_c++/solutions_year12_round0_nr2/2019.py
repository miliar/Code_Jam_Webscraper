#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int Arr[110][5];

void Solve(int TestNo)
{
	int N,S,P,Ans=0;
	memset(Arr,0,sizeof(Arr));
	scanf("%d%d%d",&N,&S,&P);
	for (int i=1;i<=N;++i)
		scanf("%d",&Arr[i][0]);
	for (int i=1;i<=N;++i)
	{
		Arr[i][1]=Arr[i][2]=Arr[i][3]=Arr[i][0]/3;
		for (int j=1;j<=Arr[i][0]%3;++j)
			Arr[i][j]++;
		if (Arr[i][1]>=P)
			Ans++;
		else
		if (Arr[i][1]==Arr[i][2]&&Arr[i][1]+1>=P&&Arr[i][1]+1<=10&&Arr[i][2]-1>=0&&S>0)
		{
			S--;
			Ans++;
		}
	}
	printf("Case #%d: %d\n",TestNo,Ans);
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int T;
	scanf("%d",&T);
	for (int i=1;i<=T;++i)
		Solve(i);
	return 0;
}
