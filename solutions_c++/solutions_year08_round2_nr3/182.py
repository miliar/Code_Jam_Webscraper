#include <cstdio>

int main(void)
{
	freopen("C-small-attempt0.in", "r" ,stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int q=1;q<=T;q++)
	{
		int K, N;
		scanf("%d %d", &K, &N);
		int data[100];
		for(int i=0;i<N;i++) scanf("%d", data+i);

		bool isVisit[5000]={false, };

		isVisit[0]=true;
		int ansField[5000];
		ansField[0]=0;

		int curPoint=0;

		for(int i=1;i<K;i++)
		{			
			for(int j=0;j<=i;j++) 
			{
				curPoint++;
				curPoint%=K;
				if(isVisit[curPoint]) j--;
			}
			ansField[curPoint]=i; isVisit[curPoint]=true;
		}

		printf("Case #%d:", q);
		for(int i=0;i<N;i++) printf(" %d", ansField[data[i]-1]+1);
		printf("\n");
	}

	return 0;
}

