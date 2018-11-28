#include <iostream>
#include <vector>
#include <string>

#define MIN(X,Y) ((X)<(Y)?(X):(Y))

using namespace std;

int main(){
	int T;
	cin>>T;
	int N,S,p;
	int t;
	
	int rig,sol;

	for(int i=0;i<T;i++){
		cin>>N>>S>>p;

		rig=0;sol=0;

		for(int j=0;j<N;j++){
			cin>>t;
			if(t>=3*p-2) rig++;
			else if(t<=1||t>=29) continue;
			else if(t>=3*p-4) sol++;
		}

		cout<<"Case #"<<i+1<<": "<<rig+MIN(sol,S)<<endl;
	}
	return 0;
}
