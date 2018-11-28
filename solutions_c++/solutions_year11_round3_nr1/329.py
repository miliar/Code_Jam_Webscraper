#include <iostream>
#include <math.h>
#include <string>
#include <set>
using namespace std;
#define MAX(a, b) (((a)<(b))?(b):(a))
int R,C;
char A[51][51];

void fill(int ii, int jj){
	A[ii][jj]=A[ii+1][jj+1]='/';
	A[ii][jj+1]=A[ii+1][jj]='\\';
}
bool possible(int ii, int jj){
	if((ii<R-1) && (jj<C-1)){
		if((A[ii][jj]=='#') && (A[ii+1][jj]=='#') && (A[ii][jj+1]=='#') && (A[ii+1][jj+1]=='#')){
			return true;
		}
		return false;
	}
	return false;
}
void solve(int c){
	for(int i=0;i<R;++i){
		for(int j=0;j<C;++j){
			if((A[i][j]=='#') && possible(i,j)){
				fill(i,j);
			}
		}
	}
	/////
	bool ok=true;
	for(int i=0;i<R;++i){
		for(int j=0;j<C;++j){
			if(A[i][j]=='#'){
				ok=false;
			}
		}
	}
	if(!ok){
		cout<<"Case #"<<c<<":"<<endl<<"Impossible"<<endl;
		return;
	}
	cout<<"Case #"<<c<<": "<<endl;
	for(int i=0;i<R;++i){
		for(int j=0;j<C;++j){
			cout<<A[i][j];
		}
		cout<<endl;
	}
	
	
	
}


int main(int argc, char *argv){
	int numCases;
	cin>>numCases;
	for(int c=0;c<numCases;++c){
		cin>>R>>C;
		string s;
		for(int i=0;i<R;++i){
			cin>>s;
			for(int j=0;j<C;++j){
				A[i][j]=s[j];
			}
		}
		solve(c+1);
	}
	return 0;
}
