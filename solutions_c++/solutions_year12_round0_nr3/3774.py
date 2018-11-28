#include<iostream>
#include<cstdio>
#include<vector>
#include<cmath>
#include<map>
using namespace std;
int RetDigits(int n){
	int no=0;
	while(n){
		no++;
		n/=10;
	}
	return no;
}
int main(){
	int test,A,B,Dno,k=1,num;
	long long count;
	cin>>test;
	while(test--){
		cin>>A>>B;
		count=0;
		map< pair<int,int>,int> freq;
		for(int i=A;i<=B;i++){
			Dno=RetDigits(i);
			if(Dno==1)
				continue;
			else{
				for(int j=1;j<Dno;j++){
					int n=pow(10,j);
					num=pow(10,Dno-j)*(i%n)+(i/n);
					pair<int,int> PI;
					if(num>=i){
						PI.first=num;
						PI.second=i;
					}
					else{
						PI.first=i;
						PI.second=num;
					}
					if(num>=A && num<=B && !freq[PI]&& num!=i){
						count++;
						freq[PI]=1;
						//cout<<i<<"   "<<num<<"count=="<<count<<endl;
					}
						
					
				}
			}	
		}
		printf("Case #%d: %lld\n",k++,count);
	}
	return 0;
}
