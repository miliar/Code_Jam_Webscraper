
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
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

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>


long unsigned int N,K;
int first_light;
int main()
{

	printf("\nHello GCJ");

		freopen("A-large.in","r",stdin);
		freopen("Output.out","w",stdout);
	//freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
	//	freopen("A-small-attempt1.in","r",stdin);freopen("A-small-attempt1.out","w",stdout);
	//	freopen("A-small-attempt2.in","r",stdin);freopen("A-small-attempt2.out","w",stdout);
	//	freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
	int testcase;
	scanf("%d",&testcase);
	
	for (int caseId=1;caseId<=testcase;caseId++)
	{
		scanf("%d%d",&N,&K);
		first_light = (pow(2,(double)N) - 1);

		if((int)(K + 1) % (first_light + 1) == 0)
		{
			printf("Case #%d: ON\n",caseId);
		}
		else
		{
			printf("Case #%d: OFF\n",caseId);
		}

	}
	return 0;
}

