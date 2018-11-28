#include <fstream>
#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

int T, N;
int res, n, it;
int GetSum(int a, int b)
{
	res = 0;
	n = (int)max((a == 0) ? 1 : floor(log(a + .0)/log(2.0)) + 1, (b == 0) ? 1 : floor(log(b + .0)/log(2.0)) + 1);
	for (it = 0; it < n; it++)
	{
		res |= (a & (1 << it)) ^ (b & (1 << it));
	}
	return res;
}

int n_mx, n_mn;
/*bool ProbablyEquals(int a, int b, int ex)
{
	n_mx = (mx == 0) ? 1 : (int)floor(log(mx + .0)/log(2.0)) + 1;
	n_mn = (mn == 0) ? 1 : (int)floor(log(mn + .0)/log(2.0)) + 1;
	for(it = n_mx - 1; it > n_mn; it++)
	{
		if((mx & (1 << it)) != (mn & (1 << it)))
		{
			return false;
		}
	}
	return true;
}*/

int mx, mn, result;
vector<int> c;
void calculate(int pile1, int pile2, int normal1, int normal2, int pos)
{
	if(pos == N)
	{
		if(pile1 == pile2 && pile1 > 0 && pile2 > 0)
		{
			result = max(max(normal1, normal2), res);
		}
		return;
	}
	
	calculate(GetSum(pile1, c[pos]), pile2, normal1 + c[pos], normal2, pos + 1);
	calculate(pile1, GetSum(pile2, c[pos]), normal1, normal2 + c[pos], pos + 1);
}

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");

	GetSum(50, 10);
	GetSum(5, 4);
	GetSum(7, 9);

	cin >> T;
	for (int t = 0; t < T; t++)
	{
		cin >> N;
		c.resize(N);
		for(int i = 0; i < N; i++)
		{
			cin >> c[i];
		}
		sort(c.rbegin(), c.rend());

		result = -1;
		calculate(0, 0, 0, 0, 0);
		
		cout << "Case #" << t + 1 << ": ";
		if(result == -1)
		{
			cout << "NO" << endl;
		}
		else
		{
			cout << result << endl;
		}
	}

	return 0;
}