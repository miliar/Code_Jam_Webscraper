#include <iostream>
#include <string>
#include <set>
#include <map>
using namespace std;


int main()
{
	int N;
	cin >> N;
	string s;

	for (int i=0;i<N;i++) {
		cin >> s;
		set<char> b;
		for (int j=0;j<s.size();j++) {
			b.insert(s[j]);
		}
		int base = b.size();
		if (base<2) base=2;

		map<char,int> d;
		int k=0;
		for (int j=0;j<s.size();j++) {
			if (d.count(s[j])) continue;
			d[s[j]] = (k==0)?1:(k==1)?0:k;
			k++;
		}

		unsigned long long a=0;
		for (int j=0;j<s.size();j++) {
			a*=base;
			a+=d[s[j]];
		}

		cout << "Case #" << i+1 << ": "<< a << endl;
	}

	return 0;
}

