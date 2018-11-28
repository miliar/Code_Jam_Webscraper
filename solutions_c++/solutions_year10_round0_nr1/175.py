#include<cstdio>
#include<cmath>
#include<fstream>
#include<iostream>
using namespace std;

int main(){
	ifstream fin("input.txt");
	ofstream fout("output.txt" );
	
	int T;
	int N, K;
	fin >> T;
	int i, j;
	bool flag;
	for(i = 0; i < T; ++i)
	{
		fin >> N >> K;
		flag = true;
		for(j = 0; j < N; ++j)
		{
			if((K % (1 << (j+1))) < (1 << j))
			{
				flag = false;
				break;
			}
		}
		if(flag)
		{
			fout << "Case #" << i+1 << ": ON" << endl;

		}
		else
		{
			fout << "Case #" << i+1 << ": OFF" << endl;
		}
	}

	fin.close();
	fout.close();
	return 0;
}