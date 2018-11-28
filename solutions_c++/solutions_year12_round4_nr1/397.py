#include<cstdio>
#include<algorithm>
using namespace std;
#define MAXN 10010

int Q[MAXN];
int F[MAXN];
int D[MAXN],L[MAXN];
int T,N,Dt;

int main()
{
	//freopen("A.in","r",stdin);
//	freopen("A.out","w",stdout);
	int i;
	int head,tail;
	scanf("%d",&T);
	for (int t=1;t<=T;t++)
	{
		scanf("%d",&N);
		for (i=0;i<N;i++)
			scanf("%d%d",&D[i],&L[i]);
		scanf("%d",&Dt);
		D[N++] = Dt;
		head = tail = 0;
		Q[tail++] = 0;
		F[0] = D[0];
		for (i=1;i<N;i++)
		{
			while (head < tail && D[Q[head]] + F[Q[head]] < D[i])
				head++;
			if (head == tail)
				break;
			F[i] = min(L[i],D[i] - D[Q[head]]);
			Q[tail++] = i;
		}
		printf("Case #%d: ",t);
		if (i < N)
			printf("NO\n");
		else
			printf("YES\n");
	}
	return 0;
}
