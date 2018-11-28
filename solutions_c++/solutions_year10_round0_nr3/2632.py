#include<iostream>

using namespace std;

int main()
{
	int T,R,N,K,i,j,k,money;
	int arry[1001]={0};
	int arry1[1001]={0};
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>R>>K>>N;
		for(j=1;j<=N;j++)
			cin>>arry[j];

		money=0;
		for(j=1;j<=R;j++)
		{
			int temp=0;
			for(k=1;k<=N;k++)
			{
				if(temp+arry[k]>K)
					break;
				temp+=arry[k];
				arry1[k]=arry[k];
			}
			money+=temp;
			int l=1,m=k-1;
			for(;k<=N;k++)
			{
				arry[l]=arry[k];
				l++;
			}
			l=N;
			for(;m>=1;m--)
			{
				arry[l]=arry1[m];
				l--;
			}
		}

		cout<<"Case #"<<i<<": "<<money<<endl;
	
	}


}