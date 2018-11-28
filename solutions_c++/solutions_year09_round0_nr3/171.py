#include <cstdio>
#include <cstring>
#include <string>
#include <iostream>
using namespace std;

string b = "welcome to code jam";

int la, lb = 19;
string a;
int f[1000][20];

void init() {
	getline(cin,a); 
	la = a.length();
}

void work() {
	memset(f, 0, sizeof(f));
	for (int i=0;i<=la;i++) f[i][0] = 1;
	for (int i=1;i<=la;i++)
		for (int j=1;j<=lb;j++) {
			if (a[i-1]==b[j-1])
				f[i][j] = (f[i-1][j-1]+f[i-1][j])%10000;
			else
				f[i][j] = f[i-1][j];
		}
	printf("%04d\n", f[la][lb]);
}

int main() {
	freopen("c.in","r",stdin);
	freopen("c.out","w",stdout);
	int T;
	cin>>T;
	getline(cin,a);
	for (int ti=1;ti<=T;ti++) {
		cout<<"Case #"<<ti<<": ";
		init();
		work();
	}
	return 0;
}
