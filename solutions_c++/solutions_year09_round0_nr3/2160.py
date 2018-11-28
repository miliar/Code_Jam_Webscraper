#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <strstream>
#include <vector>
#include <list>
#include <string>
#include <map>

using namespace std;

#define VAR(i,v) __typeof((v))i=(v)
#define FOREACH(i,v) for(VAR(i,(v).begin());i!=(v).end();i++)

vector<long> cnt;

string pat("welcome to code jam");

void setCount() {
	cnt.resize(0,0);
	cnt.resize(pat.length()+1, 0);
	cnt[0] = 1;
}

map<char, list<int> > letters;

void setLetters() {
	for (int i=0; i<pat.length(); i++) {
		char c = pat[i];
		letters[c].push_back(i+1);
	}
}

int main(int argc, char* argv[]) {

	if (argc<2) {
		printf("podaj nazwe pliku\n");
		exit(1);
	}

	setLetters();

	char buf[2048];
	ifstream fin(argv[1]);
	istrstream nStr(buf, 2048);
	int N=0;

	fin.getline(buf, 2048);

	nStr >> N;

	int check_pos = pat.length();

	for (int n=1; n<=N; n++) {
		fin.getline(buf, 2048);
		setCount();
		int i=0;
		
		while (buf[i]!=0) {
			char c = buf[i];
			map<char, list<int> >::iterator iter = letters.find(c);
			i++;
			if (iter!=letters.end()) {
				FOREACH(p,iter->second) {
					cnt[*p] += cnt[*p-1];
					cnt[*p] %= 10000;
				}

/*cout << buf << " == [ " << c << " ";

			int j=0;
			FOREACH(x,cnt) {
				char cc = (j==0) ? '-' : pat[j-1];
				j++;
				cout << "("<< cc << ")" << *x << ", "; 
			}
			cout << "]" << endl;*/
			}

		}
/*		cout << buf << " == [ ";
		FOREACH(x,cnt) cout << *x << ", ";
		cout << "] == " ;*/
		printf("Case #%d: %04d\n", n, cnt[check_pos]);
	}

	return 0;
}

