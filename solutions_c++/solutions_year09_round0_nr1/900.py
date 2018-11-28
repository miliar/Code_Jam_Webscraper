#include <map>
#include <algorithm>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string>
#include <vector>
#include <set>
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
	
	int l,d,tests;
	inf >> l >> d >> tests;
	inf.getline(tmpb, 100000);
	vector <string> words;
	for (int i = 0; i < d; i++)
	{
		inf.getline(tmpb, 100000);
		words.push_back(tmpb);
		
	}


	for(int test = 0; test < tests; test++)
	{
		string pattern;
		inf.getline(tmpb, 100000);
		pattern = tmpb;
		vector <set<int> > vs;
		vs.assign(l,  set<int>());
		int pos = 0;
		int next = 1;
		for(int i = 0; i < pattern.length(); i++)
		{
			if ((pattern[i]) == '(' )
			{
				next = 0;
				continue;
			}
			if ((pattern[i]) == ')') 
			{
				pos++;
				next = 1;
				continue;
			}
			vs[pos].insert(pattern[i]);
			pos += next;
			
		}
		int anw = 0;
		for(int i = 0; i < d; i++)
		{
			int good = 1;
			for(int j = 0; j < l; j++)
				if (vs[j].find(words[i][j]) == vs[j].end()) 
				{
					good = 0;
					break;
				}
			anw += good;

		}
		outf << "Case #"  << test+1 << ": " << anw << endl;

	}
	
	outf.close();
	return 0;
}
