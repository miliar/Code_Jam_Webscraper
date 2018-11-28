#include<iostream>
#include<fstream>
#include<string>
#include<vector>
using namespace std;

int main()
{
	int T;
	int N;
	ifstream fin("C-large.in");
	fin>>T;
	ofstream fout("C-large.out");
	std::vector<int> V;
	int temp;
	int min;
	int sum;
	int realsum;
	for(int i = 0; i < T; i++)
	{
		V.clear();
		fin>>N;
		for(int j = 0; j < N; j++)
		{
			fin>>temp;
			V.push_back(temp);
			if(j == 0)
			{
				sum = temp;
				min = temp;
				realsum = temp;
			}
			else
			{
				sum = sum^temp;
				realsum += temp;
				if(min > temp)
				{
					min = temp;
				}
			}
		}
		fout<<"Case #"<<i+1<<": ";
		if(sum == 0)
		{
			fout<<realsum - min<<"\n";
		}
		else
		{
			fout<<"NO\n";
		}
	}
	return 0;
}