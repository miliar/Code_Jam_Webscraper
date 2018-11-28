#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <fstream>
using namespace std;
#define FOR(i,n) for(i=0;i<n;i++)
#define VI vector<int>
#define FORR(i,a,b) for(i=a;i<b;i++)
#define pb(a) push_back(a)

string ans(int r, int k) {
	string s = "";
	for(int i=0;i<k;i++) {
		s = char((r%10) + '0') + s;
		r /= 10;
	}
	return s;
}

int main() {
	int i,j,k,l,n,p,m,r,t;
	ifstream cin("C.in.txt");
	ofstream cout("C.out.txt");
	cin >> t;
	string S = "welcome to code jam";
	char *s = new char[1000];
	cin.getline(s,1);
	FORR(p,1,t+1) {
		
		cin.getline(s,1000); n = strlen(s);
		VI a(n,0),b(n,0);
		FOR(j,S.size()) {
			b = a;
			l = 0;
			a.clear(); a.resize(n,0);
			FORR(i, j, n) if (s[i] == S[j]) {
				//if (i) a[i] = a[i-1];
				if (!j) a[i]++; 
				   else
				FORR(k,j-1,i) if (s[k]==S[j-1]) a[i]+=b[k];
				a[i] %= 10000;
				l += a[i];
			}
		}
		cout << "Case #" << p << ": " << ans(l,4) << endl;
	}
	return 0;
}