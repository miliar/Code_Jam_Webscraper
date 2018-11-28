// 
// Author:	G2 (Jit Ray Chowdhury)
//jit.ray.c@gmail.com
// Created on July 27, 2008, 2:30 PM
//For Google Code Jam Round 1 C
//problem A

#include <stdlib.h>

#include <iostream>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <vector>
#include <list>
#include <string>
#include <cmath>

using namespace std;

typedef long long LL;
typedef vector<int> VI;
typedef vector<LL> VLL;
typedef vector<VI> VVI;
typedef vector<string> VS;

LL s2i(string s) { istringstream i(s); LL x; i>>x; return x; }
template<class T> string i2s(T x) { ostringstream o; o << x; return o.str(); }
//
// 
//
int main(int argc, char** argv) {
    ifstream fin("inputA.txt");
	ofstream fout("outputA.txt");

	int CN, cn, S;
LL nEach,nkey,nLet,fKey[1001],R,mull=1;
	fin >> CN;

	for (cn = 1; cn <= CN; ++cn) {

		fin >> nEach>>nkey>>nLet ;//normal input of no.
		 //getline(fin,tmp);S=atoi(tmp.c_str());//line input to int
//g2's_coode start
for(LL i=0;i<nLet;i++)
{
       fin>>fKey[i];
       }
       sort(fKey,fKey+nLet);
       R=0;
       mull=1  ;
       for(LL i=nLet-1,l=1;i>=0;i--,l++)
       {
       cout<<mull*fKey[i]<<" ";
       R=R+mull*fKey[i];
       if((l)%nkey==0){mull++;cout<<"i="<<l<<" ";}
       }
       

//g2's_coode endt
		//debug output
		cout << "Case #" << cn << ": " << R << '\n';
		//final output
		fout << "Case #" << cn << ": " << R<< '\n';
	}
	system("pause");
    return (EXIT_SUCCESS);
}

