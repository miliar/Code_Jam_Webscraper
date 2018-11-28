/*
Author : Prem Kumar
language : C++
*/
#include<iostream>
using namespace std;

int toggle(int a[],int i){
	if(a[i]==1)
		return 0;
	else
		return 1;	
}

void print(int a[],int N,int turn){
	cout<<"printing turn "<<turn<<"\n";
	for(int i=0;i<N;i++){
		cout<<a[i]<<" ";	
	}
	cout<<endl<<endl;
}

int main(){
	unsigned int T,N,K;
	cin>>T;
int ind =1;
while(ind<=T){
	cin>>N>>K;

	int count = 0;
	int a[N];

	for(int q=0;q<N;q++)
		a[q]=0;

	//print(a,N,0);
	while(K!=0){
		if(a[0]==0){
			a[0] = 1;
		}
		else{
			bool val=true;
			int i=0;
			while(i<N && val){
				if(a[i]==0)
				{	a[i]=toggle(a,i);val=false; break;}
				else{
					a[i]=toggle(a,i);
				}
				i++;
			}
		}
		count++;
	//	print(a,N,count);
		K--;
	}
	int flag = 1;
	for(int q=0;q<N;q++){
		if(a[q]==0)
		{	cout<<"Case #"<<ind<<": OFF\n";flag=0;
			 break;}
	}
	if(flag==1)
	cout<<"Case #"<<ind<<": ON\n";
ind++;
}

return 0;
}
