#include<iostream>
using namespace std;

char ar[100][100];
int T,N,M;
bool valid;
char ch;

int main() {
	cin>>T;
	for(int tc=1;tc<=T;tc++) {
		cin>>N>>M;
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				cin>>ch;
				ar[i][j]=ch;
			}
		}
		for(int i=0;i<N-1;i++) {
			for(int j=0;j<M-1;j++) {
				if(ar[i][j]=='#'&&ar[i][j+1]=='#'&&ar[i+1][j]=='#'&&ar[i+1][j+1]=='#') {
					ar[i][j]='/'; ar[i][j+1]='\\'; ar[i+1][j]='\\'; ar[i+1][j+1]='/'; 
				}
			}
		}
		valid=true;
		for(int i=0;i<N;i++) {
			for(int j=0;j<M;j++) {
				if(ar[i][j]=='#') valid=false;
			}
		}
		cout<<"Case #"<<tc<<":"<<endl;
		if(valid) {
			for(int i=0;i<N;i++) {
				for(int j=0;j<M;j++) {
					cout<<ar[i][j];
				}
				cout<<endl;
			}
		}
		else cout<<"Impossible"<<endl;
	}
}
