#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>

using namespace std;
void move(vector<string> & mm, int n){
	for(int i=n-1; i>=0; i--){
		for(int j=0; j<n; j++){
			if(mm[j][i]=='.'){
				int j1=-1;
				for(int k=i-1; k>=0; k--){
					if(mm[j][k]!='.'){
						mm[j][i]=mm[j][k]; mm[j][k]='.';
						break;
					}
				}
			}
		}
	}
}
bool find(vector<string> & mm, int n, int k, char c){
	if(k>n)return false;
	int st=-1; int fin=-1;
	int maxlen=0;
	//cout<<"hor"; cout.flush();
	for(int i=0; i<n; i++){
		st=-1; fin=-1;
		for(int j=0; j<n; j++){
			if(mm[i][j]==c){
				if(st==-1){
					st=j; fin=j;
					
				}else{
					fin=j;
				}
			}else{
				if(st>=0 && fin-st+1>maxlen){
					maxlen=fin-st+1;
				}
				st=-1;
			}
			//cout<<i<<" "<<j<<" "<<st<<" "<<fin<<" "<<maxlen<<"\n"; cout.flush();
			if(maxlen>=k) return true;
		}
				if(st>=0 && fin-st+1>maxlen){
					maxlen=fin-st+1;
				}
			if(maxlen>=k) return true;
	}
	st=-1; maxlen=0;
	//cout<<"ver"; cout.flush();
	for(int i=0; i<n; i++){
		st=-1;fin=-1;
		for(int j=0; j<n; j++){
			if(mm[j][i]==c){
				if(st==-1){
					st=j; fin=j;
					
				}else{
					fin=j;
				}
			}else{
				if(st>=0 && fin-st+1>maxlen){
					maxlen=fin-st+1;
				}
				st=-1;
			}
			//cout<<i<<" "<<j<<" "<<maxlen<<"\n"; cout.flush();
			if(maxlen>=k) return true;
		}
				if(st>=0 && fin-st+1>maxlen){
					maxlen=fin-st+1;
				}
			if(maxlen>=k) return true;
	}
	//cout<<"di1";cout.flush();
	st=-1; maxlen=0;
	for(int d=0; d<2*n-1; d++){
		st=-1;fin=-1;
		for(int i=0; i<n && i<=d && i<=2*n-1-d; i++){
			int x,y;
			if(d<n){
				y=i; x = d-i;
			}else{
				y=n-i-1; x=d-y;
			}
			//cout<<y<<" "<<x<<" "<<d<<"\n";
			if(mm[y][x]==c){
				if(st==-1){
					st=i; fin=i;
					
				}else{
					fin=i;
				}
			}else{
				if(st>=0 && fin-st+1>maxlen){
					maxlen=fin-st+1;
				}
				st=-1;
			}
			if(maxlen>=k) return true;
		}
				if(st>=0 && fin-st+1>maxlen){
					maxlen=fin-st+1;
				}
			if(maxlen>=k) return true;
	}
	st=-1; maxlen=0;
	//cout<<"di2";cout.flush();
	for(int d=-n+1; d<n; d++){
		st=-1;fin=-1;
		for(int i=0; i<n-abs(d); i++){
			int x,y;
			
			y=i; x = d+y;
			if(mm[y][x]==c){
				if(st==-1){
					st=i; fin=i;
					
				}else{
					fin=i;
				}
			}else{
				if(st>=0 && fin-st+1>maxlen){
					maxlen=fin-st+1;
				}
				st=-1;
			}
			if(maxlen>=k) return true;
		}
				if(st>=0 && fin-st+1>maxlen){
					maxlen=fin-st+1;
				}
			if(maxlen>=k) return true;
	}
	return false;	
}
int main(){
	int T, N, K;
	cin>>T;
	for(int i=0; i<T; i++){
		//cin>>wrds[i]; 
		cin>>N>>K;
		vector<string> ma(N);
		vector<string> map2(N, string(' ', N));
		for(int j=0; j<N; j++) cin>>ma[j];
		move(ma, N);
	/*	for(int j=0; j<N; j++){
			cout<<ma[j]<<"\n";
		}*/
		bool red = find(ma, N, K, 'R');
		bool blue = find(ma, N, K, 'B');
		string res="Neither";
		if(red && blue)res="Both";
			else if(red)res="Red";
			else if(blue)res="Blue";
		cout<<"Case #"<<i+1<<": " <<res<<"\n";
	}
	
}
