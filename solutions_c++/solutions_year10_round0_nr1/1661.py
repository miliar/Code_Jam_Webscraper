#include <iostream>
#include <fstream>

using namespace std;

ifstream fin;
ofstream fout;

int main()
{
	unsigned int N, K, total, i, n, j;
	unsigned int tmp;
	
	//char res[2][30], str, on[2][30];
	
	//char* str = "ON";
	
	fin.open("A-small.in");
	fout.open("A.out");
	
	fin >> total;
	
	cout << "total: " << total << endl;
	
	for(n = 0; n < total; n ++)
	{
	
		fin >> N >> K;
	//	cout << "N = " << N << ", K = " << K << " ";
		tmp = 1;
		tmp = (tmp << N);
	//	cout << "tmp = " << tmp << ", (K + 1) % tmp " << (K + 1) % tmp << " ";
		
		if((K + 1) % tmp)
		{
			cout << "OFF" << endl ;
			fout << "Case #" << n + 1 << ": OFF" << endl;
		}
		else {
			cout << "ON" << endl;
			fout << "Case #" << n + 1 << ": ON" << endl;
		}
		
	}
}
