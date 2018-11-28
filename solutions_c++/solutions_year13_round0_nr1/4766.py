#include <iostream>
#include <cstdio>
#include <cstdlib>

using namespace std;

int tt;
string s[4],s1[4];
bool f1,f2;

void check(string s[4]) {
	for (int i=0;i<4;++i) {
		int c1=0,c2=0;
		for (int j=0;j<4;++j)
			c1+=(s[i][j]=='X'),c2+=(s[i][j]=='O');
		if (c1==4) f1=true;
		if (c2==4) f2=true;
	}
	for (int j=0;j<4;++j) {
		int c1=0,c2=0;
		for (int i=0;i<4;++i)
			c1+=(s[i][j]=='X'),c2+=(s[i][j]=='O');
		if (c1==4) f1=true;
		if (c2==4) f2=true;
	}
	int c1=0,c2=0;
	for (int i=0;i<4;++i)
		c1+=(s[i][i]=='X'),c2+=(s[i][i]=='O');
	if (c1==4) f1=true;
	if (c2==4) f2=true;
	c1=c2=0;
	for (int i=0;i<4;++i)
		c1+=(s[i][3-i]=='X'),c2+=(s[i][3-i]=='O');
	if (c1==4) f1=true;
	if (c2==4) f2=true;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);

	scanf("%d\n",&tt);
	for (int ii=1;ii<=tt;++ii) {
		int cnt=0;
		for (int i=0;i<4;++i) {
			cin >> s[i];
			s1[i]=s[i];
		}
		f1=false,f2=false;
		for (int i=0;i<4;++i)
			for (int j=0;j<4;++j) {
				if (s[i][j]=='T') s[i][j]='O';
				cnt+=(s[i][j]=='.');
			}
		for (int i=0;i<4;++i)
			for (int j=0;j<4;++j)
				if (s1[i][j]=='T') s1[i][j]='X';
		check(s);
		check(s1);
		printf("Case #%d: ",ii);
		if (f1 && !f2) cout << "X won\n";
		if (!f1 && f2) cout << "O won\n";
		if (!f1 && !f2 && cnt>0) cout << "Game has not completed\n";
		else if ((!f1 && !f2) || (f1 && f2)) cout << "Draw\n";
	}
}
