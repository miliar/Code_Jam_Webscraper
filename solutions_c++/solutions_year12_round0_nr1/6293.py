#include<iostream>
#include<fstream>
#include<string>
using namespace std;

char map[26]={'y','h','e','s','o','c','v','x','d','u','i','g','l','b','k','r','z','t','n','w','j','p','f','m','a','q'};

int main(int argc, char *argv[]) {
	ifstream in(argv[1]);
	ofstream out("out.txt");
	int T, len;
    char c;
	in >> T;
    in.get(c);
    char s[101];
	for (int i=1; i <= T; i++) {
		in.getline(s, 101);
		len = strlen(s);
		for (int j = 0; j < len; j++) {
			if (isalpha(s[j]))
				s[j] = map[s[j]-'a'];
		}
		out << "Case #" << i << ": " << s << endl;
	}
	return 0;
}