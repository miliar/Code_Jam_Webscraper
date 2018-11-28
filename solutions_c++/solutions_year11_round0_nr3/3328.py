#include<iostream>
#include<fstream>

using namespace std;

int main(int argc, char **argv){
	ifstream ifs( argv[1] );

	int T;
	ifs>>T;

	int times=0;
	while(T--){
		++times;
		int N;
		int store[100];
		ifs>>N;
		
		for(int i=0;i<N;i++)
			ifs>>store[i];

		int ans=0;
		for(int i=1;i< (1<<N)-1;i++){

			int num=1;
			
			int add1=0,add2=0;
			int ans1=0,ans2=0;
			for(int j=0;j<N;j++){
				if( (num<<j) & i){
					add1 = add1^store[j];
					ans1+=store[j];
				}
				else{
					add2 = add2^store[j];
					ans2+=store[j];
				}
			}
			if(add1==add2)	
				ans = max( ans, max( ans1, ans2) );

		}
		
		if(ans)
			cout<<"Case #"<<times<<": "<<ans<<endl;
		else
			cout<<"Case #"<<times<<": "<<"NO"<<endl;

	}
	return 0;
}
