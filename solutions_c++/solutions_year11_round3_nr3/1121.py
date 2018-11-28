#include<iostream>
#include<fstream>
#include<string>
#include<vector>
#include<cmath>
using namespace std;
int T;
int N;
int L;
int H;

std::vector<int> Notes;

int Judge()
{
	bool Flag = false;
	for(int i = L; i <= H; i++ )
	{
		Flag = true;
		for(int j = 0; j < N; j++)
		{
			if(i%Notes[j] != 0 && Notes[j]%i != 0)
			{
				Flag = false;
				break;
			}
		}
		if(Flag)
			return i;
	}
	return -1;
}

int main()
{
	ifstream fin("C-small.in");
	ofstream fout("C-small-ans.out");
	fin>>T;
	int Flag;
	for(int i = 0; i < T; i++)
	{
		fin>>N>>L>>H;
		Notes.clear();
		Notes.resize(N);
		Flag = false;
		for(int j = 0; j < N; j++)
		{
			fin>>Notes[j];
		}
		Flag = Judge();
		fout<<"Case #"<<i+1<<": ";
		if( Flag == -1 )
		{
			fout<<"NO\n";
		}
		else
		{
			fout<<Flag<<"\n";
		}
	}
	fin.close();
	fout.close();
	return 0;
}

