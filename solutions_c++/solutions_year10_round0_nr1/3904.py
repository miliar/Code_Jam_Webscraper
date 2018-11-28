
//#include <iostream>
#include <algorithm>
#include <vector>
#include <fstream>


using namespace std;
#define VL vector<long long>
#define IO ifstream cin("A-large.in") ; ofstream cout("A-large.out");
#define ll long long

IO

VL preCal;

inline void gen(){
	preCal.assign(50,(ll)0);
	ll ini=1;
	
	for(int i = 1; i <= 31 ; i++){
		preCal[i] = ini<<=1;
	}
return ;
}

inline void decision(int testCase){
	
	int indx;
	ll value;
	
	cin>>indx>>value;
	
	
	cout<<"Case #"<<testCase<<": ";
	
	if(value==0){
		cout<<"OFF\n";
	}
	else{
		long long tmpValue = value%preCal[indx] ;
		
		if(tmpValue == (preCal[indx]-1 ) ){
			cout<<"ON\n";
		}
		else{
			cout<<"OFF\n";
		}
	}
return ;
}

int main(){
	gen();
	int testCase;
	cin>>testCase;
	for(int i=1;i<=testCase;i++){
		decision(i);
	}
	return 0;	
}
