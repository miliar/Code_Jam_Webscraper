#include <iostream>
#include <fstream>
#include <string.h>
#include <iomanip>

using namespace std;



int main(int argc, char ** argv)
{
	//cout << argv[2] << endl;
	fstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);
	int n, k, i, j, t;
	fin >> t;
	//cout << n << endl;
	for (i = 1;i <= t;i ++)
	{
		fin >> n >> k;
//		cout << n << " " << k << " " << ((1 << n )-1 )<<  " " << (j ^ k) << endl;		
		fout << "Case #" << i << ": ";
		j = (1 << n) - 1;
		if ((j ^ (j & k)) == 0)
			fout << "ON";
		else
			fout << "OFF";
		fout << endl;
		
	}
	fout.close();
	fin.close();
}
