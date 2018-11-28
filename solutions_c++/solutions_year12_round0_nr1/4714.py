#include <iostream>
#include <string>
using namespace std;

string in="ejp mysljylc kd kxveddknmc re jsicpdrysi rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd de kr kd eoya kw aej tysr re ujdr lkgc jv zq";
string out="our language is impossible to understand there are twenty six factorial possibilities so it is okay if you want to just give up qz";

int main() {
	int N; cin >> N;
	cin.ignore();
	for (int I=0; I<N; ++I) {
		cout << "Case #" << I+1 << ": ";
		string str;
		getline(cin, str);
		for(int j=0; j<(int)str.size(); ++j) {
			int k=0;
			for(; k<(int)in.size(); ++k)
				if (str[j]==in[k])
					break;
			cout << out[k];
		}
		cout << endl;
	}
}
