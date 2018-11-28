#include<iostream>
#include<fstream>
#include<iomanip>
#include<algorithm>
using namespace std;

const char *key = "welcome to code jam";
int len = strlen(key);
int d[32];

void add(int pos, int val) { d[pos] = (d[pos] + val) % 10000; }

int main(void)
{
	ifstream fin("C-large.in");
	ofstream fout("C-large.out");
	
	int t; fin >> t; fin.ignore(10, '\n');
	for (int ct=1; ct<=t; ++ct) {
		memset(d, 0, sizeof(d));
		
		char c;
		c = fin.get();
		while (c != '\n' && !fin.eof()) {
			if (c == key[0]) add(0, 1);
			for (int i=1; i<len; ++i)
				if (c == key[i])
					add(i, d[i-1]);
			c = fin.get();
		}
		fout << "Case #" << ct << ": " << setfill('0') << setw(4) << d[len-1] << endl;
	}
	
	return 0;
}
