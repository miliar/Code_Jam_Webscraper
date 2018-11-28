#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>

using namespace std;
		vector<int> a;
		vector<vector<int> > sav;
	int T, D,I,M, N;
int f(int n, int s){
	if(n<0) return 0;
	if(sav[n][s]>=0) return sav[n][s];
	int res=1000000000;
	res=min(res, D+f(n-1, s)); //delete
	//change:
//if(s<=10)cout<<"D "<<res<<"\n";
		int change = abs(a[n]-s);
	for(int c=s-M; c<=s+M && c<256; c++){
		if(c<0)continue;
		res=min(res, f(n-1, c)+change);
	}
//	if(s<=10)cout<<"C "<<res<<"\n";
	//insert:
	if(M!=0){
		int ins = abs((s-a[n])/M);
		if((s-a[n])%M==0 ){
		}else{
			ins++;
		}
	for(int c=a[n]-M; c<=a[n]+M && c<256; c++){
		if(c<0)continue;
		res=min(res, f(n-1, c)+ins*I);
	}
	}
//	if(s<=10)cout<<"I "<<res <<" "<<s<<" "<<a[n]<<" "<<(s-a[n])%M<<"\n";
		
//	if(s<=10)cout<<n<<" "<<s<<" "<<res<<"\n";	
	
	
	sav[n][s]=res;
	return res;
}
int main(){
	cin>>T;
	for(int i=0; i<T; i++){
		//cin>>wrds[i]; 
		cin>>D>>I>>M>>N;
		a.clear(); a.resize(200);
		sav.clear(); sav.resize(200, vector<int> (256, -1));
		for(int j=0; j<N; j++)cin>>a[j];
			
		int res=10000000;
		for(int j=0; j<=255; j++)
		res = min(res , f(N-1,j ));
		cout<<"Case #"<<i+1<<": " <<res<<"\n";
	}
	
}
