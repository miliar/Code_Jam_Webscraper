#include <stdio.h>
#include <math.h>

#define ON "ON"
#define OFF "OFF"

int main()
{
//	freopen("in.in","r",stdin);freopen("out.out","w",stdout);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase = 0;
	scanf("%d",&testcase);
	for (int caseId=1; caseId<=testcase; caseId++)
	{
		int N = 0;
		int K = 0;
		scanf("%d %d", &N, &K);

		// stepen'
		int step = pow(2.0f, (float)N);
		int rez = (K+1)%step;

		//char str[100];
		//scanf("%s",str);

		printf("Case #%d: ", caseId);
		if (rez == 0)
			printf(ON);
		else
			printf(OFF);
		printf("\n");
	}

	return 0;
}