#include <iostream>
#include <vector>
using namespace std;

int timee;
int con[100][100];
int a[100][100];
int use[100];
int n,k;
int connect(int * a, int * b){
	if(a[0]==b[0])
		return true;
	for(int i=1; i<k; i++){
		if((a[i]<b[i])!=(a[i-1]<b[i-1]))
			return true;
		if(a[i]==b[i])
			return true;
	}
	return false;
}
vector<int> put[100];
int search(int t, int k){
	if(clock()-timee>500){
		return false;
	}
	if(t==n){
		return true;
	}
	if(t==0){
		for(int i=0; i<k; i++){
			put[i].clear();
		}
	}
	for(int i=0; i<k; i++){
		int conn=false;
		for(int p=0; p<(int)put[i].size(); p++){
			if(con[put[i][p]][t])
				conn=true;;
		}
		if(!conn){
			put[i].push_back(t);
			if(search(t+1,k))
				return true;
			put[i].pop_back();
		}
	}
	return false;
}
int main(){
	int t;
	cin >> t;
	for(int kase=1; kase<=t; kase++){
		cin >> n >> k;
		for(int i=0; i<n; i++){
			for(int j=0; j <k ;j++){
				cin>> a[i][j];
			}
		}
		for(int i=0; i<n; i++){
			for(int j=0; j<n; j++){
				if(i-j){
					if(connect(a[i],a[j])){
						con[i][j]=true;
					}
					else
						con[i][j]=false;
				}
						cerr<<con[i][j]<<" ";
			}
			cerr<<endl;
		}
		for(int ans=n; ; ans--){
			timee=clock();
			if(!search(0,ans)){
				cout<<"Case #"<<kase<<": "<<ans+1<<endl;
				break;
			}
		}
	}
}


