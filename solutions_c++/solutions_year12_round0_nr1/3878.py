#include <iostream>
#include <cstdio>

using namespace std;

char x[] = "zqejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv";
char y[] = "qzour language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up";

char convert(char op) {
	int i=0;
	while(x[i]!=op) ++i;
	return y[i];
}

int main() {
	int T;
	string s;
	cin>>T;
	getline(cin, s);
	for(int i=0; i<T; ++i) {
		getline(cin, s);
		for(int j=0; j<s.length(); ++j)
			s[j] = convert(s[j]);
		cout<<"Case #"<<(i+1)<<": "<<s<<endl;
	}
}
