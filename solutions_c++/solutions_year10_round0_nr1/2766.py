#include <iostream>
#include <fstream>

using namespace std;

int main(int argc, char ** argv)
{
	ifstream fin("A-large.in");// A-small-attempt2.in
	ofstream fout("A-large.out");// A
	
	int T;
	fin >> T;
	
	for (int i = 1; i <= T; i++)
	{
		int N, K;
		fin >> N >> K;
		
		if (((K + 1 ) % (1 << N)) == 0)
		{
			
			fout << "Case #" << i << ": ON" << endl; 	
		}else
		{
			fout << "Case #" << i << ": OFF" << endl; 	
		}
	}
	
	return 0;	
}
