#include <iostream>
#include <cstdio>
#include <string>
using namespace std;

char m[256];
string line;
int T;

void translating() {
	string S1, S2, S3, s1, s2, s3;
	
	s1 = "our language is impossible to understand";
	S1 = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	s2 = "there are twenty six factorial possibilities";
	S2 = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	s3 = "so it is okay if you want to just give up";
	S3 = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	
	for(int i=0; i<(int)S1.size(); i++)
		m[(int)S1[i]] = s1[i];
	for(int i=0; i<(int)S2.size(); i++)
		m[(int)S2[i]] = s2[i];
	for(int i=0; i<(int)S3.size(); i++)
		m[(int)S3[i]] = s3[i];
	
	m['q'] = 'z';
	m['z'] = 'q';
}

int main() {
	ios_base::sync_with_stdio(false);
	translating();
	
	cin >> T;
	cin.ignore();
	for(int t=1; t<=T; t++) {
		getline(cin, line);
		cout << "Case #" << t << ": ";
		for(int i=0; i<(int)line.size(); i++)
			cout << m[(int)line[i]];
		cout << "\n";
	}
	
	return 0;
}


