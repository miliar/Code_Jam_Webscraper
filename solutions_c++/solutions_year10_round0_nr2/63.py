#include <stdio.h>
#include <assert.h>
#include <math.h>
#include <iostream>
#include <string>
#include <set>
#include <queue>
#include <vector>
#include <algorithm>
#include <map>
#include <stack>
#include <memory.h>
#include <time.h>

using namespace std;

typedef long long ll;

ll gcd(ll a, ll b) 
{
	return b == 0 ? a : gcd(b, a % b); 
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);

	int caseCount;
	scanf("%d", &caseCount);

	
	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		 int g= 26000000;
		 g = gcd(g, 11000000);
		 g = gcd(g, 600000);
		
		fflush(stdout);
	}

	return 0;
}


