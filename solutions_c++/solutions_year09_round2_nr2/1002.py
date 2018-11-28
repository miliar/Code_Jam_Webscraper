#include <fstream>
#include <algorithm>
#include <vector>
#include <string>

using namespace std;

int main ()
{

	ifstream fin("B-large.in");
	ofstream fout("B.large.out");
	int n, j, pos;
	bool b;
	char c;
	string s;
	vector <char> t;
	
	fin>> n;
	for (int i=0; i<n; i++) {
		fin>>s;
		t.clear();
		for (int k=0; k<s.length();k++) t.push_back (s[k]);	
		fout<<"Case #"<<i+1<<": ";
		if (next_permutation (t.begin(), t.end())) for (int k=0; k<s.length();k++) fout<<t[k];
		else {
			c = ' ';
			j = 0;
			sort (t.begin(), t.end());
			while ((c == ' ') && (j <= t.size()-1)){
				if (t[j] != '0') {c = t[j]; pos=j;}
				else j++;
			}
			fout<<t[pos]<<'0';
			for (int k=0; k<s.length();k++) if (k != pos) fout<<t[k];			
		}
		fout<<'\n';		
	}

	fin.close();
	fout.close();
	return 0;

}
