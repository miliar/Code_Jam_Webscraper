#include <iostream>
#include <fstream>
#define MAXL 16
#define MAXD 5001
#define MAXN 501
using namespace std;

ifstream fin("ailen2.in");
ofstream fout("ailen2.out");

int L, D, N;
string a[MAXD];

int main()
{
	fin >> L >> D >> N;
	getline(fin, a[0]);
	
	for (int i=1; i<=D; i++) {
		getline(fin, a[i]);
	}
	
	for (int i=1; i<=N; i++) {
		string s;
		getline(fin, s);
		int p = -1;
		bool inside = false;
		bool dd[MAXL][256];
		for (int k=0; k<MAXL; k++)
			for (int j=0; j<256; j++) dd[k][j] = false;
			
		for (int k=0; k<s.length(); k++) {
			if (s[k] == '(') {inside = true; p++;}
			else if (s[k] == ')') inside = false;
			else if (inside) dd[p][int(s[k])] = true;
			else dd[++p][int(s[k])] = true;
		}
		int count = D;
		for (int k=1; k<=D; k++)
			for (int j=0; j<L; j++)
				if (! dd[j][int(a[k][j])]) {
					count--;
					break;
				}
		fout << "Case #" << i << ": " << count << endl;
	}
	
	fin.close();
	fout.close();
	
//	fflush(stdin); cin.get();
}
