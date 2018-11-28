#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <iostream>

using namespace std;

int N,K;
const int Fx[4][2]={{1,0},{0,1},{1,1},{-1,1}};

char OldMap[100][100];
char Map[100][110];

bool Check(char JJJ)
{
	for (int i=1;i<=N;++i)
		for (int j=1;j<=N;++j)
			for (int f=0;f<4;++f)
				for (int l=0;l<K&&Map[i+Fx[f][0]*l][j+Fx[f][1]*l]==JJJ;++l)
					if (l==K-1)
						return true;
	return false;
}

void Solve(int KKK)
{
	memset(Map,0,sizeof(Map));
	scanf("%d%d",&N,&K);
	for (int i=1;i<=N;++i)
		scanf("%s",OldMap[i]+1);
	for (int i=1;i<=N;++i)
		for (int j=1;j<=N;++j)
			Map[i][j]=OldMap[N-j+1][i];
	for (int j=1;j<=N;++j)
	{
		int K=N+1;
		char tmp;
		for (int i=N;i;--i)
			if (Map[i][j]!='.')
			{
				tmp=Map[i][j];
				Map[i][j]='.';
				Map[--K][j]=tmp;
			}
	}
// 	for (int i=1;i<=N;++i)
// 	{
// 		for (int j=1;j<=N;++j)
// 			cout<<Map[i][j];
// 		cout<<endl;
// 	}
	bool A1=Check('R');
	bool A2=Check('B');
	printf("Case #%d: ",KKK);
	if (A1&&A2)
		printf("Both\n");
	if (A1&&!A2)
		printf("Red\n");
	if (!A1&&A2)
		printf("Blue\n");
	if (!A1&&!A2)
		printf("Neither\n");
}

int main()
{
	freopen("A.in","r",stdin);
	freopen("A.out","w",stdout);
	int Test;
	scanf("%d",&Test);
	for (int i=1;i<=Test;++i)
		Solve(i);
}