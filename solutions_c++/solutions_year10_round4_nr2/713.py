#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>
#include<set>

using namespace std;
vector<int > M;
	int C, P;
int f(int s, int e){
	bool sm=false;
	for(int i=s; i<e; i++){
		if(M[i]<P)sm=true;
	}
	int res=0;
	if(sm){
		for(int i=s; i<e; i++){
			M[i]++;
		}       
		res=1+f(s, (s+e)/2)+ f((s+e)/2,e) ;		
	}
	return res;
}
int main(){
	cin>>C;
	for(int i=0; i<C; i++){
		//cin>>wrds[i]; 
		cin>>P;
		M.clear(); M.resize(2000, 0);
		for(int j=0; j<(1<<P); j++)cin>>M[j];
		int tmp;
		for(int j=0; j<(1<<P)-1; j++)cin>>tmp;
		
		int res=0;
		res = f(0, (1<<P));
		cout<<"Case #"<<i+1<<": " <<res<<"\n";
	}
	
}
