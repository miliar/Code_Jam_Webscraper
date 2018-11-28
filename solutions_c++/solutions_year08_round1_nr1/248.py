#include <fstream>

using namespace std;

ifstream cin("data.in");
ofstream cout("data.out");

int n;
int x[1000];
int y[1000];

void init()
{
	cin >> n;
	for (int i = 0; i < n; i++)
		cin >> x[i];
	for (int i = 0; i < n; i++)
		cin >> y[i];
}

void sort()
{
	for (int i= 0; i < n; i++)
		for (int j = i+1; j < n; j++)
			if (x[i] > x[j])
			{
				int tmp = x[i];
				x[i] = x[j];
				x[j] = tmp;
			}
	for (int i= 0; i < n; i++)
		for (int j = i+1; j < n; j++)
			if (y[i] > y[j])
			{
				int tmp = y[i];
				y[i] = y[j];
				y[j] = tmp;
			}
}





int main()
{
	int T;
	cin >> T;
	for (int i = 0; i < T; i++)
	{
		init();
		sort();
		long long ans = 0;
		for (int j = 0; j < n; j++)
			ans += x[j]*y[n-1-j];
		cout << "Case #" << i+1 << ": " << ans << endl;
	}
}