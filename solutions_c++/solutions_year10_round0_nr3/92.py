#include<iostream>
#include<vector>
#include<string>
#include <iomanip>

using namespace std;
long long calc(int r, vector<int> & g, int gn, int ul, int sp){
	long long res=0;
	int pos=sp;
	for(int i=0; i<r; i++){
		int sum=0; int c=0;
		while(sum<ul && c<gn){
			if(sum+g[pos]<=ul){
			sum+=g[pos];
			pos++;
			pos%=gn;
			c++;
			} else break;
		}
		res+=sum;
	}
	
	return res;
}
void calc2(vector<int> & g, int gn, int ul, long long & r1, long long &c1, long long & r2, long long & c2, int & sp ){
	r1=c1=c2=r2=sp=0;
	int pos=0; long long res=0;
	vector<long long> rs(gn, 0);
	vector<long long> cs(gn, 0);
	for(int i=0; ; i++){
		long long sum=0; int c=0;
		while(sum<ul && c<gn){
			if(sum+g[pos]<=ul){
			sum+=g[pos];
			pos++;
			pos%=gn;
			c++;
			} else break;
		}
		res+=sum;
		if(rs[pos] || pos==0){
			r1=rs[pos]; r2 = i+1-r1;
			c1 = cs[pos]; c2 = res-c1;
			sp=pos;
			return;
		}else{
			rs[pos]=i+1;
			cs[pos]=res;
		}
	}
	
}
int main(){
	int T;
	cin>>T;
	int R, K,N;
	vector<int> g(1000,0);
	for(int i=0; i<T; i++){
		cin>>R>>K>>N;
		for(int j=0; j<N;j++){
			cin>>g[j];
		}
		long long res=0;
		if(R<=10000){
			res = calc(R, g, N, K, 0);
		} else {
			long long r1, r2, c1, c2; int sp;
			calc2(g, N, K, r1, c1, r2, c2, sp);
			long long A = calc((R-r1)%r2, g, N, K, sp);
			res = A+ c1+ c2*((R-r1)/r2);
			//cout<<r1<<" "<<c1<<" "<<r2<<" "<<c2<<" "<<res<<"\n";
		}
		cout<<"Case #"<<i+1<<": "<<res<<"\n";
	}
	
}
