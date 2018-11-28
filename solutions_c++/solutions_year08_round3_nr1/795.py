#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <stdio.h>
using namespace std;

#define FOR(a,b) for (a=0;a<b;a++)
#define FORD(a,b) for (a=b;a>=0;a--)
#define PI 3.141592653589


struct T_Letter {
	int nNum;
	int nFreq;
};
bool comp (const T_Letter &a,const T_Letter &b) {return a.nFreq>b.nFreq;}
vector<T_Letter> vLetters;

int main()
{
	int i,j,k;
	int num_cases;
	fstream fin,fout;

	fin.open ("A-small-attempt0.in", fstream::in);
	fout.open("A-small.out",fstream::out);

	fin >>num_cases;


	
	FOR(i,num_cases)
	{
		int j;
		int P,K,L;
		fin >>P>>K>>L;
		vLetters.clear();
		FOR(j,L)
		{
			T_Letter thisLetter;
			thisLetter.nNum=j;
			fin>>thisLetter.nFreq;
			vLetters.push_back(thisLetter);

		}

		sort(vLetters.begin(),vLetters.end(),comp);
		int nNumPresses=0;
		FOR(j,vLetters.size())
		{
			nNumPresses+=vLetters[j].nFreq*(1+(j/K));
		}

		fout << "Case #"<<i+1<<": "<<nNumPresses<<endl;
	}
	
	cin >>i;
}