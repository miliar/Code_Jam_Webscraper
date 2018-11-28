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


vector <vector<int > >m;
int n;
int good(int l,int  from)
{
	//int fl = 0;
	for (int i = from + 1;i < n; i++)
		if (m[l][i] == 1) return 0;
	return 1;
}
int main(void){
	//freopen("input.txt","rt",stdin);
	//freopen("output.txt","wt",stdout);
	inf.open("input.txt");
	outf.open("output.txt");
	int tests;
	inf >> tests;
	for(int test = 0; test < tests; test++)
	{
		m.clear();
		inf >> n;
		for (int y = 0; y < n; y++)
		{
			m.push_back(vector<int>(100));
			char cc;
			for (int x = 0; x < n; x++)
			{
				inf >> cc;
				m[y][x] = cc - '0';
			}

		}
		int anw = 0;
		for(int k = 0; k < n; k++)
		{
			int fl = 0;
			int zz ;
			//outf <<"SDSDF" << good(k,k) << endl;;
			if (good(k, k)) continue;
			for(int z = k + 1; z < n; z++)
				if (good(z, k)) 
				{
					//outf <<"SDSDF" <<z << ' ' << good(z,k) << endl;;
					zz = z;
					break;
				}
			for (int i = zz; i > k; i--)
			{
				anw++;
				swap(m[i], m[i-1]);
			}
			
		}


			outf << "Case #"  << test+1 << ": " ;
			outf <<  anw << endl;
		
	}
	
	outf.close();
	return 0;
}
