#include<stdio.h>
#include<iostream>
using namespace std;

int main(){
	int m,caseno=1;
	cin>>m;
	while(m--){
		int n;
		cin>>n;
		char code[n+1];
		int step[n+1],i,ans=0,poso=1,posb=1,prevo=1,prevb=1;
		for(i=0;i<n;i++){
			cin>>code[i]>>step[i];
			//cout<<code[i]<<step[i]<<" ";
		}
		int timeo=0,timeb=0,curr=0,tmp;
		for(i=0;i<n;i++){
			if(code[i]=='O'){
			   tmp=abs(step[i]-poso)+1;
			   timeo+=tmp;
			   curr=max(curr+1,timeo);
			   timeo=curr;
			   poso=step[i];
			}else{
			   tmp=abs(step[i]-posb)+1;
			   timeb+=tmp;
			   curr=max(curr+1,timeb);
		           timeb=curr;
			   posb=step[i];
			}		
		}
		cout<<"Case #"<<caseno++<<":"<<" "<<curr<<"\n";
	}

	
return 0;
}
