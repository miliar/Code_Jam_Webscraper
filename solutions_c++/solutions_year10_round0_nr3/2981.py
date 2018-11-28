#include <sstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int main(int argc, char **argv)
{
//	freopen("c.in","r",stdin);
	freopen("C-small-attempt0.in","r",stdin);freopen("C-small-attempt0.out","w",stdout);
//	freopen("C-large.in","r",stdin);freopen("C-large.out","w",stdout);

	int testcase, R, k, N, numberOfEuros;
	int gi[10]={0};
	
	scanf("%d",&testcase);

	for (int caseId=1; caseId<=testcase; caseId++)
	{
		printf("Case #%d: ", caseId);
		scanf("%d%d%d",&R, &k, &N);
		numberOfEuros = 0;
		for (int i=0; i<N; i++)
		{
			scanf("%d", &gi[i]);
		}
		
		// Solve problem ...
		
		for (int counter=1, i=0, j, sum; counter<=R; counter++)
		{
			sum=gi[i];
			j=(i+1)%N;
			
			while ( (i!=j) && (sum+gi[j]<=k) )
			{
				sum+=gi[j];
				j=(j+1)%N;
			}
			i=j;
			numberOfEuros+=sum;
		}
		
		printf("%d\n", numberOfEuros);
		fflush(stdout);
	}
	return 0;
}
