#include<cstdio>
#include<iostream>
#include<algorithm>
using namespace std ;
int A[1000+100], B[1000+100]; 
int n ; 
typedef struct {double x, y ;} Point; 
int main(){
	int tt;  
	freopen("in.txt", "r", stdin); 
	freopen("out.txt", "w", stdout); 
	scanf("%d",&tt); 
	int Cas=0; 
	while(tt--){
		int n;
		scanf("%d",&n); 
		for(int i=0; i <n ;++i){
			scanf("%d%d",A+i, B+i) ;
		}
		int ans=0; 
		for(int i=0; i<n; ++i){
			for(int j=i+1; j<n; ++j){
				if(A[j]>A[i]&&B[j]<B[i]||A[j]<A[i]&&B[j]>B[i] ){
					++ans ;
				}
			}
		}
		printf("Case #%d: %d\n", ++Cas, ans); 

	}
	return 0; 
}
	
				
			