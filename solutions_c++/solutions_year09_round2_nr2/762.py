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
		
		string anw = input;
		int res = next_permutation(anw.begin(),anw.end());
		if(!res)
		{
			sort(anw.begin(), anw.end());
			int zero = 0;
			for(int i = 0; i < anw.length();i++)
				if(anw[i] == '0') zero++;
			string res = "";
			res = anw[zero];
			zero ++;
			for(int i = 0; i < zero;i++)
				res+="0";
			
			for(int i = zero ;i < anw.length();i++)
				res+=anw[i];
			anw = res;
		}
			outf << "Case #"  << test+1 << ": " ;
			outf <<  anw << endl;
			//if (test != tests-1) outf << endl;
		
	}
	
	outf.close();
	return 0;
}
