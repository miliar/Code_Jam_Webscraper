#include<iostream>
#include<cstdlib>
using namespace std;

int main()
{
	int T,R,K,N;
	int * groups;
	int i,j,k,sum,ptr,prev,count;	
		
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>R;
		cin>>K;
		cin>>N;
		
		groups= new int[N];
		for(j=0;j<N;j++)
			cin>>groups[j];
	
		sum=0;
		ptr=0;
		for(j=0;j<R;j++)
		{
			k=0;		
			count=0;	
			while(k<=K&&count<=N)
			{
				k+=groups[ptr];
				prev=ptr;
				if(ptr==N-1)
					ptr=0;
				else
					ptr++;
				count++;
			}
			k-=groups[prev];
			ptr=prev;
			sum+=k;
		}
	
		cout<<"Case #"<<i<<": "<<sum<<endl;
	}

	return 0;
}
