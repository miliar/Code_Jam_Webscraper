#include <iostream>
#include <sstream>
#include <string>
using namespace std;

typedef long long LL;

char text[1000];
const char* str = "welcome to code jam";
int n,m;

string count() {
	static int tab[1000][50];
	for (int i=0; i<=n; ++i) {
		tab[i][m]=1;
	}
	for (int i=0; i<m; ++i) {
		tab[n][i]=0;
	}
	for (int i=n-1; i>=0; --i) {
		for (int j=m-1; j>=0; --j) {
			tab[i][j]=tab[i+1][j];
			if (text[i]==str[j]) {
				tab[i][j]+=tab[i+1][j+1];
				tab[i][j]%=10000;
			}
		}
	}
	ostringstream os;
	os<<(tab[0][0]+10000);
	string ans=os.str();
	return ans.substr(1);
}

int main() {
	int N;
	cin.getline(text,1000);
	N=atol(text);
	m=strlen(str);
	for (int i=0; i<N; ++i) {
		cin.getline(text,1000);
		n=strlen(text);
		cout<<"Case #"<<(i+1)<<": "<<count()<<endl;
	}
	return 0;
}
