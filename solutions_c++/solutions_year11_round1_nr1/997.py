#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ofstream outf;
	outf.open("1.out",ios::out);
	int t;
	int k;
	cin >> t;
	int i,j,p;
	for (k = 1;k <= t;k++)
	{
		int pd,pg;
		double n;
		cin >> n >> pd >> pg;
		if ((pg == 100 && pd < 100) || (pd > 0 && pg == 0))
		{
			outf << "Case #" << k <<": Broken"<<endl;
			continue;
		}
		for (i = 100;i >= 1;i--)
		{
			if (100 % i == 0 && pd % i == 0)
				break;
		}
		if ((double)(100/i) > n)
			outf << "Case #" << k <<": Broken"<<endl;
		else
			outf << "Case #" << k <<": Possible"<<endl;
	}
	return 0;
}
