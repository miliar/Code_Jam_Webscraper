#include<iostream>
using namespace std;
int length(int);
int power(int);
int main1(int,int);
int *p;
int main(){
	int A,B,T,i=0,k;
	cin>>T;
	k=T;
	p=new int [T];
	do{
		cin>>A;
		cin>>B;
		p[i++]=main1(A,B);
		//cout<<p[i-1];
		}while(--T);

	for(i=0;i<k;i++){cout<<"Case #"<<i+1<<": "<<p[i]<<"\n";}
		return 0;
}
int main1(int a,int b){
	int i,len,j,temp,pow,count=0;
	for(i=a;i<=b;i++){
		len=length(i);
		if(len==1)break;
		pow=power(len);
		len--;
		j=i;
		do{
			temp=j%10;
			j/=10;
			j=pow*temp+j;
			if((i<j)&&(j<=b)){count++;  //cout<<i<<"\t"<<j<<"\n";}
			}
		}while(--len);
	}
	return count;
}
int power(int x){
	int i,k=1;
	for(i=x;i>0;i--){
		k*=10;}
	return k/10;
}
int length(int x){
	int i,k=0;
	for(i=x;i>0;i/=10)
		k++;
	return k;
}