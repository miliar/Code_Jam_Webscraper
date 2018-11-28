#include <iostream>
#include <cstdio>
#include <vector>
#include <cstring>
#include <fstream>

using namespace std;

#define ll long long

int main () {
	fstream cin("A-large.in");
	ofstream cout("output.txt");
	int T;
	cin>>T;
	for (int run=1;run<=T;++run) {
		int r,c;
		cin>>r>>c;
		char a[r+2][c+2];
		for (int i=0;i<=r+1;++i)
			for (int j=0;j<=c+1;++j)
				a[i][j] = '.';
				
		for (int i=1;i<=r;++i) {
			string str;
			cin>>str;
			for (int j=1;j<=c;++j) 
				a[i][j] = str[j-1];
		}	
		bool found = true;
		for (int i=1;i<r;++i) {
			for (int j=1;j<c;++j)
				if (a[i][j]=='#'&&a[i-1][j]!='#'&&a[i-1][j-1]!='#'&&a[i][j-1]!='#') {
					if (a[i][j+1]=='#' && a[i+1][j]=='#' && a[i+1][j+1]=='#') {
						a[i][j]='/';
						a[i][j+1]='\\';
						a[i+1][j]='\\';
						a[i+1][j+1]='/';
					}
					else {
						found = false;
						break;	
					}
				}
			if (!found) break;
		}
		cout<<"Case #"<<run<<":\n";
		if (!found) {
			cout<<"Impossible"<<endl;
		}
		else {
			for (int i=1;i<=r;++i) {
				for (int j=1;j<=c;++j)
					if (a[i][j]=='#') {
						found = false;
						break;	
					}
				if (!found) break;
			}
			if (!found) {
				cout<<"Impossible"<<endl;	
			}	
			else {
				for (int i=1;i<=r;++i) {
					for (int j=1;j<=c;++j)
						cout<<a[i][j];
					cout<<endl;	
				}
			}
		}
	}
	cin>>T;
	return 0;
}
