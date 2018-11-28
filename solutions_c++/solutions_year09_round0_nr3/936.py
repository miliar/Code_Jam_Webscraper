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
		string welcome = "welcome to code jam";
		//memset(tmpb,sizeof(tmpb),0);
		inf.getline(tmpb, 100000);		
		string input = tmpb;
		memset(dp,sizeof(dp),0);
		if (input.length() < 10)
			input = "12345";
		input = string("Z") + input;
		for (int i = 1; i < input.length(); i++)
			for (int j = 0; j < welcome.length(); j++)
			{

				if (input[i] == welcome[j])
				{
					if (j > 0)
						dp[i][j] = (dp[i-1][j-1] + dp[i-1][j]) % modd;
					else 
						dp[i][j] = (1 + dp[i-1][j]) % modd ;
				}
				else 
					dp[i][j] = dp[i-1][j];
				//outf << i << " " << j << " "<< dp[i][j] << endl;

			}
		
			outf << "Case #"  << test+1 << ": ";
			int anw = dp[input.length()-1][welcome.length()-1] % modd;
			if (anw < 1000) outf << "0";
			if (anw < 100) outf << "0";
			if (anw < 10) outf << "0";
		    outf <<  anw << endl;
			//if (test != tests-1) outf << endl;
		
	}
	
	outf.close();
	return 0;
}
