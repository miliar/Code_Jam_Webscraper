#include <iostream>
#include <fstream>
#include <vector>
#include <queue>
#include <stack>
#include <list>
#include <map>
#include <math.h>

using namespace std;

const long long MAX=100000010;
int T;
fstream	fin;
fstream fout;
int N;
long long K;

void main()
{
	fin.open("z:\\input.txt", ifstream::in);
	fout.open("z:\\output.txt", ifstream::out);


	fin >> T;

	for(int t = 1; t <= T; t++) {
		fin >> N >> K;
		
		int i;
		for(i=0; K & 0x1; i++)
			K >>= 1;
		if(i>=N)
			fout << "Case #" << t <<": ON" << endl;
		else
			fout << "Case #" << t <<": OFF" << endl;
	}

	fin.close();
	fout.close();
}