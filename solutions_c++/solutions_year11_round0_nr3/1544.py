// c.cpp : 定义控制台应用程序的入口点。
//

//#include "stdafx.h"


#include<iostream>
#include<algorithm>
using namespace std;
#define N 1004
int main(){
	int T;
	int n;
	//freopen("C-large.in","r",stdin);
	//freopen("out.txt","w",stdout);
	int a[N];
	int i;
	cin>>T;
	int cas=1;
	int sum;
	int s;
	while(T--){
		cin>>n;
		sum=s=0;
		for(i=0;i<n;i++){
			cin>>a[i];
			sum=sum+a[i];
			s=s^a[i];
		}
		cout<<"Case #"<<cas++<<": ";
		if(s!=0)
		{
			cout<<"NO"<<endl;
			continue;
		}
		sort(a,a+n);
		cout<<sum-a[0]<<endl;
	}
}