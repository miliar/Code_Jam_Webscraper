#include<iostream>
#define f(i,n) for(int i=0;i<n;i++)
#define ulli unsigned long long int
using namespace std;
int main(){
	int T;
	cin>>T;
	ulli snap[31];
	snap[0]=0;
	snap[1] =1;
	for(int i=1;i<=30;i++){
		snap[i+1] = 2*snap[i] +1;
	}
	f(i,T){
		ulli N,K;
		cin>>N>>K;
		bool done =false;
		if(K<snap[N]) done =false;
		else{
			if((K-snap[N])%(snap[N] +1) == 0){
				done =true;
			}
		}
		
		if(!done){
			cout<<"Case #"<<i+1<<": OFF"<<endl;
		}
		else {
			cout<<"Case #"<<i+1<<": ON"<<endl;
		}
	}
}
