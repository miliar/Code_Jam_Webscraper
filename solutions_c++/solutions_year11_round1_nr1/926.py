#include <iostream>
#include <fstream>

using namespace std;

int gcd(int val)
{
	int de = 100;
	while(1)
	{
		val = val % de;
		if(!val)
			return de;
		de = de % val;
		if(!de)
			return val;
	}
}

int main()
{
	long long int n;
	int pd, pg;
	int case_num;
	ifstream ifile("A-large.in");
	ofstream ofile("A-large.out");
	ifile >> case_num;
	for(int i=0;i<case_num;++i)
	{
		bool res = false;
		ifile >> n >> pd >> pg;
		if((pg == 100 && pd != 100) || (pg == 0 && pd != 0))
			res = false;
		else
		{
			int min_win = 100 / gcd(pd);
			if((long long int)min_win <= n)
				res = true;
		}
		if(res)
			ofile << "Case #" << i+1 << ": Possible\n";
		else
			ofile << "Case #" << i+1 << ": Broken\n";
	}
	ifile.close();
	ofile.close();
	system("pause");
	return 0;
}

