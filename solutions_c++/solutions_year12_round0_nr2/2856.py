#include<iostream>
#include<vector>
using namespace std;
int caso(){
	int N,S,p,x,y;
	cin>>N>>S>>p;
	vector<int> a,b;
	int res=0;
	for(int i=0;i<N;++i){
		cin>>x;
		if(x<2){
			if(x>=p)++res;
		}
		else if(x>28){
			++res;
		}
		else{
			y=x/3;
			if(x%3==0)a.push_back(y),b.push_back(y+1);
			else if(x%3==1)a.push_back(y+1),b.push_back(y+1);
			else a.push_back(y+1),b.push_back(y+2);
			if(b.back()>=p)++res;
		}
	}
	int sur=a.size();
	for(int i=a.size()-1;i>=0&&sur>S;--i){
		if((a[i]>=p)==(b[i]>=p))sur--;
	}
	for(int i=a.size()-1;i>=0&&sur>S;--i){
		if((a[i]>=p)!=(b[i]>=p))sur--,res--;
	}
	return res;
}
int main(){
	int T;
	cin>>T;
	for(int i=1;i<=T;++i){
		cout<<"Case #"<<i<<": "<<caso()<<"\n";
	}
}
