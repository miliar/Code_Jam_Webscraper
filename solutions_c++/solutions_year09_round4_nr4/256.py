#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <cmath>
#include <map>
#include <set>

using namespace std;

#define fr(i, N) for(i = 0; i < (int)N; i++)
#define setContains(i,j) (((1<<j)&i) != 0)
#define MP make_pair
#define F first
#define S second
#define pb push_back
#define Eps 1e-11

typedef pair<int, int> pi;

int N;
double X[10], Y[10], R[10];

void input()
{
	int i, j;
	scanf("%d", &N);

	fr (i, N) scanf("%lf%lf%lf", &X[i], &Y[i], &R[i]);
}

double get(int a, int b) {
	return (R[a] + R[b] + sqrt((X[a] - X[b])*(X[a] - X[b]) + (Y[a] - Y[b])*(Y[a] - Y[b]))) / 2;
}

void process()
{
	if (N <= 2) {
		int i;
		double m = 0.0;
		fr (i, N) m = max(R[i], m);

		printf("%.9lf\n", m);
		return;
	}

	else if (N == 3) {
		double m = max(get(0, 1), R[2]);
		m <?= max(get(0, 2), R[1]);
		m <?= max(get(1, 2), R[0]);

		printf("%.9lf\n", m);
	}
}

int main()
{
	int t, T;
	scanf("%d", &T);

	fr(t, T)
	{
		input();
		printf("Case #%d: ", t+1);
		process();
	}
	return 0;
}

