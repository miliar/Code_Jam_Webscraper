#include <iostream>
#include <vector>
using std::cin;
using std::cout;
using std::cerr;
using std::vector;

int f(int x, int y)
{
	if(x < y)
		return 1;
	return 0;
}

int main()
{
	int c;
	cin >> c;
	for(int i = 0; i < c; i++)
	{
		int n;
		cin >> n;
		vector <int> a(n);
		vector <int> b(n);
		for(int j =0; j < n; j++)
			cin >> a[j] >> b[j];

		int r=0;
		for(int j = 0; j < n; j++)
			for(int k = j+1; k < n; k++)
			{
				int a2 = f(a[j], a[k]);
				int b2 = f(b[j], b[k]);
				if(a2 != b2)
					r++;
			}
		cout << "Case #" << (i+1) << ": " << r << "\n";
	}
	return 0;
}
