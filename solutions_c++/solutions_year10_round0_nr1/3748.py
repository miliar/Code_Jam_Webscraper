#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <vector>
#include <iostream>
#include <map>
#include <set>
#include <algorithm>
#include <queue>
#include <sstream>
#include <fstream>

using namespace std;

int main(int argc, char *argv[])
{
 	freopen("A.in", "r", stdin);
 	freopen("A.out", "w", stdout);

	string strbuf;
	int Case, Cases;
	int N,K;
	int i,sum;
	int rem;
	int right;

	scanf("%d", &Cases);

	for (Case = 1; Case <= Cases; Case ++)
	{
		scanf("%d %d", &N, &K);
		sum=1;
		for (i=1; i<=N; i++)
		{
			sum=2*sum;
		}
		rem=K%sum;
		right=sum-1;
		if (rem==right)
		{
			printf("Case #%d: ON\n", Case);
		}
		else
		{
			printf("Case #%d: OFF\n", Case);
		}
	}
	return 0;
}