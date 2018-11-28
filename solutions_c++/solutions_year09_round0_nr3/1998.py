#include<iostream>
#include<string>

using namespace std;
long n,x,y,l[30][1000],ans;;
string str="welcome to code jam";

int main() {
	string s;
	cin >> n;
	getline(cin,s);
	for (int i=0;i<n;i++) {
		getline(cin,s);
		for (int j=0;j<30;j++) {
			for (int k=0;k<1000;k++) {
				l[j][k]=0;
			}
		}
		ans=0;
		for (int j=0;j<str.length();j++) {
			if (s[j]==str[0]) {
				l[0][j]=1;
			}
		}
		for (int j=0;j<str.length()-1;j++) {
			int curr=0;
			for (int k=0;k<s.length();k++) {
				if (s[k]==str[j]) {
					curr=(l[j][k]+curr)%10000;
				}
				if (s[k]==str[j+1]) {
					l[j+1][k]=(l[j+1][k]+curr)%10000;
				}
			}
		}
		for (int j=0;j<s.length();j++) {
			ans=(ans+l[str.length()-1][j])%10000;
		}
		cout << endl;
		printf("Case #%ld: %04ld\n",i+1,ans);
	}
	return 0;
}

			


