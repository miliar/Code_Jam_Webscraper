#include <fstream>
#include <string>
using namespace std;

string pad(int l) {
	string ret;
	do {
		ret=char(l%10+'0')+ret;
		l/=10;
	} while (l>0);
	for (;ret.length()<4;)ret='0'+ret;
	return ret;
}

int rec(int i, int j);

int N;
string in;
string f="welcome to code jam";

int main() {
	ifstream fin("cjc.in");
	ofstream fout("cjc.out");
	
	fin>>N;fin.get();
	for (int i = 0; i < N; i++) {
		getline(fin,in);
		fout << "Case #" << i+1<<": " << pad(rec(-1,0)) << "\n";
	}	
}

int rec(int i, int j) {
	if (j==f.length()) 
		return 1;
	if (i==in.length()) return 0;

	int ret=0;
	for (int k = i+1; k <in.length();k++)
		if (in[k]==f[j]) ret=(ret+rec(k,j+1))%10000;
	return ret;
}
