#include<iostream>
using namespace std;

int main()
{
	
	int arry[1001][2],T,N,i,j,k,number;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		number=0;
		cin>>N;
		for(j=1;j<=N;j++)
		{
			cin>>arry[j][0]>>arry[j][1];
		}
		for(j=1;j<=N;j++)
		{
			for(k=j+1;k<=N;k++)
			{
				if(arry[j][0]>arry[k][0]&&arry[j][1]<arry[k][1])
				{
					number++;
				}
				else if(arry[j][0]<arry[k][0]&&arry[j][1]>arry[k][1])
				{
					number++;
				}
			}
		}
		cout<<"Case #"<<i<<": "<<number<<endl;

	}
	return 0;
}