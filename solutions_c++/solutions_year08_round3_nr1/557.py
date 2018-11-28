#include<iostream>
using namespace std;

void sort(long x[],int length)
{
  int key,i;
  for(int j=1;j<length;j++)
  {
     key=x[j];
     i=j-1;
     while(x[i]<key && i>=0)
     {
               x[i+1]=x[i];
         i--;
     }
     x[i+1]=key;
  }
}

int main()
{
	int N,z;
	cin>>N;
	for(int z=1;z<=N;z++)
	{
		int P,K,L;
		cin>>P>>K>>L;
		long fr[L];
		long kp=0;
		for(int i=0;i<L;i++)
			cin>>fr[i];
		if(P*K<L)	
		{
			cout<<"Case #"<<z<<": Impossible"<<endl;
		}
		else
		{
			sort(fr,L);
			/*
			for(int j=0;j<L;j++)	
			{
				cout<<fr[j]<<" ";
			}*/
			int m=0;
			for(int j=0;j<L;j++)	
			{
				if((j%K) == 0)
					m++;
				kp += (long) fr[j]*m;	
			}				
			
		cout<<"Case #"<<z<<": "<<kp<<endl;
		}		
		
	}
	return(0);
}
