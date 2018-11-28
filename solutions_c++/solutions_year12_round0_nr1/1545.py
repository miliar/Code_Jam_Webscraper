#include <iostream>
#include <sstream>
using namespace std;

int main(int ac, char* av[])
{
	// st char* m = "abcdefghijklmnopqrstuvwxyz";
	const char* m = "yhesocvxduiglbkrztnwjpfmaq";
	char t[32];
	cin.getline(t, 32);
	stringstream ss(t);
	int N=3;
	ss >> N;
	for (int i=1; i<=N; i++) {
		char s[101], r[101];
		cin.getline(s, 101);
		char* rp = r;
		for(char* sp = s; *sp; ++sp, ++rp) {
			if (*sp == ' ') {
				*rp = ' ';
			} else {
				*rp = m[*sp-'a'];
			}
		}
		*rp = 0;
		cout << "Case #" << i << ": " << r << endl;
	}
	return 0;
}
