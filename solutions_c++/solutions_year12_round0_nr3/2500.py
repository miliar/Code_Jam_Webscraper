#include<iostream>
#include<cstring>
#include<stdio.h>
#include<algorithm>
#include<cstdlib>
#include<fstream>
#include<vector>
#include<cmath>
using namespace std;

vector<int>sieve(2000000);

int ifFound(int a,int b,int n){

	int low=a-1;
	int high=b-1;
	int mid;

	while(high>=low){

		mid=(high+low)/2;
			
		if(sieve[mid]==n){
			//cout<<n<<"\t"<<sieve[mid]<<endl;
			return sieve[mid];
		}
		else if(n>sieve[mid]){
			low=mid+1;
		}
		else if(n < sieve[mid]){
			high=mid-1;
		}
	}

	return 0;

}


int main(){

	ofstream fout ("googlecodejamq3long.txt");
    	ifstream fin ("C-large.in");
	int testcase;
	fin>>testcase;
	int i,j,k;int o=1;int flag=0;
	int a,b;int len,t,exp;int y;
	long long int count=0;int result;int n;
	vector<int>rev(2000000);
	for(i=0;i<2000000;i++){
		sieve[i]=i+1;
		rev[i]=i+1;
	}
	while(testcase--){
	
		fin>>a>>b;
		if(b<10){
			count=0;
			flag=1;
		}
		for(i=(a);i<(b) && flag==0;i++){
			
			t=i;len=0;
			while(t>0){
				t/=10;
				len++;		
			}
			exp = pow(10,len-1);
			t=i;
			n=1;
			//cout<<i<<"\t"<<exp<<"\t"<<y<<endl;
			while(i!=n){
				y=t%10;
				t=t/10;
				n=(y*exp)+t;
				//cout<<i<<"\t"<<n<<endl;
				if(n!=i){
					result = ifFound(a,b,n);
					if(result!=0 && i<result){
						//cout<<i<<"\t"<<result<<endl;
						count++;
					}
				}
				t=n;
			}
		
		}
		//count=count/2;
		fout<<"Case #"<<o<<": "<<count<<"\n";
		o++;
		count=0;
		flag=0;
	}	
	
	return 0;
 
} 
