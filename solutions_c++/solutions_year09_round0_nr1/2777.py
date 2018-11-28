#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main ()
{
	
	int l, d, n, count=0, k=0, pos=0;
	bool b=true, isW=true, isL=false, abre;
	string word[5000], pat;
	ifstream fin ("A-large.in");
	ofstream fout ("A-large.out");
	
	fin>> l;
	fin>> d;
	fin>> n;
	for (int i=0; i<d; i++) fin>>word[i];
	
	for (int i=0; i<n; i++) {
		fin>> pat;
		count = 0;
		
		for (int j=0; j<d; j++) {
			b = true;
			k = 0;
			pos = 0;
			abre = false;
			while ((b) && (k < l)) {
				if (pat[pos] == '(') abre=true; 
				else {
					if (pat[pos] == ')') {
						abre = false;
						if (isL) k++;
						else b = false;
						isL=false;
					}
					else {
						if (abre) {if (pat[pos] == word[j][k]) isL=true;}
						else {
							if (pat[pos] != word[j][k]) b=false;
							else k++;
						}
					}
				}
				pos++;
			}
			if (b) count++;
		}
		fout<< "Case #"<<i+1<<": "<<count<<'\n';
	}

	fin.close();
	fout.close();
	
	return 0;

}
