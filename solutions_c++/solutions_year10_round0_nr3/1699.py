#include<vector>
#include<iostream>

using namespace std;

int main()
{
	long r,k,n;
	int noOfCases=0;
	cin>>noOfCases;
	int cnt=noOfCases;
	long long num=1;
	long long arr[1000];
	long long res[1000];
	long long nextSt[1000];
	memset(arr,0,sizeof(long)*1000);
	memset(res,0,sizeof(long)*1000);
	while(noOfCases-->0)
	{
		int flag=0;
		int i;
		long long totalsum=0;
		cin>>r>>k>>n;
		for(i=0;i<n;i++)
		{
			cin>>arr[i];
			totalsum+=arr[i];
		}
		if(totalsum<=k)
		{
			cout<<"Case #"<<(cnt-noOfCases)<<": "<<(totalsum*r)<<endl;		
			continue;
		}

		long long pre=0,next=0,sum=0;
		for(;pre<n;)
		{			
			if(sum+arr[next]<=k)
			{
				long presum=sum;
				sum=sum+arr[next];				
				next++;
				if(next>=n)
					next=0;
			}
			else
			{				
				res[pre]=sum;
				sum=sum-arr[pre];
				if(next<=pre)
					nextSt[pre]=(next-pre+n);
				else
				   nextSt[pre]=(next-pre);
				pre++;
			}
		}
		long long money=0,pos=0;
		for(int k=0;k<r;k++)
		{
			money+=res[pos];			
			pos+=nextSt[pos];
			if(pos>=n)
				pos-=n;
		}
		cout<<"Case #"<<(cnt-noOfCases)<<": "<<money<<endl;		
	}
	return 0;
}

