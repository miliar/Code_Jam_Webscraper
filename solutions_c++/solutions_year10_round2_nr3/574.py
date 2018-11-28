#include <cstdio>

using namespace std;

const int base=100003;
const int max=25;

int comb[max+2][max+1]={0};

void ComputeComb()
{
	for (int i=1; i<=max; i++)
		comb[i][0]=1;
	for (int i=1; i<=max; i++)
		for (int j=1; j<=i; j++)
			comb[i][j]=(comb[i-1][j-1]+comb[i-1][j])%base;
}

int main()
{
	/*
	freopen("inputC.txt","r",stdin);
	freopen("outputC.txt","w", stdout);
	*/
	freopen("C-small-attempt0.in","r",stdin);
	freopen("C-small-attempt0.out","w", stdout);

	ComputeComb();

	int testcase;
	scanf("%d", &testcase);
	for (int i=0; i<testcase; i++)
	{
		int n;
		scanf("%d", &n);
		
		int a[max+1][max+1]={0};
		for (int j=2; j<=n; j++)
			a[j][1]=1;
		for (int j=2; j<=n; j++)
			for (int k=2; k<j; k++)
				for (int l=1; l<k; l++)
					a[j][k]=(a[j][k]+(a[k][l]*comb[j-k][k-l-1])%base)%base;			
		int num=0;
		for (int j=1; j<=n; j++)
			num=(num+a[n][j])%base;
		printf("Case #%d: %d\n", i+1, num);
	}

	fflush(stdout);

	return 0;
}