#include <iostream>
#include <fstream>
using namespace std;

int main () {
	ifstream in ("asmall.in");
	ofstream out ("asmall.out");
	int t;
	char io [300];
	string str;
	in >> t;
	in.get (io[0]);
	char map [180];
	for (int c = 'a'; c <= 'z'; ++c)
		map [c] = 0;
	string plain, cipher;
	plain = "our language is impossible to understand";
	cipher = "ejp mysljylc kd kxveddknmc re jsicpdrysi";
	for (int c= 0;c != cipher.size (); ++c)
		map[cipher[c]] = plain[c];
	plain = "there are twenty six factorial possibilities";
	cipher = "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd";
	for (int c= 0;c != cipher.size (); ++c)
		map[cipher[c]] = plain[c];
	plain = "so it is okay if you want to just give up";
	cipher = "de kr kd eoya kw aej tysr re ujdr lkgc jv";
	for (int c= 0;c !=cipher.size (); ++c)
		map[cipher[c]] = plain[c];
	map ['q'] = 'z';
	map['z'] = 'q';
	for (int c= 'a'; c <= 'z'; ++c)
		cout << ((map[c] == 0)?'?' : map[c]);
	for (int c= 0;c != t; ++c) {
		in.getline (io, 110, '\n');
		str = io;
		out << "Case #" << c+1 << ": ";
		for (int d = 0; d != str.size (); ++d)
			out <<  map [str[d]];
		out << endl;
	}
}
