#include <iostream>
#include <fstream>
#include <vector>
#include <algorithm>
#include <string>
#include <iomanip>
#include <ios>
#include <functional>

using namespace std;
int main()
{
	ifstream ifs("A-large.in");
	ofstream ofs("A-large.out");
	
	if(ifs.is_open() && ofs.is_open())
	{
		int T;
		ifs>>T;
		int i=0;
		while(ifs.good() && i<T)
		{
			unsigned long long N, K, TwoPowerN;
			ifs>>N>>K;
			TwoPowerN = (long long)1<<N;
			bool isOn = K % TwoPowerN == TwoPowerN - 1;
			ofs<<"Case #"<<++i<<": "<<(isOn ? "ON" : "OFF")<<"\n";
		}
	}
	ifs.close();
	ofs.close();

	return 0;
}