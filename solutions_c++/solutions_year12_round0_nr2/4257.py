#include <iostream>
using namespace std;

int main(){
	int T;
	cin>>T;
	for(int j=0;j<T;j++){
		int N,S,p;
		cin>>N>>S>>p;
		int t[N][3];
		int count=0;
		//int min[3];
		for(int i=0;i<N;i++){
			int max;
			cin>>t[i][0];
			int rem=t[i][0]%3;
			int div=t[i][0]/3;
			if(rem==0){
				t[i][0]=div;
				t[i][1]=div;
				t[i][2]=div;
				max=div;
				if(max>=p) count++;
				else if(max+1>=p && S>0 && max-1>=0) {count++;S--;}
			}
			else if(rem==1){
				t[i][0]=div+1;
				t[i][1]=div;
				t[i][2]=div;
				max=div+1;
				if(max>=p) count++;
			}
			else{
				t[i][0]=div+1;
				t[i][1]=div+1;
				t[i][2]=div;
				max=div+1;
				if(max>=p) count++;
				else if(max+1>=p && S>0 && max-1>=0) {count++;S--;}
			}
			
		}
		cout<<"Case #"<<j+1<<": "<<count<<endl;
	}
	return 0;
}
		
