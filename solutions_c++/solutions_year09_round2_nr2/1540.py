#include <algorithm>
#include <iostream>
#include <fstream>
#include <queue>

using namespace std;

int main()
{
	ifstream fin("next_number.in");
	ofstream fout("NextNumber.txt");
	
	int T;
	fin>>T;
	for(int test=1; test<=T; test++)
	{
		int N;
		fin>>N;
		deque<int> vi;
		while(N > 0)
		{
			vi.push_front(N%10);
			N/=10;
		}
		if(next_permutation(vi.begin(), vi.end()))
		{;
		}
		else
		{
			sort(vi.begin(), vi.end());
			vi.push_front(0);
			int ind=0;
			while(vi[ind] == 0)	ind++;
			swap(vi[ind],vi[0]);
		}
		fout<<"Case #"<<test<<": ";
		for(int i=0; i<vi.size(); i++)	fout<<vi[i];
		fout<<"\n";
	}
	return 0;
}
