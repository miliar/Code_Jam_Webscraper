// Google.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <iostream>
#include <string>
using namespace std;

int main(){
	int l,d,n;
	cin>>l>>d>>n;
	string dic[5000],s;
	for(int i =0;i<d;i++)
		cin>>dic[i];
	for(int i =1;i<=n;i++){
		int let[26][15],c=0,ans=0;
		memset(let,0,sizeof(let));
		cin>>s;
		for(int j=0;j<l;j++){
			if(s[c]=='('){
				c++;
				while(s[c]!=')'){
					let[s[c]-'a'][j]=1;
					c++;
				}
			}
			else{
				let[s[c]-'a'][j]=1;
			}
				c++;
		}
		//for(int j=0;j<s.length();j++){
		//	char x =s[j];
		//	switch(x){
		//		case '(':
		//			break;
		//		case ')':
		//			c++;break;
		//		default:
		//			let[x-'a'][c]=1;
		//	}
		//}
		for(int j=0;j<d;j++){
			int k;
			for(k=0;k<l;k++){
				if(let[dic[j][k]-'a'][k]!=1) break;
			}
			if(k==l)
				ans++;
		}
		cout<<"Case #"<<i<<": "<<ans<<endl;

	}
	//int n,next,c[19][3];
	//string s,jam="welcome to code jam";
	//scanf("%d",&n);
	//getchar();
	//for(int i = 1;i<=n;i++){
	//	getline(cin,s);
	//	int ind=0;
	//	int k;
	//	for(int j =0;j<19;j++){
	//		c[j][0]=c[j][1]=c[j][2]=0;
	//	}
	//	do{
	//		for(int j =0;j<19;j++){
	//			c[j][1]=
	//		}
	//	}while(ind!=-1);
	//}
	return 0;
}

