#include <iostream>
using namespace std;

const int DIGIT = 1000;
int mark[DIGIT][DIGIT];

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("c0.out", "w", stdout);
	memset(mark, -1, sizeof(mark));
	int C = 0;
	for(int a=2, b=6, i=1; mark[a][b] == -1; i++, C++)
	{
		mark[a][b] = i;
		int t = 6*b-4*a;
		t = (t%DIGIT+DIGIT)%DIGIT;
		a = b, b = t;
	}

	int T;
	cin >> T;
	for(int testCase=0; testCase<T; testCase++)
	{
		int n;
		cin >> n;
		n = n%C;
		if (n == 0)
			n = C;
		int a = 2, b = 6;
		for(int i=1; i<n; i++)
		{
			int t = 6*b-4*a;
			t = (t%DIGIT+DIGIT)%DIGIT;
			a = b, b = t;
		}
		b = (b-1+DIGIT)%DIGIT;
		printf("Case #%d: ", testCase+1);
		if (b < 100)
			cout << '0';
		if (b < 10)
			cout << '0';
		cout << b << endl;
	}
}
