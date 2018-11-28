#include <iostream>
#include <fstream>
using namespace std;
int main()
{
	int T;
	int N;
	int temp;
	int sum;
	ifstream fin;
	ofstream fout;
	fin.open("D-large.in");
	fout.open("Dlarge.txt");
	fin>>T;
	for (int i=1;i<=T;i++)
	{
		fin>>N;
		sum=0;
		for (int j=1;j<=N;j++)
		{
			fin>>temp;
			if (j!=temp)
			{
				sum++;
			}
		}
		fout<<"Case #"<<i<<": "<<sum<<endl;
	}
	return 0;
}
