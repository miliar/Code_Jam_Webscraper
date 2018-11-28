#include <cstdio>
#include <cstring>
#include <iostream>
#include <string>
using namespace std;

const int MAXD = 5100;
int ok[20][30];
int L, D, N;
string word[MAXD];

void init() {
	memset(ok, 0, sizeof(ok));
	char c;
	for (int i=0;i<L;i++) {
		cin>>c;
		if (c == '(') {
			do {
				cin>>c;
				if (c == ')') break;
				ok[i][c-'a'] = 1;
			} while(1);
		} else ok[i][c-'a'] = 1;
	}
}

void work() {
	int ans = 0;
	for (int i=0;i<D;i++) {
		int flag = 1;
		for (int j=0;j<L;j++)
			if (!ok[j][word[i][j]-'a']) { flag = 0; break; }
		if (flag) ans ++;
	}
	cout<<ans<<endl;
}

int main() {
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	
	cin>>L>>D>>N;
	for (int i=0;i<D;i++)
		cin>>word[i];
	for (int ti=1;ti<=N;ti++) {
		cout<<"Case #"<<ti<<": ";
		init();
		work();
	}
	return 0;
}

