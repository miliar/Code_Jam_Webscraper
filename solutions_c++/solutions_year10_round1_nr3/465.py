#include<iostream>
using namespace std;

int search(int a,int b,int color){
	//printf("a=%d b=%d color=%d\n",a,b,color);
	int tmp;
	if(a == b)return -color;
	if(a%b == 0 || b%a ==0){
		return color;
	}
	if(search(b,a%b,-color) == color){
		return color;
	}
	
	
	if( a%b+b < a && search( a%b+b,b,-color ) == color ){
		return color;
	}
	
	return -color;
} 

int main(){
	int T,A1,A2,B1,B2;
	scanf("%d",&T);
	for(int i=0;i<T;i++){
		scanf("%d %d %d %d",&A1,&A2,&B1,&B2);
		int cnt = 0,tmp;
		
		for(int j=A1;j<=A2;j++){
			for(int k=B1;k<=B2;k++){
				if(k>j){
					if( search(k,j,1) == 1 ){
						cnt++;
					}
				}else{
					if( search(j,k,1) == 1 ){
						cnt++;
					}

				}
				
			}
		}
		cout << "Case #" << i+1 << ": " << cnt << endl;
	}
	return 0;
}
