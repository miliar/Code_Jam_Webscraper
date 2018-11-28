#include <cstdio>
#include <cstring>
#include <string>
#include <cstdlib>
#include <iostream>
#include <vector>

using namespace std;

int tasks;
string a;
string s = "welcome to code jam";

int f[600][20];

int calc(string a) {
	memset(f,0,sizeof(f));
	for (int i=0; i<s.length(); i++)
		for (int j=i; j<a.length(); j++) {
			if (j!=0)
				f[j][i] = f[j-1][i];
			if (a[j]==s[i]) {
				if (i==0)
					f[j][i] += 1;
				else
					f[j][i] += f[j-1][i-1];
			}
			f[j][i] = f[j][i]%10000;
		}

		/*for (int i=0; i<a.length(); i++){
			for (int j=0; j<s.length(); j++)
				cout << f[i][j] << " ";
			cout << endl;
		}*/
	return f[a.length()-1][s.length() - 1];
}

int main() {
	freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	cin >> tasks;
	getline(cin, a);
	for (int i=0; i<tasks; i++) {
		getline(cin, a);
		int ans = calc(a);
		cout << "Case #" << i+1 << ": ";
		if (ans/1000==0)
			cout << 0;
		if (ans/100==0)
			cout << 0;
		if (ans/10==0)
			cout << 0;
		cout << ans << endl;
	}
	return 0;
}