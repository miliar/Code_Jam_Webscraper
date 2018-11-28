#include <iostream>
#include <iomanip>

using namespace std;

struct Cdata
{
	double b, e, w, l;
}data[1002];

int n, TT;
double X, S, R, T, ans;

void init()
{
	cin >> X >> S >> R >> T >> n;
	for(int i = 1 ; i <= n ; i++)
	{
		cin >> data[i].b >> data[i].e >> data[i].w;
		data[i].l = data[i].e - data[i].b;
		X -= data[i].l;
	}
}

bool cmp(const Cdata &a, const Cdata &b)
{
	if(a.w < b.w) return true;
	return false;
}

void work()
{
	int s = 0;
	data[n + 1].w = 0, data[n + 1].l = X;
	sort(data + 1, data + n + 2, cmp);
	ans = 0;
	for(int i = 1 ; i <= n + 1 ; i++)
	{
		if(T >= data[i].l / (R + data[i].w))
		{
			ans += data[i].l / (R + data[i].w);
			T -= data[i].l / (R + data[i].w);
		}
		else
		{
			ans += (data[i].l - T * (R + data[i].w)) / (S + data[i].w) + T;
			T = 0;
		}
	}
	cout << "Case #" << TT << ": " << fixed << setprecision(7) << ans << endl;
}

int main()
{
	int TTT;
	freopen("A.in", "r", stdin);
	freopen("A.out", "w", stdout);
	cin >> TTT;
	for(TT = 1 ; TT <= TTT ; TT++)
	{
		init();
		work();
	}
	return 0;
}
