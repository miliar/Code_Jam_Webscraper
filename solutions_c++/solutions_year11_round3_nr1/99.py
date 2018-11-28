#include <iostream>
#include <cstring>
#include <cctype>
#include <algorithm>
#include <map>
#include <string>
using namespace std;
typedef __int64 ll;
const int N=1100000;
int tests,t,r,c;
string s[100];
int main () {
#ifndef ONLINE_JUDGE
	freopen ("input.txt","r",stdin);
	freopen ("output.txt","w",stdout);
#endif
	cin>>tests;
	for (t=1; t<=tests; t++) {
		cin>>r>>c;
		for (int i=0; i<r; i++) 
			cin>>s[i];
		int ok=1;
		for (int i=0; i<r-1; i++)
			for (int j=0; j<c-1; j++)
				if (s[i][j]=='#' && s[i+1][j]=='#' && s[i+1][j+1]=='#' && s[i][j+1]=='#') {
					s[i][j]=s[i+1][j+1]='/';
					s[i+1][j]=s[i][j+1]='\\';
				}
		for (int i=0; i<r; i++)
			for (int j=0; j<c; j++)
				if (s[i][j]=='#') ok=0;
		cout<<"Case #"<<t<<":"<<endl;
		if (ok) {
			for (int i=0; i<r; i++)
				cout<<s[i]<<endl;
		} else cout<<"Impossible"<<endl;
	}
}