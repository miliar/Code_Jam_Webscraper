#include <iostream>
#include <cmath>
#include <cstdio>

inline double sq(double a)
{
    return a*a;
}

using namespace std;

int main()
{
    int C;
    cin >> C;
    
    for(int z = 0; z < C; z++)
    {
	int N;
	cin >> N;

	double X[3], Y[3], R[3];

	for(int j = 0; j < N; j++)
	    cin >> X[j] >> Y[j] >> R[j];

	double ret;
	if(N == 1)
	{
	    ret = R[0];
	    goto print;
	}
	else if(N == 2)
	{
	    ret = max(R[0], R[1]);
	    goto print;
	}
	else
	{
	    ret = 10000000000LL;
	    for(int i = 0; i < 3; i++)
	    {
		int test[3][2] = {{1,2}, {0,2}, {0,1}};
		ret = min(ret, max((sqrt(sq(X[test[i][0]] - X[test[i][1]]) + sq(Y[test[i][0]] - Y[test[i][1]])) + R[test[i][0]] + R[test[i][1]])/2.0, R[i]));
	    }
	}

	print:
	    printf("Case #%d: %1.6lf\n", z + 1, ret);
    }
}
