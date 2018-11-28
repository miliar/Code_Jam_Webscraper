#include<iostream>
using namespace std;

int main(){
int n;
cin>>n;
for(int i=0;i<n;i++)
{
int ng,s,p;
cin>>ng>>s>>p;
	int type1=0,type2=0,cur;
	for(int j=0;j<ng;j++){
		cin>>cur;
		if(cur%3==0)
		{
			int temp=cur/3;
			if(temp>=1&&temp<=9&&temp+1>=p&&temp<p) type1++;
			else if(temp>=p) type2++;
			else{}
		}
		if(cur%3==1)
		{
			int temp=(cur-1)/3;
			if(temp>=1&&temp<=9&&temp+1>=p&&temp+1<p) type1++;
			else if(temp+1>=p) type2++;
			else{}
		}
		if(cur%3==2)
		{
			int temp=(cur-2)/3;
			if(temp<=8&&temp+2>=p&&temp+1<p) type1++;
			else if(temp+1>=p) type2++;
			else{}
		}
	}
if(type1>s) type1=s;

cout<<"Case #"<<i+1<<":"<<" "<<type1+type2<<endl;
}
return 0;
}

