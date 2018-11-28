#include <iostream>
#include <string>
#include <fstream>
#include <cstdio>
#include <cstdlib>
using namespace std;

void cycshift(string &num)
{
	int i, len = num.length();
	char leadingc = num[0];
	for(i = 0 ; i < len - 1; i++) {
		num[i] = num[i + 1];
	}
	num[len - 1] = leadingc;
}

int cycle(int x, int y)
{
	char strx[50],stry[50];
	sprintf(strx, "%d", x);
	sprintf(stry, "%d", y);
	
	string sx(strx);
	string sy(stry);
	
	if(sx.length() != sy.length()) return -1;
	
	int len = sx.length();
	for(; len > 0; len--) {
		if(sx == sy) return 0;
		cycshift(sy);
	}
	return -1;
}

int calc(int a, int b)
{
	int x, y, total = 0;
	for(x = a; x < b; x++)
	{
		for(y = x + 1; y <= b; y++)
		{
			if(cycle(x, y) == 0) total++;
			//cout << "total = " << total << endl;
		}
	}
	return total;
}


int main(int argc, char* argv[])
{
	if(argc != 2) {
		cout << "usage: ./recycle in-file" << endl;
		exit(0);
	}
	
	fstream fin(argv[1]);
	
	if(fin.is_open() == false) {
		perror("open");
		exit(0);
	}
	
	int i, ntest, A, B;
	fin >> ntest;
	for(i = 0; i < ntest; i++)
	{
		fin >> A >> B;
		//cout << "A = "<< A << ", B = " << B << endl;
		cout << "Case #" << i + 1 << ": " << calc(A, B) << endl;
	}
	
	return 0;
}

