#include <iostream>
#include <fstream>
#include <iomanip>
using namespace std;
int main()
{
	ofstream outf;
	outf.open("1c3.out",ios::out);
	int t;
	int k;
	cin >> t;
	int i,j;
	for (k = 1;k <= t;k++)
	{
		outf << "Case #"<<k <<": ";
		int n,l,h;
		cin >> n >> l >> h;
		int note[100];
		for (i = 0; i < n;i++)
			cin >> note[i];
		int cnt;
		bool flag = true;
		for (i = l;i <= h;i++)
		{
			cnt = 0;
			for (j = 0;j < n;j++)
			{
				if (i % note[j] == 0 || note[j] % i == 0)
					cnt ++;
			}
			if (cnt == n)
			{
				outf << i <<endl;
				flag = false;
				break;
			}
		}
		if (flag)
			outf << "NO"<<endl;
	}
	return 0;
}
