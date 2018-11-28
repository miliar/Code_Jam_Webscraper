#include <iostream>
#include <iomanip>
#include <fstream>
#include <string>
using namespace std;
int main()
{
	//========read in input==========//
	char* input = "e:\\A-large.in";
	ifstream fin;
	fin.open(input,ios_base::binary);
	//========create output=========//
	ofstream fout;
	fout.open("output_f2.txt", ios_base::binary);
	
	//==========begin here==========//
	int T;
	fin >> T;
	int  N = 0, K = 0;
	for(int k = 1; k <=T; k++)
	{
		fin >> N;
		fin >> K;
		fout<<"Case #" << k <<": ";
		int count = 0;
		while(K&1 == 1)
		{
			K = K >> 1;
			count ++;
		}
		if(N <= count)
		fout<< "ON"<<endl;
		else
		fout<<"OFF" <<endl;
	}
	return 0;
}