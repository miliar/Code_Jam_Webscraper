#include<iostream>
#include<math.h>
using namespace std;

int comp(int no,int dest,int digits)
{
int flag=0,mod=1,que=1,no1=1;
for(int i=0;i<digits;i++){
	int m=pow(10,i);
	mod=no%m;
	int s=pow(10,digits-i);
	mod*=s;
	que=no/pow(10,i);
	no1=mod+que;
	//if(no==11&&dest==11)
	//cout<<"mod "<<mod<<" que "<<que<<" no1 "<<no1<<endl;
	if (dest==no1){
		flag=1;
		break;
		}
	}
return flag;
}
int main(){
	int a,b,ans[50],j,d,t=0;
	for(int i=0;i<50;i++)
	ans[i]=0;
	cin>>t;
	for(int k=0;k<t;k++){
	cin>>a>>b;
	if(a>=100)
		d=3;
	else
	{
		if(a>=10)
			d=2;
		else
			d=1;
	}
			
	for(int i=a+1;i<=b;i++){
		for(j=a;j<i;j++){
			//cout<<"i :"<<i<<"j :"<<j<<endl;
			//c=comp(j,i,3);
			//if(c==1)
			//cout<<"j "<<j<<" i "<<i<<endl;
			ans[k]+=comp(j,i,d);
		}
	}
}
	for(int i=0;i<t;i++)
	cout<<"Case #"<<i+1<<": "<<ans[i]<<endl;
	return 0;
}
