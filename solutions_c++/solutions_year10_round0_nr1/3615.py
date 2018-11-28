#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;


int main ()
{
	string line;
	ifstream testfile;
	ofstream result;
	result.open("C:\\Users\\Allan Yu\\Desktop\\output.txt");
	testfile.open("C:\\Users\\Allan Yu\\Desktop\\A-large.in");

	int CaseNo;
	testfile >>CaseNo;
	int nCase[30];
	nCase[0] = 2;
	for(int f = 1; f < 30; f++)
		nCase[f] = nCase[f-1] * 2;
	for(int i = 0; i < CaseNo;i++)
	{
		int N;
		testfile >>N;
		int K;
		testfile >>K;

		K += 1;
		bool bOpen = true;
		int k = K%nCase[N-1];
		if(k == 0)
			bOpen = 1;
		else
			bOpen = 0;

		result<<"Case #"<<i+1<<": ";
		if (bOpen)
		{
			result<<"ON"<<endl;
		}
		else
		{
			result<<"OFF"<<endl;
		}
	}
}