#include<iostream>
#include<stdio.h>
#include<string.h>
#include<algorithm>
using namespace std;
int main(){
	int t,T=1;
	cin>>t;
	while(T<=t){
	int n;
	cin>>n;
	int a[n],b[n];
	pair<int,int> pr[n];
	for(int i=0;i<n;i++)
	cin>>pr[i].first>>pr[i].second;
	int cnt=0;
/*	if(n==1)
	{

	}
	else if(n==2)
	{
	if(a[0]<a[1]&&b[0]>b[1])
	{
	cnt=1;
	}
	else if(a[1]<a[0]&&b[1]>b[0])
	{
	cnt=1;
	}
	}
	else
	{*/
	sort(pr,pr+n);
	for(int i=0;i<n;i++)
	{
	for(int j=i+1;j<n;j++)
	{
	if(pr[i].second>pr[j].second)
	cnt++;
	}
	
	}
	
		printf("Case #%d: %d\n",T,cnt);
		T++;
	}
	return 0;
} 
