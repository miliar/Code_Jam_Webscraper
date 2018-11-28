#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
using namespace std;
ifstream inf;
ofstream outf;
#define FOR(i,a,b) for(int _b=(b),i=(a);i<=_b;i++)
#define FORD(i,a,b) for(int _b=(b),i=(a);i>=_b;i--)

char tmpb[100000];
int dp [600][600];
const int modd = 10000;
int main(void){
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	
	int tests;
	inf >> tests;
	
	inf.getline(tmpb, 100000);	

	for(int test = 0; test < tests; test++)
	{
		inf.getline(tmpb, 100000);		
		string input = tmpb;
		long long anw = 0;
		long long base;
		
		
			map<char, int> ma;
			ma.clear();
			
			for(char c ='0'; c<='9';c++)
				ma[c] = -1;
			for(char c ='a'; c<='z';c++)
				ma[c] = -1;
			ma[input[0]] = 1;
			int zeroused = 0;
			base = 2;

			for(int i = 1; i < input.length();i++)
			{
				if (ma[input[i]] == -1)
				{
					if(!zeroused) {
						ma[input[i]] = 0;
						zeroused = 1;
					}
					else
					{						
						ma[input[i]] = base;
						base++;

					}

				}


			}
			// base - baza
			long long  dp = 1;
			anw = 0;
			for(int i = input.length() - 1; i >= 0; i--)
			{
				anw += dp*ma[input[i]];
				dp*=base;

			}


		
			outf << "Case #"  << test+1 << ": " ;
			outf <<  anw << endl;
			//if (test != tests-1) outf << endl;
		
	}
	
	outf.close();
	return 0;
}
