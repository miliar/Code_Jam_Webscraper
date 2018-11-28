#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int i, j, k, p;
	
	int cnt[3000] = {0};
	int d;
	char num[5];
	char tmp;
	int l;

	ifstream inf("1.in", ios::in);
	ofstream outf("1.out", ios::out);
	int t;
	inf >> t;
	int a, b;
	int sum;
	for (p = 1;p <= t;p++)
	{
		inf >> a >> b;
		sum = 0;
		for (i = a; i <= b; i++)
		{
			d = log((double)i)/log(10.0);
			itoa(i, num, 10);
			for (j = 0;j < d;j++)
			{
				tmp = num[0];
				for (k = 1; k <= d; k++)
					num[k-1] = num[k];
				num[d] = tmp;
				l = atoi(num); 
				if (l >= a && l < i && (int)(log((double)l)/log(10.0)) == d)
					sum ++;
			}
		}		
		outf << "Case #" << p << ": " << sum << endl;
	}

	inf.close();
	outf.close();

	return 0;
}