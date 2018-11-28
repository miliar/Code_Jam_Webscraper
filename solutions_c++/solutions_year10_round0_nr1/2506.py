#include <fstream>
#include <cmath>
using namespace std;

int main()
{
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");
	int cases;
	fin>>cases;
	int tcase = 1;
	while(cases--)
	{
		int n,k;
		fin>>n>>k;
		int bb = pow(2,(double)n);
		if((k%bb) == (bb-1))
		{
			fout<<"Case #"<<tcase++<<": ON"<<endl;
		}
		else
		{
			fout<<"Case #"<<tcase++<<": OFF"<<endl;
		}
	}
	fin.close();
	fout.close();
	return 0;
}
