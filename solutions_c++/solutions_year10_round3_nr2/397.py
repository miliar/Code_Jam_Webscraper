#include <fstream>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string>
#include <sstream>
#include <map>
#include <hash_set>

using namespace std;

int main()
	{
	ifstream inf("B-large.in");
	ofstream ouf("A-small-attempt2.out");
	int T;
	inf >> T;
	for(int k=0;k<T;k++)
		{
		int L,P,C;
		inf >> L >> P >> C;
		int tmp=P;
		int lg=0;
		while(tmp>L)
			{
			if(tmp%C==0) tmp/=C; else tmp=tmp/C+1;
			if(tmp>L)lg++;
			}
		int ret=0;
		int lg2=1;
		while(lg2<=lg){ lg2<<=1;ret++;}
		ouf << "Case #" << (k+1) << ": " << ret << endl;
		}
	}