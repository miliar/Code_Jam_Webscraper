#include "stdafx.h"

int main(){
	int T;
	cin>>T;
	loop(C, 1, T+1){
		int N, S, p;
		cin>>N>>S>>p;
		int c=0, t;
		if(p>=2){
			loop(n, 0, N){
				cin>>t;
				if(t>=3*p-2)c++;
				elif(t>=3*p-4 && S>0){
					c++;
					S--;
				}
			}
		}elif(p==1){
			loop(n, 0, N){
				cin>>t;
				if(t>=1)c++;
			}
		}else{
			loop(n, 0, N){
				cin>>t;
				c++;
			}
		}
		cout<<"Case #"<<C<<": "<<c<<endl;
	}
    return 0;
}
