#include "stdafx.h"
#include <cstdlib>
#include <iostream>
#include <vector>
#include <fstream>
#include <string>
#include <map>
#include <algorithm>
#include <cstdio>
#include <stack>
#include <cmath>
#include <queue>
#include <istream>
#include <sstream>
#include <set>
using namespace std;
 
typedef vector < string > vs;
typedef vector <int> vi;
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)
#define deb(x) cout << #x << ": " << x << endl;
#define debv(x) for(int i = 0; i < (x).size(); i++) cout << x[i] << ' '; cout << endl; 

vs strsp(string c, string delim=" ")
{
	vs ret;
	string a = "";
	int p = 0;
	while(p < c.size())
	{
		while(p < c.size() && delim.find(c[p]) == string::npos ) { a += c[p++]; }
		if(a.size()) { ret.push_back(a); a = ""; }
	}
	return ret;
}	

int main()
{
	int T, ctest = 0;
	
	ofstream fout("bout.txt");
	ifstream fin("bin.txt");
	fin >> T;
	while(ctest++ < T)
	{
		int N;
		fin >> N;
		vs base(31,"");
		base[2] = "027";
		base[3] = "143";
		base[4] = "751";
		base[5] = "935";
		base[6] = "607";
		base[7] = "903";
		base[8] = "991";
		base[9] = "335";
		base[10] = "047";
		base[11] = "943";
		base[12] = "471";
		base[13] = "055";
		base[14] = "447";
		base[15] = "463";
		base[16] = "991";
		base[17] = "095";
		base[18] = "607";
		base[19] = "263";
		base[20] = "151";
		base[21] = "855";
		base[22] = "527";
		base[23] = "743";
		base[24] = "351";
		base[25] = "135";
		base[26] = "407";
		base[27] = "903";
		base[28] = "791";
		base[29] = "135";
		base[30] = "647";

		fout << "Case #" << ctest << ": " << base[N] << endl;
	}
	fin.close();
	fout.close();
	return 0;
}
		