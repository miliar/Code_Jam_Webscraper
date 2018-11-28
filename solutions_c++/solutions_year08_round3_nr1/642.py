#include<stdio.h>
#include<iostream.h>
#include<math.h>

int main()
{
int N,P,K,L,j,k,temp,key[10000],cnt;
cin>>N;
for(int i=1;i<=N;i++)
{
cin>>P>>K>>L;
	cnt=0;
	for(j=0;j<L;j++)
			cin>>key[j];
	for(j=0;j<L-1;j++)
			for(k=0;k<L-j-1;k++)
				if(key[k+1]>key[k]) 
				{
					temp=key[k];
					key[k]=key[k+1];
					key[k+1]=temp;
				}
	for(k=0;k<L;k++)
		//cout<<key[k];
		cnt=cnt+key[k]*((k/K)+1);			


cout<<"Case #"<<i<<": "<<cnt<<"\n";
}
return 0;
}
