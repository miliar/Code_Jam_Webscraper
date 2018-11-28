#include<iostream>
#include<stdio.h>
using namespace std;
int main(){
	int t,n,s,p,m[100],s1=0,ans[100];
	for(int i=0;i<100;i++)
	ans[i]=0;
	cin>>t;
	for(int k=0;k<t;k++){
	scanf("%d %d %d",&n,&s,&p);
	s1=0;
	for(int i=0;i<n;i++)
		scanf(" %d",&m[i]);
	for(int i=0;i<n;i++){
		if((m[i]==3*p-3&&m[i]!=0)||m[i]==3*p-4){
			if(s1<s){
				s1++;
				ans[k]++;
				
			}
		}
	}
	for(int i=0;i<n;i++){
		if(m[i]>3*p-3){
			ans[k]++;
		}
		
	}
}
	for(int i=0;i<t;i++)
	cout<<"Case #"<<1+i<<": "<<ans[i]<<endl;
}
	
