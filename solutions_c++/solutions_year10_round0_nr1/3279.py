#include <fstream>
#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;
int main()
	{
ifstream inf("A-large.in");
ofstream ouf("A-large.out");
int T;
inf >> T;
for(int i=0;i<T;i++)
	{
	int N,K;
	inf >> N >> K;
	int tmp=(int)pow(2.0,N);
	char* ret=(tmp-1==K%tmp)?"ON":"OFF";	
	ouf << "Case #" << (i+1) <<": " << ret << endl;
	}
	}