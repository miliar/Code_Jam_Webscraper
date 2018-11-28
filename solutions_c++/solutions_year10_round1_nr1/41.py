#include <iostream>
#include <string>
#include <sstream>
using namespace std;

#define debug(x) cerr<<#x<<"="<<(x)<<endl;

void eval(){
	int N, K;
	cin>>N>>K;
	char grid[51][51];
	for(int i=0; i<N; i++)
		cin>>grid[i];
	for(int i=0; i<N; i++){
		int p=N-1;
		for(int j=N-1; j>=0; j--){
			if(grid[i][j]!='.'){
				if(j!=p){
					grid[i][p]=grid[i][j];
					grid[i][j]='.';
				}
				p--;
			}
		}
	}
	int rflag=0, bflag=0;
	for(int i=0; i<N; i++){
		int c='.';
		int streak=0;
		for(int j=0; j<N; j++){
			if(grid[i][j]==c){
				streak++;
				if(streak==K){
					if(c=='R')
						rflag=1;
					if(c=='B')
						bflag=1;
				}
			}else{
				c=grid[i][j];
				streak=1;
			}
		}
	}
	for(int i=0; i<N; i++){
		int c='.';
		int streak=0;
		for(int j=0; j<N; j++){
			if(grid[j][i]==c){
				streak++;
				if(streak==K){
					if(c=='R')
						rflag=1;
					if(c=='B')
						bflag=1;
				}
			}else{
				c=grid[j][i];
				streak=1;
			}
		}
	}
	for(int i=0; i<2*N; i++){
		int c='.';
		int streak=0;
		for(int j=(i<N ? 0 : i-N); j<(i<N ? i : N); j++){
			if(grid[i-j-1][j]==c){
				streak++;
				if(streak==K){
					if(c=='R')
						rflag=1;
					if(c=='B')
						bflag=1;
				}
			}else{
				c=grid[i-j-1][j];
				streak=1;
			}
		}
	}
	for(int i=0; i<2*N; i++){
		int c='.';
		int streak=0;
		for(int j=(i<N ? 0 : i-N); j<(i<N ? i : N); j++){
			if(grid[N-(i-j)][j]==c){
				streak++;
				if(streak==K){
					if(c=='R')
						rflag=1;
					if(c=='B')
						bflag=1;
				}
			}else{
				c=grid[N-(i-j)][j];
				streak=1;
			}
		}
	}
	if(!rflag && !bflag)
		cout<<"Neither"<<endl;
	else if(!rflag && bflag)
		cout<<"Blue"<<endl;
	else if(rflag && !bflag)
		cout<<"Red"<<endl;
	else
		cout<<"Both"<<endl;
}

int main(){
/*
	int N=3;
	for(int i=0; i<2*N; i++){
		for(int j=(i<N ? 0 : i-N); j<(i<N ? i : N); j++){
			cout<<(N-(i-j))<<" "<<j<<"  ";
		}
		cout<<endl;
	}
	return 0;
*/

	int cases;
	string line;
	getline(cin, line);
	istringstream(line)>>cases;
	for(int i=1; i<=cases; i++){
		cout<<"Case #"<<i<<": ";
		eval();
	}
	return 0;
}
