//#include<iostream>
#include<fstream>
#include<algorithm>
#include<stdio.h>
using namespace std;

int arr[1100000]={0,};


int main(){
	int T,cs=0;
	ifstream in("input.txt");
	FILE* out=fopen("output.txt","w");

	in>>T;

	while(++cs<=T){
		int X,S,R,N;
		double t;		
		in>>X>>S>>R>>t>>N;
		double sum=0;
		for(int i=0;i<X;i++) arr[i]=0;

		for(int i=0;i<N;i++){
			int B,E,w;
			in>>B>>E>>w;
			for(int j=B;j<E;j++){
				arr[j]=w;
			}
		}
		
		sort(arr,arr+X);
		

		
	//	for(int i=0;i<t;i++) arr[i]+=R;
	//	for(int i=t;i<X;i++) arr[i]+=S;
	//	for(int i=0;i<X;i++) sum+=1.00/arr[i];
		
		for(int i=0;i<X;i++){
			if(t>0){
				if(t*(R+arr[i])>=1){
					sum+=1.00/(arr[i]+R);
					t-=1.00/(arr[i]+R);
				}
				else{
					double one=1;
					sum+=t;
					one-=t*(R+arr[i]);
					sum+=one/(S+arr[i]);
					t=0;
				}
			}
			else{
				sum+=1.00/(arr[i]+S);
			}
		}

		fprintf(out,"Case #%d: %.8lf\n",cs,sum);
	}
	
	return 0;
}