#include <iostream>
#include <fstream>
#include <list>

using namespace std;

void main()
{
	ifstream f("Input.txt");
	ofstream outFile("Output.txt");
	int T;
	f >> T;
	for(int i=0; i<T; i++)
	{
		int N;
		f >> N;
		list<int> seq;
		for(int j=0; j<N; j++)
		{
			int tmp;
			f >> tmp;
			seq.push_back(tmp);
		}
		seq.sort();
		list<int>::iterator it = seq.begin();
		int xorSum = *it;
		long total = 0;
		it++;
		for(; it != seq.end(); it++)
		{
			xorSum ^= *it;
			total += *it;
		}
		outFile << "Case #" << i+1 << ": ";
		if(xorSum != 0)
			outFile << "NO" << endl;
		else
			outFile << total << endl;
	}
	outFile.close();
	f.close();
}