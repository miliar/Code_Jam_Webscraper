#include <iostream>
using namespace std;

int N, M, A;

void work()
{
	cin >> N >> M >> A;
	for(int x1=1; x1<=N; x1++)
	{
		int x2 = (A%x1) ? x1-(A%x1) : 0;
		int y1 = 1;
		int y2 = (A+x2*y1)/x1;
		if (y2 <= M)
		{
			printf(" %d %d %d %d %d %d\n", 0, 0, x1, y1, x2, y2);
			if (x1*y2-x2*y1 != A)
				cerr << "error" << endl;
			return;
		}
	}
	cout << " IMPOSSIBLE" << endl;
}

int main()
{
	freopen("B-large.in", "r", stdin);
	freopen("b.out", "w", stdout);
	int nOfTest;
	cin >> nOfTest;
	for(int testCase=0; testCase<nOfTest; testCase++)
	{
		printf("Case #%d:", testCase+1);
		work();
	}
}
