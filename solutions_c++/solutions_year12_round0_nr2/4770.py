#include<cstdio>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
int main()
{
int T,N,p,a[120],S,m,count1,count2,i;
int r,s,t;
cin>>T;
t=T;
while(T--)
{
	cin>>N>>S>>p;
	for(i=0;i<N;i++)
		cin>>a[i];
	count1=0;
	count2=0;
	r=3*p-2;
	s=3*p-4;
	if(p==0){r=0;s=0;}
	if(p==1){r=1;s=1;}
	for(i=0;i<N;i++)
	{
		if(a[i]>=r)
			count1++;
		if(a[i]>=s)
			count2++;
	}
	m=min(count2,count1+S);
	cout<<"Case #"<<t-T<<": "<<m<<endl;
}
return 0;
}
