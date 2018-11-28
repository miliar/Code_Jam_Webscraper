// jam.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdlib>
#include <vector>
#include <iostream>
#include <fstream>

//namespace std;

int _tmain(int argc, _TCHAR* argv[])
{
	std::ifstream fp_in;
	std::ofstream fp_out;
	fp_in.open("d:\\jam\\in1.txt", std::ios::in);
	int T;
	fp_in >> T;
	std::vector<int> res;

	for (int cs=0; cs<T; cs++) {
		int N,K;
		fp_in >> N >> K;		
		char snips[30];
		for(int xx=0; xx<N; xx++)
			snips[xx]='0'; 
		
		for(int i=0; i<K; i++) {		
			for(int xx=0; xx<N; xx++) {
				if (snips[xx]=='0') {
					snips[xx]='1';
					break;
				}
				snips[xx]= '0';			
			}		
		}

		int lastpos = 0;
		for (int xx=0; xx<N; xx++) {
			if (snips[xx]=='0') 
				break;
			lastpos += 1;
		}
		res.push_back(lastpos==N);
	}
	fp_in.close();

	fp_out.open("d:\\jam\\out2.txt", std::ios::out);
	for(int cs=0; cs<T; cs++) {
		char *r = res[cs] ? "ON" : "OFF";
		fp_out << "Case #" << cs+1 << ": " << r << std::endl;
	}
	fp_out.close();

	return 0;
}

