#include<iostream>
#include<algorithm>
#include<cmath>

using namespace std;

#define FOR(i,a,b)		for(int i=(a); i<(b); i++)
#define REP(i,n)		FOR(i,0,n)

char input[50][50];

int main() {
	int t, r, c;
	bool flag;

	cin>>t;

	for(int i=0; i<t; i++) {
		cin>>r>>c;
		for(int j=0;j<r;j++) {
			for(int k=0;k<c;k++) {
				cin>>input[j][k];
			}
		}
		
		cout<<"Case #"<<i+1<<":"<<endl;
		flag = true;
		for(int j=0;j<r;j++) {
			for(int k=0;k<c;k++)
				if(input[j][k] == '#') {
					if((input[j+1][k] == '#') && (input[j][k+1] == '#') && (input[j+1][k+1] == '#')) {
						input[j][k] = '/';
						input[j+1][k+1] = '/';
						input[j][k+1] = '\\';
						input[j+1][k] = '\\';
					}
					else {
						cout<<"Impossible"<<endl;
						flag = false;
						break;
					}
				}
			if(!flag)
				break;
		}
		if(flag) {
			for(int j=0;j<r;j++){
				for(int k=0;k<c;k++)
					cout<<input[j][k];
				cout<<endl;
			}
		}
			
	}
	return 0;

}
