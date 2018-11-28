#include <iostream>
using std::cin;
using std::cout;
using std::endl;

bool a[60];
int n, k, t, b;

void workout()
{
	int x = 0, y = 0, g = 0;
	for(int i = n-1; i>=0; i--)
	{
		if(x >= k) break;
		if(a[i])
		{
			x ++;
			y += g;
		}
		else
		{
			g++;
		}
		//cout << "i=" << i << " x=" << x << " y=" << y << " g=" << g << endl;
	}
	if(x < k) cout << "IMPOSSIBLE" << endl;
	else cout << y << endl;
}

void workin()
{
	int x[60];
	int v[60];
	cin >> n >> k >> b >> t;
	//cout << "n=" << n << " k=" << k << " b=" << b << " t=" << t << endl;
	for(int i=0; i<n; i++)
	{
		cin >> x[i];
		//cout << x[i] << " ";
	}
	//cout << endl;
	for(int i=0; i<n; i++)
	{
		cin >> v[i];
		//cout << v[i] << " ";
	}
	//cout << endl;
	for(int i=0; i<n; i++)
	{
		//a[i] = (b - x[i])/v[i] <= t;
		a[i] = ((x[i] + t * v[i]) >= b);
		//cout << a[i] << " ";
	}
	//cout << endl;
}

int main()
{
	int t;
	cin >> t;
	for(int i = 1; i <= t; i++)
	{
		cout << "Case #" << i << ": ";
		workin();
		workout();
	}
	return 0;
}
