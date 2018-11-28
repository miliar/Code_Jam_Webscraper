#include <iostream>
#include <fstream>
#include <string>
#include <vector>
using namespace std;

int match(const string &d, const string &s)
{
	int p=0;
	int L = d.size();
	for (int k=0;k<L;k++) {
		char c = d[k];
		if (s[p]==c) {
			p++;
			continue;
		} else if (s[p]=='(') {
			p++;
			int f=0;
			while(s[p]!=')') {
				if (s[p++]==c) f=1;
			}
			p++;
			if (f==0) return 0;
		} else {
			return 0;
		}
	}

	return 1;
}

int main()
{
	int L,D,N;

	ifstream cin( "A-large.in" );

	cin >> L >> D >> N;

	string s;
	vector<string> dic;

	for (int i=0;i<D;i++) {
		cin >> s;
		dic.push_back(s);
	}

	for (int i=0;i<N;i++) {
		cin >> s;
		int count = 0;
		int p=0;
		for (int j=0;j<D;j++) {
			count += match(dic[j],s);
		}

		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}

