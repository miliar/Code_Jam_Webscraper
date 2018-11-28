// iassad - Iyad Assad
// to solve Google code.jam Round 1 - Subround c - Problem b

#include <iostream>
#include <fstream>

using namespace std;

int main (int argc, char * argv[]) {
	int cases;
	char fn[200];

	if (argc < 2) {
		cout << endl << "Usage: " << endl << endl << argv[0] << " input-filename" << endl << endl;
		return 0;
	}

	ifstream fin(argv[1]);
	sprintf(fn,"%s.output",argv[1]);
	ofstream fout(fn);

	fin >> cases;

	for (int cn=1; cn<=cases; cn++) {
		char str[20];
		int s[20];

		for (int i=0; i<20; i++) {
			s[i] = 0;
			str[i] = 0;
		}

		fin >> str;

		long k, cnt=0;
		do {
			long long cnum=str[0]-'0', n=0, ls=0;
			for (int i=1; str[i]; i++) {
				if (s[i] == 0) {
					cnum*=10; 
					cnum+=str[i]-'0';
				} else {
					n += (ls==1?cnum:-cnum);
					ls = s[i];
					cnum=str[i]-'0';
				}
					
			}
			n += (ls==1?cnum:-cnum);

			if (((n%2)==0) || ((n%3)==0) || ((n%5)==0) || ((n%7)==0))
				cnt++;
			
			k=1;
			(s[k])++;
			while (s[k]==3) {
				s[k] = 0;
				k++;
				(s[k])++;
			}
		} while (k<strlen(str));

		fout << "Case #" << cn << ": " << cnt << endl;
	}

	fin.close();
	fout.close();
	
	return 0;
}
