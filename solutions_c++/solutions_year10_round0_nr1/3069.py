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
//	freopen("a.in","r",stdin);
//	freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);

	int testcase, N, K, bulbON, max;
	
	scanf("%d",&testcase);

	for (int caseId=1; caseId<=testcase; caseId++)
	{
		printf("Case #%d: ",caseId);
		scanf("%d%d",&N,&K);
		
		// Solve problem ...
		max = (1<<N);
		bulbON = max-1;
		
		printf("%s\n",((K%max)==bulbON ? "ON" : "OFF"));
		fflush(stdout);
	}
	return 0;
}
