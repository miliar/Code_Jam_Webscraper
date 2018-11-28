#include<iostream>
#include<vector>
#include<string>
#include <iomanip>
#include<sstream>

using namespace std;

int main(){
	int T,pd, pg;
	long long N;
	cin>>T;
	for(int i=0; i<T; i++){
		cin>>N>>pd>>pg;
		bool res=false;
		if((pg==100 && pd<100) || (pg==0 && pd>0) ){
			res=false;
		}else{
			int ngames=100;
			for(int i=0; i<2; i++){
				if(pd%2==0){pd/=2; ngames/=2;}
				if(pd%5==0){pd/=5; ngames/=5;}
			}
			if(ngames<=N)res=true;
			else res=false;
		}
		
		cout<<"Case #"<<i+1<<": ";
		if(res)cout<<"Possible"<<"\n";
		else cout<<"Broken"<<"\n";
	}
	
}
