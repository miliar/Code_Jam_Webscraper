#include <iostream>
#include <iomanip>
using namespace std;

const int maxC = 200 + 5;
int C, D;
double P[maxC], V[maxC];

bool check(double dis)
{
	double e = -1e6;
	for (int i = 0; i < C; i ++)
	{
		if (e + dis > P[i])
			e = e + (V[i] - 1) * D;
		else
			e = P[i] - dis + (V[i] - 1) * D;
		if (e > P[i] + dis) return false;
		e += D;
	}
	return true;
}

void solve(int cID)
{
	cin >> C >> D;
	for (int i = 0; i < C; i ++)
		cin >> P[i] >> V[i];

	double hd, tl, md;
	hd = 0.0; tl = 1e6;
	double eps = 1e-7;
	while (hd + eps < tl) 
	{
		md = (hd + tl) / 2;
		if (check(md)) tl = md; else hd = md;
	}
	cout << "Case #" << cID << ": ";
	cout << setprecision(7) << (hd + tl) / 2 << endl;
}

int main()
{
	int T;
	cin >> T;
	for (int t = 1; t <= T; t ++)
		solve(t);
}
