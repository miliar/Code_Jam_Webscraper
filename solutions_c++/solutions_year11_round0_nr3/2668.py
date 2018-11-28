#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	int T;
	fin>>T;
	for(int t = 1; t<=T; t++)
	{
		int N;
		fin >> N;
		int sum = 0, realsum = 0, min = 2000000;
		int curr;
		for(int n = 0; n <N; n++)
		{
			fin >> curr;
			sum = sum ^curr;
			realsum += curr;
			if(curr < min)
			{
				min = curr;
			}
		}
		fout << "Case #" << t << ": ";
		if(sum != 0)
		{
			fout << "NO" <<endl;
			continue;
		}
		else
		{
			fout << realsum - min <<endl;
		}
	}
	int x =  50^10;
	cout << x<<endl;
	return 0;
}