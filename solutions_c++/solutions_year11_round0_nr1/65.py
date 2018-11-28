#include<iostream>
using namespace std;
#include<stdio.h>
int a[105];
char b[105];
int s[2][2];  //0 position 1 time

int f(int x){
	if(x>0)
		return x;
	else
		return -x;
}
int main(){
	int T,r,i,n,time,temp;
	freopen("in.in","r",stdin);
	freopen("out.txt","w",stdout);
	cin>>T;
	for(r=1;r<=T;r++){
		cin>>n;
		s[0][0]=s[1][0]=1;
		s[0][1]=s[1][1]=0;
		time=0;
		for(i=0;i<n;i++){
			cin>>b[i]>>a[i];
			if(b[i]=='O'){
				temp=f(a[i]-s[0][0])+s[0][1];
				if(temp<time)
					time++;
				else
					time=temp+1;
				s[0][1]=time;
				s[0][0]=a[i];
			}
			else{
				temp=f(a[i]-s[1][0])+s[1][1];
				if(temp<time)
					time++;
				else
					time=temp+1;
				s[1][1]=time;
				s[1][0]=a[i];
			}
		}
		cout<<"Case #"<<r<<": "<<time<<endl;
	}
}