#include<fstream>
#include<cstring>
#include<iostream>
using namespace std;

int main()
{
	int l, d, n;
	int i, j, k, t;
	int ans;
	bool match, pass;
	string str[5001];
	string s;
	fstream inf("a.in");
	ofstream ouf("a.out");
	inf>>l>>d>>n;
	for (i = 0; i < d; i++)
		inf>>str[i];
	for (i = 0; i < n; i++) {
		inf>>s;
		ans = 0;
		for (j = 0; j < d; j++) {
			pass = true; t = 0;
			for (k = 0; k < l; k++) {
				match = false;
				if (s[t] == '(') {
					while (s[t] != ')') {
						t ++;
						if (s[t] == str[j][k]) match = true;
					}
				}
				else {
					if (s[t] == str[j][k]) 
						match = true;				
				}
				t ++;
				if (!match) {
					pass = false;
					break;
				}
			}
			if (pass) ans ++;
		}
		ouf<<"Case #"<<i+1<<": "<<ans<<endl;
	}
	inf.close();
	ouf.close();
}