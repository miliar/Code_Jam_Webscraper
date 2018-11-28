#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>

using namespace std;

double p[100005], pa[100005];
 
int main()
{
	int nCasos;
	scanf("%d", &nCasos);
	
	for(int caso=1; caso<=nCasos; caso++)
	{
		int A, B;
		scanf("%d %d", &A, &B);
		
		for(int i=0; i<A; i++)
			scanf("%lf", &p[i]);
		
		pa[0] = p[0];
		for(int i=1; i<A; i++)
			pa[i] = pa[i-1] * p[i];
		
		double minE = 1 + B + 1;
		
		for(int pos = A; pos >= 0; pos--)
		{
			double p1 = (pos != 0 ? pa[pos-1] : 1);
			int n1 = 2*(A - pos) + B - A + 1;
			int n2 = n1 + B + 1;
			minE = min(minE, p1 * n1 + (1 - p1) * n2);
		}

		printf("Case #%d: %.10lf\n", caso, minE);
	}
	
	return 0;
}
