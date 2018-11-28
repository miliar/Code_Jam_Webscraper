#include<cstdio>
#include<fstream>
#include<iostream>
using namespace std;

int main()
{
	ifstream istr("plik.txt");
	ofstream ostr("out.txt");
	int t, n, k;
	istr >> t;
	for(int i = 1; i <= t; ++i)
	{
		istr >> n >> k;
		//ostr << n << " " << k << "\n";
		ostr << "Case #" << i << ": " << (!((k+1)&((1<<n)-1)) ? "ON" : "OFF") << "\n";
	}

	istr.close();
	ostr.close();
	return 0;
}