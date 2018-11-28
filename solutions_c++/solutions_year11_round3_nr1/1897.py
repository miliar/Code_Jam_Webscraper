#include<iostream>
using namespace std;

int main(){
	int test;
	cin>>test;
	for(int  t=0;t<test;t++){
	int r,c;
	cin>>r>>c;
	char arr[r][c];
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			cin>>arr[i][j];
		}
	}
	bool imp=0;
	for(int i=0;i<r;i++){
		for(int j=0;j<c;j++){
			if(arr[i][j]=='#'){
				if(i+1<r && j+1<c){
					if(arr[i+1][j]=='#' && arr[i][j+1] && arr[i+1][j+1]=='#' ){
						arr[i][j]=arr[i+1][j+1]='/';
						arr[i][j+1]=arr[i+1][j]='\\';
					}
					else{
						imp=1;
						break;
					}
				}
				else{
					imp=1;
					break;
				}
			}
		}
		if(imp) break;
	}
	cout<<"Case #"<<t+1<<":"<<endl;
	if(imp) cout<<"Impossible"<<endl;
	else{
		for(int i=0;i<r;i++){
			for(int j=0;j<c;j++){
				cout<<arr[i][j];
			}
				cout<<endl;
		}
	}
	}
}
