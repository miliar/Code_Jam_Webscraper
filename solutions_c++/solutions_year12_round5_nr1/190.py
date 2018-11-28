#include <iostream>
#include <algorithm>
#include <vector>
#include <string.h>
#include <string>

using namespace std;

const int MAXN = 1024;

struct sNode
{
	int id;
	int L, P, LP;
};

bool operator<(const sNode &a, const sNode &b)
{
	return (a.LP > b.LP)||(a.LP == b.LP && a.P > b.P) || (a.LP == b.LP && a.P == b.P && a.id < b.id);
}

int n;
sNode p[MAXN];

void Work()
{
	cin >> n;
	for (int i = 0; i < n; i ++)
	{
		p[i].id = i;
		cin >> p[i].L;
	}
	for (int i = 0; i < n; i ++)
	{
		cin >> p[i].P;
		p[i].LP = p[i].L * p[i].P;
	}
	sort(p, p + n);
	for (int i = 0; i < n; i ++)
		cout << " " << p[i].id;
}

int main()
{
	freopen("A-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	cin.sync_with_stdio(false);

	int T;
	cin >> T;
	for (int k = 1; k <= T; k ++)
	{
		cout << "Case #" << k << ":";
		Work();
		cout << endl;
	}

	return 0;
}