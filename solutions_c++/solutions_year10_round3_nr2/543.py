#include <iostream>
#include <cstdio>
#include <cstring>
#include <vector>
#include <algorithm>
#define MIN(a,b) ((a)<(b)?(a):(b))
#define MAX(a,b) ((a)>(b)?(a):(b))

using namespace std;

int ans[1005][1005];

int T,L,P,C;

void Calc(){
	
	for(int i=1; i<=P-L; i++){
		for(int j=L; j+i<=P; j++){
			if(i==1){
				ans[j][j+i] = 0;
				//cout<<j<<" "<<j+i<<" "<<ans[j][j+i]<<endl;
			}
			else{
				if(j*C >= j+i){
					ans[j][j+i] = 0;
				}
				else{
					int min = -1;
					for(int k=j+1; k<j+i; k++){
						if(min==-1){
							min = 1 + MAX(ans[j][k], ans[k][j+i]);
						}
						else{
						
							int min1 = 1 + MAX(ans[j][k], ans[k][j+i]);
							if(min1<min){
								min = min1;
							}
						}
					}
					ans[j][j+i] = min;
				}
				//cout<<j<<" "<<j+i<<" "<<ans[j][j+i]<<endl;
			}
		}
	}

	return;
}

int main(){

	 
	cin>>T;

	for(int i=0; i<T; i++){
		
		cin>>L>>P>>C;

		for(int j=L; j<P; j++){
			for(int k=j+1; k<=P; k++){
				ans[j][k] = -1;
			}
		}

		Calc();

		cout<<"Case #"<<i+1<<": "<<ans[L][P]<<endl;

		
	}

	return 0;
}