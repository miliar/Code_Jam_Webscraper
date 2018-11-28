#include<iostream>
using namespace std;
int A[101];
int main(){
	int t,n,s,p,res;cin>>t;
	
	for(int i = 0; i < t; i++){
		cin>>n>>s>>p;
		int c = 0;
		for(int j = 0; j < n; j++){
			cin>>A[j];
			if( A[j] % 3 == 1){
				res = A[j] / 3;
				res += 1;
				if( res >= p)
					c++;
				continue;
			}
			else if(A[j] % 3 == 0){
				res = A[j] / 3;
				if( res >= p){
					c++;
					continue;
				}
				if( A[j] >= 2 && A[j] <= 28 && res + 1 >= p && s > 0){
					s--;c++;continue;
				}
			}
			else if(A[j] % 3 == 2){
				res = A[j] / 3;
				if( res +1 >= p){
					c++;continue;
				}
				if( A[j] >= 2 && A[j] <= 28 && res + 2 >= p && s > 0){
					s--;c++;continue;
				}
			}

		}
		cout << "Case #" << i+1 << ": " << c <<endl; 					
	}
	return 0;		
}
	
	
