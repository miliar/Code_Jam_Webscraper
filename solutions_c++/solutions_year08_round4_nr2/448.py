#include <iostream>
using namespace std;

int A,M,N;

int A1,A2,B1,B2;

void work_ans()
{
	A1 = A2 = B1 = B2 = -1;
	int i,j,k,l,S;
	for (i=0;i<=N;i++)
		for (j=0;j<=M;j++)
			for (k=0;k<=N;k++)
				for (l=0;l<=M;l++)
				{
					S = abs(i * l - k * j);
					if (S == A)
					{
						A1 = i;  B1 = j;  A2 = k;  B2 = l;
						return;
					}
				}
}

void show_ans()
{
	if (A1 == -1) printf("IMPOSSIBLE\n");
	else printf("%d %d %d %d %d %d\n",0,0,A1,B1,A2,B2);
}

int main()
{
	freopen("B.in","r",stdin);
	freopen("B.out","w",stdout);
	int t,i;
	cin >> t;
	for (i=1;i<=t;i++)
	{
		printf("Case #%d: ",i);
		cin >> N >> M >> A;
		work_ans();
		show_ans();
	}
	return 0;
}