#include <iostream>
#include <cmath>
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<fstream>

using namespace std;
int m;
string b="welcome to code jam",c;
void calc(int let,int pos){
	int i,k;
	for(i=pos;i<c.length();i++){
		if(b[let]==c[i]){
			if(let==18){
				m+=1;
			}else{
				calc(let+1,i+1);
			}
		}
	}
	return;
}
			
int main(void){
	int i,j,n;
	cin>>n;
	getline(cin,c);
	for(i=0;i<n;i++){
		getline(cin,c);
		m=0;
		calc(0,0);
		cout<<"Case #"<<i+1<<": ";
		m=m%10000;j=0;
		if(m<1000){j=1;}
		if(m<100){j=2;}
		if(m<10){j=3;}
		for(int t=0;t<j;t++){
			cout<<"0";
		}
		cout<<m<<"\n";
	}
	return 0;
}
