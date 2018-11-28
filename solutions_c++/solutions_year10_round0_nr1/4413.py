#include<iostream>
#include<string.h>
#include<stdio.h>


using namespace std;

void exc(int a[],int j)
{
	for(int i=1;i<=j;i++){
		if(a[i]==1)
			a[i]=0;
		else
			a[i]=1;

	}
}

int snapper(int n,int k)
{
	int a[n];

	//memset(a,0,n);

	for(int i=1;i<=n;i++)
		a[i]=0;


	for(int i=0;i<k;i++){
		int j=1;
		while(a[j]==1 && j<=n)
			j++;
		exc(a,j);
	}

	int chk=1;

	//cout<<a[0]<<" "<<a[1];
	for(int i=1;i<=n;i++) 
		if(a[i]==0)
		{
			//cout<<"enter";
			chk=0;
		}

	if(chk==1)
		return 1;
	else
		return 0;

}

int main()
{
	int T;
	int n,k;

	cin>>T;
	int counter=1;

	while(T>0){
		cin>>n>>k;

		if(snapper(n,k))
			cout<<"Case #"<<counter<<": ON\n";
		else
			cout<<"Case #"<<counter<<": OFF\n";
	
		
		T--;
		counter++;
	}

	
	return 0;

}
