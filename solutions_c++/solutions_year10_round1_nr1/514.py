#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;
vector<char> v[51];
char a[51][51],b[51][51];
int T,n,k;
void input(){
	cin>>n>>k;
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			cin>>a[i][j];
			if (a[i][j]!='.'){
				v[i].push_back(a[i][j]);
			}
		}
	}
}
void transformate(){
	for (int i=0;i<n;i++){
		for (int j=0;j<n-v[i].size();j++){
			b[j][i]='.';
		}
		for (int j=n-v[i].size();j<n;j++){
			b[j][i]=v[i][j-n+v[i].size()];
		}
	}
}	
void printb(){
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			cout<<b[i][j];
		}
		cout<<endl;
	}
}
bool solve_B(){
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			if (b[i][j]!='B') continue;
			if (j+k<=n){
				bool f=true;
				for (int h=j+1;h<j+k;h++){
					if (b[i][h]!=b[i][j]){
						f=false;
						break;
					}
				}
				if (f) return true;
			}
			if (i+k<=n){
				bool f =true;
				for (int h=i+1;h<i+k;h++){
					if (b[h][j]!=b[i][j]){
						f=false;
						break;
					}
					
				}
				if (f) return true;
			}
			if (i+k<=n && j+k<=n){
				bool f =true;
				for (int h=1;h<k;h++){
					if (b[i+h][j+h]!=b[i][j]){
						f=false;
						break;
					}
					
				}
				if (f) return true;
			}
			if (i+k<=n && j-k+1>=0){
				bool f =true;
				for (int h=1;h<k;h++){
					if (b[i+h][j-h]!=b[i][j]){
						f=false;
						break;
					}
					
				}
				if (f) return true;
			}
		}
	}
	return false;
}
bool solve_R(){
	for (int i=0;i<n;i++){
		for (int j=0;j<n;j++){
			if (b[i][j]!='R') continue;
			if (j+k<=n){
				bool f=true;
				for (int h=j+1;h<j+k;h++){
					if (b[i][h]!=b[i][j]){
						f=false;
						break;
					}
				}
				if (f) return true;
			}
			if (i+k<=n){
				bool f =true;
				for (int h=i+1;h<i+k;h++){
					if (b[h][j]!=b[i][j]){
						f=false;
						break;
					}
					
				}
				if (f) return true;
			}
			if (i+k<=n && j+k<=n){
				bool f =true;
				for (int h=1;h<k;h++){
					if (b[i+h][j+h]!=b[i][j]){
						f=false;
						break;
					}
					
				}
				if (f) return true;
			}
			if (i+k<=n && j-k+1>=0){
				bool f =true;
				for (int h=1;h<k;h++){
					if (b[i+h][j-h]!=b[i][j]){
						f=false;
						break;
					}
					
				}
				if (f) return true;
			}
		}
	}
	return false;
}
int main(){
	freopen("readme.txt","r",stdin);
	freopen("output.txt","w",stdout);
	cin>>T;
	for (int t=1;t<=T;t++){
		input();
		transformate();
		//printb();
		bool f1=solve_B();
		bool f2=solve_R();
		cout<<"Case #"<<t<<": ";
		if (f1 && f2)	cout<<"Both"<<endl;
		else
			if(f1) cout<<"Blue"<<endl;
			else
				if (f2) cout<<"Red"<<endl;
				else cout<<"Neither"<<endl;
		for (int i=0;i<n;i++){
			v[i].clear();
		}
	}
	return 0;
}