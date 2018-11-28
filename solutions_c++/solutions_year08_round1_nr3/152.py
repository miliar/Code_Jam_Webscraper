#include <fstream>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

int n;

int expmod(const int &b, const int &e, const int &m)
{
	if (e == 0)
		return 1;
	int t = e;
	int ans = 1;
	int bin[100];
	int x = 0;
	while (true)
	{
		bin[x++] = t % 2;
		t /=2;
		if (t == 0)
			break;
	}
	for (int i = x-1; i >= 0; i--)
	{
		ans = (ans*ans)% m;
		if (bin[i] == 1)
			ans = (ans*b)%m;
	}
	return ans;
}

int C(const int &n, const int &r)
{
	if (r == 0 || r == n)
		return 1;
	if (r == 1 || r == n-1)
		return n%1000;
	if (n == 1)
	{
		return 1;
	}
	if (n == 2)
	{
		if (r == 0)
			return 1;
		if (r==1)
			return 2;
		if (r == 2)
			return 1;
	}



	return (C(n-1,r)+C(n-1,r-1))%1000;
}


int calc()
{
	int ans = 0;
	for (int i = 0; i <= n; i+=2)
	{
		int t1 = expmod(5, i/2, 1000);
		int t2 = expmod(3, (n-i), 1000);
		int t3 = (t1*t2) % 1000;
		t3 = (t3*C(n,i)) % 1000;
		ans = (ans+t3) % 1000;
	}
	return (ans*2-1) % 1000;
}


int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> n;
		cout << "Case #" << i+1 <<": ";
		cout.width(3);
		cout.fill('0');
		cout << calc() << endl;
	}
}
