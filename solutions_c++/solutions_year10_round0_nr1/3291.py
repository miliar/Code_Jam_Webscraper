#include<iostream>
#include<fstream>
#include<vector>

using namespace std;


long pow(long i,long e){
	if(e==1){
		return i;
	}
	return i * pow(i,e-1);
}


int main(){
	long t, n, k;
	ofstream out("out.txt");
	cin>>t;
	for(int i = 0 ; i < t ; i++){
		cin>>n;
		cin>>k;
		if((k+1)%pow(2,n) == 0){
			out<<"Case #"<<(i+1)<<": "<<"ON"<<endl;
		}else{
			out<<"Case #"<<(i+1)<<": "<<"OFF"<<endl;
		}
		
	}

	system("pause");
	return 0;
}
