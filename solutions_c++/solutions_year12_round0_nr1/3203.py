#include <fstream>
#include <string>
using namespace std;

string s;

int v[27]={25, 8, 5, 19, 15, 3, 22, 24, 4, 21, 9, 7, 12, 2, 11, 18, 26, 20, 14, 23, 10, 16, 6, 13, 1, 17};

int main() {
	int n,i,t,l;
	ifstream f("input.in");
	ofstream g("output.out");
	f>>t;
	getline(f,s);
	for (l=1; l<=t; l++) {
		g<<"Case #"<<l<<": ";
		getline(f,s);
		for (i=0; i<s.length(); i++)
			if (s[i]!=' ')
				s[i]=v[(int)s[i]-97]+96;
		g<<s<<'\n';
	}
	
	g.close();
	return 0;
}
