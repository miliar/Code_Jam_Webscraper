#include<iostream>
#include<vector>
using namespace std;
vector<int> t[2000001];
int pot[8]={1,10,100,1000,10000,100000,1000000,2000001};
int main(){
	int vec=1;
	for(int i=1;i<7;++i){
		int L=pot[i+1];
		for(int j=pot[i];j<L;++j){
			int x=j;
			for(int k=0;k<i;++k){
				x=(x%10)*pot[i]+x/10;
				if(x>j)t[j].push_back(x);
			}
		}
	}
	int T;
	cin>>T;
	for(int i=1;i<=T;++i){
		int A,B;
		cin>>A>>B;
		int res=0;
		for(int j=A;j<=B;++j){
			for(int k=t[j].size()-1;k>=0;--k){
				if(t[j][k]<=B)++res;
			}
		}
		cout<<"Case #"<<i<<": "<<res<<"\n";
	}
}
