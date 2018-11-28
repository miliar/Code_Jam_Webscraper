#include <iostream>
#include <fstream>

using namespace std;

int T,N,K;

bool check()
{
	int d=(1<<N);
	if (K%d==d-1)
		return true;
	return false;
}

int main()
{
	ofstream fout("A-large.out");
	ifstream fin("A-large.in");
	int i;
	fin >> T;
	for (i=0;i<T;i++)
	{
		fin >> N >> K;
		fout << "Case #" << i+1 << ": ";
		if (!check())
			fout << "OFF";
		else fout << "ON";
		fout << endl;
	}
	return 0;
}