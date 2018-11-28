#include<iostream>
#include<fstream>
#include<vector>
using namespace std;

int main(){
    ifstream cin("f1.in");
    ofstream cout("f2.out");
    int t;
    cin>>t;
	for(int j=1;j<=t;j++){
		long num;
		cin>>num;
		int cnum;
		int min=100000000;int all=0;int flag;
		for(int i=1;i<=num;i++){
			cin>>cnum;
			all+=cnum;
			if(cnum<min) min=cnum;
			if(i==1){
				flag=cnum;
				continue;
			}
			flag^=cnum;
		}
		if(flag==0){
			int ans=all-min;
			cout<<"Case #"<<j<<": "<<ans<<endl;
		}else{
			cout<<"Case #"<<j<<": NO"<<endl;
		}
	}
}