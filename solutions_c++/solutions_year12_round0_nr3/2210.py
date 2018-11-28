#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

typedef vector<int> vi;

int str2int(const string &s) {
	int res = 0;
	for (int i=0; i<s.size(); i++) {
		res *= 10;
		res += int(s[i] - '0');
	}
	return res;
}

string int2str(int n) {
	string res = "";
	while (n) {
		res += char(n%10 + '0');
		n /= 10;
	}
	reverse (res.begin(), res.end());
	return res;
}

int size(const int &n) {
	int pot=1, res=0;
	while (pot <= n) {
		res++;
		pot *= 10;
	}
	return res;
}

void rotate(string &s) {
	int size = s.size();
	string res = "";
	res += s[size-1];
	for (int i=0; i<size-1; i++) {
		res += s[i];
	}
	s = res;
}

int main() {
	ios_base::sync_with_stdio(0);

	int t;
	cin>>t;
	for(int k=1; k<=t; k++) {
		int a,b;
		cin>>a>>b;
		int s = size(a);
//		cout<<s<<endl;
		int count = 0;
		for (int i=a; i<=b; i++) {
//		cout<<i<<endl;
			vi tab;
			string n = int2str(i);
			for (int l=0; l<s; l++) {
				rotate(n);
				int k = str2int(n);
				bool bylo = false;
				for (vi::iterator it = tab.begin(); it != tab.end() && !bylo; it++) {
					if ((*it) == k) bylo = true;
				}
				if (k > i && k <= b && !bylo) {
					count++;
					tab.push_back(k);
				}
			}
		}
		cout<<"Case #"<<k<<": "<<count<<"\n";
	}

	return 0;
}
