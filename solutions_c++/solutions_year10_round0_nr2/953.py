#include<iostream>
#include<cstdlib>

using namespace std;

int gcd(int a,int b)
{
	int i=1,min,ret;
	if(a>b)	
		min=b;
	else
		min=a;
	while(i<=min)
	{
		if(a%i==0&&b%i==0)
			ret=i;
		i++;
	}
	
	return ret;
}


void insert_sort(int  a[],int N)
{
	int j,i,key;
	for(j=1;j<N;j++)
	{
		key=a[j];
		i=j-1;
		while(i>=0&&a[i]>key)
		{
			a[i+1]=a[i];
			i--;
		}
		a[i+1]=key;
	}
}



int main()
{
	int C,N;
	int * arr;
	int i,j,k,temp,temp1;
	
	cin>>C;
	for(i=1;i<=C;i++)
	{
		cin>>N;
		arr=new int[N];
		for(j=0;j<N;j++)
		{
			cin>>arr[j];
		}
		insert_sort(arr,N);		
		j=0;
		while((arr[j+1]-arr[j])==0)
			j++;
		temp=arr[j+1]-arr[j];
		j++;
		
		while(j<N-1)
		{
			temp1=arr[j+1]-arr[j];
			if(temp1!=0)
				temp=gcd(temp,temp1);
			j++;
		}
		k=0;
		while((arr[0]+k)%temp!=0)
			k++;
		cout<<"Case #"<<i<<": "<<k<<endl;
		delete arr;
	}

	return 0;
}


