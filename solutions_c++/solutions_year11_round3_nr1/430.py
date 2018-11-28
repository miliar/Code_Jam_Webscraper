#include<iostream>
#include<vector>
#include<cstdio>
#include<string>
using namespace std;
main() {
int t, n, cas = 1,r,c, ans;
char ch;
//char v[50][50];
vector<string> v(50);
scanf("%d", &t);
while(t--) {
	ans = 0;
	scanf("%d %d", &r, &c);
	scanf("%c", &ch);
	for(int i =0;i<r;i++) {
		cin>>v[i];
	}
/*	for(int i=0;i<r;i++) {
		cout<<v[i]<<endl;
	}*/
	for(int i=0;i<r;i++) {
	for(int j =0;j<c;j++) {
		if(v[i][j] == '#') {
			if( j==c-1 || i == r-1 || v[i+1][j]!='#' || v[i][j+1]!='#' || v[i+1][j+1]!='#') {
				ans = -1;
				break;
			}
			else {
				v[i][j] = '/';
				v[i+1][j] = '\\';
				v[i][j+1] = '\\';
				v[i+1][j+1] = '/';
			}
		}
	}
	}
	if(ans==-1)
	printf("Case #%d:\nImpossible\n", cas++);
	else {
	printf("Case #%d:\n", cas++);
	for(int i=0;i<r;i++) {
		cout<<v[i]<<endl;
	}	
	}
}
}
