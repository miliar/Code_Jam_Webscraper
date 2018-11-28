#include<vector>
#include<iostream>
#include<algorithm>
#include<numeric>
#include<limits>
using namespace std;
void process();
int main() {
	int t;
	cin>>t;
	for(int i=1;i<=t;i++) {
		cout<<"Case #"<<i<<":"<<endl;
		process();
	}
}

void process() {
	int r,c;
vector<vector<char> > t;
	cin>>r>>c;
//	char t[50][50];
	for(int i=0;i<r;i++) {
		vector<char> row;
//t[i]= new char[c];
		for(int j=0;j<c;j++) {
			char ch;
			cin>>ch;
			row.push_back(ch);
			//t[i][j]=ch;
		}
		t.push_back(row);
	}
	
	//check for blue
	for(int i=0;i<r;i++) {
		for(int j=0;j<c;j++) {
	//	cout<<"i"<<i<<" j"<<j<<" "<<t[i][j]<<" ";
			if(t[i][j]=='#') {
				if(i==(r-1)||j==(c-1)) {
					cout<<"Impossible"<<endl;
					return;
				}
				if((t[i][j+1]=='#') &&t[i+1][j+1]=='#' &&t[i+1][j]=='#') {
					//possible, mark all
					t[i][j]='/';
					t[i][j+1]='\\';
					t[i+1][j]='\\';
					t[i+1][j+1]='/';
				}else {
					//impossible
					cout<<"Impossible"<<endl;
					return;
				}
			}
		}
	}

	for(int i=0;i<r;i++) {
		for(int j=0;j<c;j++) {
			cout<<t[i][j];
		}
		cout<<endl;
	}
}
