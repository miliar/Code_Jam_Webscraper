#include<cstdio>
using namespace std;

int zm[255][255];
int op[255][255];
char buf[255];

int main() {
	int t,c,d,n;
	char q,w,e;
	scanf("%d\n",&t);
	for (int tt=1; tt<=t; tt++)
	{
		for (int i='A'; i<='Z'; i++)
			for (int j='A'; j<='Z'; j++)
				zm[i][j] = op[i][j] = 0;

		scanf("%d ",&c);
		for (int i=0; i<c; i++)
		{
			q = getchar();
			w = getchar();
			e = getchar();
			getchar();
			zm[q][w] = zm[w][q] = e;
		}
		scanf("%d ",&d);
		for (int i=0; i<d; i++)
		{
			q = getchar();
			w = getchar();
			getchar();
			op[q][w] = op[w][q] = 1;
		}
		scanf("%d ",&n);
		scanf("%s",buf);
		int lc = 0;
		for (int i=1; i<n; i++)
		{
			q = buf[i-1];
			w = buf[i];
			if (lc < i && zm[q][w])
			{
				buf[i-1] = 0;
				buf[i] = zm[q][w];
			}
			for (int j=lc; j<i; j++)
				if (op[buf[j]][buf[i]])
				{
					lc = i+1;
				}
			
		}
		bool jest = false;
		printf("Case #%d: [",tt);
		for (int i=lc; i<n; i++)
			if (buf[i] > 0)
			{
				if (jest)
					printf(", ");
				printf("%c",buf[i]);
				jest = true;
			}
		printf("]\n");

	}

}
