#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<cmath>

using namespace std;
int main()
{

	int test = 0;

	std::ifstream ifs( "test.txt" );
	std::ofstream ofs( "output.txt" );

	ifs >> test;

	for(int k = 0; k < test; k++)
	{
		long long int n, m;
		ifs >> n >> m;
		long long int on = pow(2.0, (double)n) - 1;
		if(m % (on + 1) == on){
			ofs << "Case #" << k + 1 << ": " << "ON" << endl;
		} else {
			ofs << "Case #" << k + 1 << ": " << "OFF" << endl;
		}
	}
	return 0;
}