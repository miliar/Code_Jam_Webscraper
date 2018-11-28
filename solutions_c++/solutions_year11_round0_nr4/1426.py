#include<iostream>
#define MAX 1001
using namespace std;
int main()
{
	freopen("D-large.in","r",stdin);
	freopen("D-large.txt","w",stdout);
	int N,i,cases,T,arr[MAX],index[MAX],counter,sum,j;
	bool check[MAX];
	cin>>T;
	for(cases=1;cases<=T;cases++)
	{
		cin>>N;
		for(i=1;i<=N;i++)
		{
			cin>>arr[i];
			index[arr[i]]=i;
		}
		sum=0;
		memset(check,0,sizeof(check));
		for(i=1;i<=N;i++)
		{
			if(arr[i]==i || check[i])
				continue;
			j=i;
			counter=0;
			while(arr[j]!=index[arr[j]])
			{
				check[j]=true;
				counter++;
				j=index[arr[j]];
				if(j==i)
					break;
			}
			sum+=counter;
		}
		printf("Case #%d: %d.000000\n",cases,sum);
	}
	return 0;
}
