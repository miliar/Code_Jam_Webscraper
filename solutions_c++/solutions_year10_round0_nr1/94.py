#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>

using namespace std;

int main(){
	int T, N, K;
	cin>>T;
	for(int i=0; i<T; i++){
		//cin>>wrds[i]; 
		string res="";
		cin>>N>>K;
		if(K%(1<<N) == (1<<N)-1){
			res="ON";
		}else{
			res="OFF";
		}
		
		cout<<"Case #"<<i+1<<": " <<res<<"\n";
	}
	
}
