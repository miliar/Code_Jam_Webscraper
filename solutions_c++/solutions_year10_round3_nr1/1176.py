#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <math.h>
#include <algorithm>
using namespace std;

#define VS vector<string>
#define VI vector<int>
#define LL long long
#define FOR(_a,_b,_c) for(int _a = _b; _a < _c; _a++)

int convert2dec(VI num, int base)
{
	int dec = 0;
	FOR(i,0,num.size())
	{
		dec = dec*base + num[i];
	}
	return dec;
}

bool isIntersect(int a1, int b1, int a2, int b2)
{	
	if((a1<a2 && b1>b2) || (a1>a2 && b1<b2))
		return 1;
	return 0;
}

int main()
{
	ifstream fin;
	ofstream fout;
	int T;
	string filename = "A-large";
	fin.open(filename+".in", ios_base::in);
	fout.open(filename+".out", ios_base::out);

	fin>>T;

	for(int i=1; i<=T; i++)
	{
		fout<<"Case #"<<i<<": ";
		VI A,B;
		int N,KQ=0;

		fin>>N;		
		for(int j=0; j<N; j++)
		{
			int a;
			fin>>a;
			A.push_back(a);
			fin>>a;
			B.push_back(a);

		}

		for(int j=0; j<N-1; j++)
		{
			for(int k=j+1; k<N; k++)
			{
				if(isIntersect(A[j],B[j], A[k], B[k]))
					KQ++;
			}
			
		}
		fout<<KQ;
		if(i<T)
			fout<<endl;
	}

	fin.close();
	fout.close();	
	
	return 0;
}