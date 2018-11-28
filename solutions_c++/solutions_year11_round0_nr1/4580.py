// gcj.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int co,cb;
int o_idx,b_idx;
int O[100],B[100];
int T[100];
int nNum,oNum,bNum;

int _tmain(int argc, _TCHAR* argv[])
{
	int nCase;
	ifstream fin("sample.txt");
	ofstream fout("out.txt");

	fin >> nCase;
	for (int i=1;i<=nCase;++i){
		int _nNum;
		fin >> _nNum;
		nNum = oNum = bNum = 0;
		for (int j=0;j<_nNum;++j){
			string type;
			int num;
			fin >>type>>num;
			
			if(type == "O"){
				O[oNum++] = num;
				T[nNum++] = 0;
			}
			else{
				B[bNum++] = num;
				T[nNum++] = 1;
			}
		}
		
		o_idx = b_idx = 0;
		co = cb = 1;
		int ttime = 0;
		for (int j=0;j<nNum; ++j){
			if (T[j] == 0){
				int interval = abs(co - O[o_idx]) + 1;
				co = O[o_idx++];
				if(b_idx < bNum){
					int b_interval = abs(cb - B[b_idx]);
					if(b_interval > interval){
						b_interval = interval;
					}
					if(cb > B[b_idx]) cb -= b_interval;
					else cb += b_interval;
				}
				ttime += interval;
			}
			else{
				int interval = abs(cb - B[b_idx]) + 1;
				cb = B[b_idx++];
				if(o_idx < oNum){
					int o_interval = abs(co - O[o_idx]);
					if(o_interval > interval){
						o_interval = interval;
					}
					if(co > O[o_idx]) co -= o_interval;
					else co += o_interval;
				}
				ttime += interval;
			}
		}


		fout<<"Case #"<<i<<": "<<ttime<<endl;	
	}


	return 0;
}

