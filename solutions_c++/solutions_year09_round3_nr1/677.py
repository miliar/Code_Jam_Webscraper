#include <fstream>
#include <string>
#include <cmath>
#include <iostream>

using namespace std;

int main () 
{

	ifstream fin ("A-small-attempt1.in");
	ofstream fout ("A-small.out");
	int t, c, pos, res;
	string s;
	int num[100];
	char car[100], temp;
	bool b;
	
	fin>> t;
	c=0;
	for (int i = 0; i<t; i++) {
		fin>> s;
		res=0;
		for (int k=0; k<c; k++) car[k] = ' ';
		c=0;
		for (int j=0; j<s.length(); j++) {
			temp = s[j];
			b = false;
			for (int k=0; k<j; k++) if (s[k] == temp) {b = true; pos = k;}
			if (not(b)) {
				car[c] = temp;
				c++;
			}
		}
		if (c == 1) c=2;
		//for (int k=0; k<c; k++) cout<<car[k]<<'\n';
		for (int j=0; j<s.length(); j++) {
			pos= 0; 
			for (int k=0; k<c; k++) if (s[j] == car[k]) pos = k;
			//cout<<pos<<'\n';
			if (pos == 0) res += pow(c,(s.length()-j-1));
			else if (pos >= 2) res += pos*(pow(c,(s.length()-j-1)));
		}
		fout<< "Case #"<<i+1<<": "<<res<<'\n';
	}

	fin.close();
	fout.close();
	return 0;

}
