#include <iostream>
using std::cin;
using std::cout;
using std::cerr;

int f(int x)
{
	int r=0;
	for(int i = 0; i < x;i++)
	{
		r<<=1;
		r|=1;
	}
	return r;
}

int main()
{
	int c;
	cin >> c;
	for(int i = 0; i < c; i++)
	{
		int n, k;
		cin >> n >> k;
	//	cerr << n << ' ' << k << "\n";
		int r = k% (1 << n);
	//	cerr << n << ' ' << f(n) << ' ' << r << "\n";
		cout << "Case #" << (i+1) << ": " << (f(n) == r ? "ON" : "OFF") << "\n";
	}
	return 0;
}
