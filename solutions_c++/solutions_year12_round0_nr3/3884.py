#include<iostream>
using namespace std;
int num_digits(int a){
	int d=0;
	while(a!=0){
		a=a/10;
		d++;
		}
	return d;
	}
int cal(int A[],int d,int k){
	int ans=0;
	for(int i=0;i<d;i++){
		ans=ans*10+A[(i+k)%d];}
	return ans;
	}
int main(){
	int n;
	cin>>n;
	for(int i=0;i<n;i++){
		int a,b;
		cin>>a>>b;
		int d = num_digits(a);
		int count=0;
		for(int j=a;j<=b;j++){
			int temp = j;
			int A[d];
			for(int k=d-1;k>=0;k--){
				A[k] = temp%10;
				temp = temp/10;
				}
			int v[d];
			for(int k=0;k<d;k++){
				int t=cal(A,d,k);
				if (k==0){v[k]=t;continue;}
				int c=0;
				for(int l=0;l<k;l++){
						if (t==v[l]){ v[k]=0;c++; }
						} 
				if(c==0){ v[k]=t;}
				}
			for(int k=1;k<d;k++){
				if((v[k]<=b)&&(v[k]>j)){
					count+=1;
					}
					}
					}
			cout<<"Case #"<<i+1<<": "<<count<<endl;
			}
		return 0;}
		
			  
