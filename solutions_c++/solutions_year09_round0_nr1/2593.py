// A1.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include <iostream>
#include <fstream>
#include <cmath>
#include <string>
#include <vector>
#include <cstddef>

using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

const double pi=acos(-1.0);
const double eps=1e-11;

string al_str[5001],str_to_process;
size_t lc,rc;//left right column
size_t str_flag;
int flago[5001];
int flagc[5001];
int answer;
int L,D,N;


int main()
{
	fstream fin("A.in");
	fstream fout("A.txt");
	fin>>L>>D>>N;
	for(int Di=1;Di<=D;Di++)
	{
		fin>>al_str[Di];
	}
 	for(int Ni=1;Ni<=N;Ni++)
	{
		answer=0;
		for (Di =1;Di<=D;Di++)
		{
			flagc[Di]=1;
		}
		fin>>str_to_process;
		str_flag=0;
		for(int Li=1;Li<=L;Li++)
		{
			memset(flago,0,sizeof(flago));
			if(str_to_process.at(str_flag) != '(')
			{
				for(Di=1;Di<=D;Di++)
				{
					if(str_to_process.at(str_flag)==al_str[Di].at(Li-1)&&flagc[Di]==1)
					{
						flago[Di]=1;
					}
				}
				for(Di=1;Di<=D;Di++)
				{
					flagc[Di]=flago[Di];
				}
 				str_flag +=1;
			}
			else
			{
				str_flag +=1;
				while (str_to_process.at(str_flag) != ')')
				{
					for(Di=1;Di<=D;Di++)
					{
						if(str_to_process.at(str_flag)==al_str[Di].at(Li-1)&&flagc[Di]==1)
						{
							flago[Di]=1;
						}
					
					}
					str_flag +=1;
				}


				for(Di=1;Di<=D;Di++)
				{
					flagc[Di]=flago[Di];
				}
				str_flag +=1;
			}
		}
		for(Di=1;Di<=D;Di++)
		{
			answer += flagc[Di];
		}
		fout<<"Case #"<<Ni<<": "<<answer<<"\n";		
	}
	return 0;
}
