#include <assert.h> 
#include <ctype.h> 
#include <float.h> 
#include <math.h> 
#include <stdio.h> 
#include <string> 
#include <stdlib.h> 
#include <time.h> 
#include <algorithm> 
#include <numeric> 
#include <functional> 
#include <utility> 
#include <vector> 
#include <list> 
#include <set> 
#include <map> 
#include <queue> 
#include <stack> 
#include <sstream> 
#include <iostream> 

using namespace std; 

#define rep(i,n) for(int i=0;i<(n);++i)
#define clr(a,b) memset(a,b,sizeof(a)); 
#define all(c) (c).begin(), (c).end() 
#define inf 1000000000 

typedef long long ll;
typedef pair<int, int> pii;
typedef vector<string> vs;
typedef vector<int> vi;

struct Circle
{
	int x, y, r;
};

Circle v[100];

double dist(double x1, double y1, double x2, double y2) 
{
	return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}

double cover(Circle c1, Circle c2)
{
	double d = dist(c1.x, c1.y, c2.x, c2.y) + c1.r + c2.r;

	return d / 2;
}

int main(int argc, char* argv[])
{
	freopen("Test.in", "r", stdin);
	//freopen("C:\\out", "w", stdout);

	int caseCount;
	cin >> caseCount;

	for (int nCase = 1; nCase <= caseCount; nCase++)
	{
		int N;
		scanf("%d", &N);

		if (N > 3)
			continue;

		for (int i = 0; i < N; i++)
		{
			scanf("%d%d%d", &v[i].x, &v[i].y, &v[i].r);
		}

		double R = INT_MAX;

		if (N == 1)
		{
			R = v[0].r;
		}
		else if (N == 2)
		{
			R = max(v[0].r, v[1].r);
		}
		else
		{
			R = min(R,  max((double)v[0].r, cover(v[1], v[2])));
			R = min(R,  max((double)v[1].r, cover(v[0], v[2])));
			R = min(R,  max((double)v[2].r, cover(v[0], v[1])));
		}



		
		printf("Case #%i: %.8lf\n", nCase, R);
		fflush(stdout);
	}


	return 0;
}


