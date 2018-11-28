#include <iostream>
#include <fstream>
#include <string.h>
#include <iomanip>

using namespace std;

const char * msg = "welcome to code jam";
const int maxlen = 600;
const int base = 10000;
int main(int argc, char ** argv)
{
	//cout << argv[2] << endl;
	fstream fin;
	ofstream fout;
	fin.open(argv[1]);
	fout.open(argv[2]);
	
	char s[maxlen];
	int len = strlen(msg), slen;
	int t[len];
	int i,j,k,n;
	fin >> n;
	fin.getline(s,100);
	//cout << n << endl;
	for (i = 1;i <= n;i ++)
	{
		memset(t,0,sizeof(t));
		fin.getline(s, 700);
		slen = strlen(s);
		//cout << s << " " << slen <<  " " << len << endl;
		for (j = 0;j < slen;j ++) {
			for (k = len-1;k >=1;k --) {
				if (s[j] == msg[k]) {
					t[k] += t[k - 1];
					t[k] = t[k] % base;
				}
				//cout << k << " " << t[k] << " ";
			}
			if (s[j] == msg[0]) {
				t[0] = t[0] + 1;
				t[0] = t[0] % base;
			}
			//cout << t[0] <<endl;
		}
		fout.fill('0');
		fout.width(4);
		fout << "Case #" << i << ": ";
		if (t[len-1] < 1000) fout << 0;
		if (t[len-1] < 100) fout << 0;
		if (t[len-1] < 10) fout << 0;
		fout  <<t[len-1]<<endl;
		
	}
	fout.close();
	fin.close();
}
