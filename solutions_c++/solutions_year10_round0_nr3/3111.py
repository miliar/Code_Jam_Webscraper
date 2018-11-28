#include<iostream>
using namespace std;
#define max 10
#include<queue>
queue<int>q;

int T,R,k,N;

int main()
{
	freopen("in1.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int i,j,xx,temp;
	cin>>T;
	for(i=1;i<=T;i++)
	{
		int am=0;
		cin>>R>>k>>N;
		for(j=1;j<=N;j++)
		{
			cin>>temp;
			q.push(temp);
			am+=temp;
		}
		int count=0;
		if(am<=k)count=am*R;
		else
		{
			for(xx=1;xx<=R;xx++)
			{
				int sum=0,sum2;
				while((sum2=(sum+q.front()))<=k)
				{
					sum=sum2;
					q.push(q.front());
					q.pop();
				}
				count+=sum;
			}
		}
		printf("Case #%d: %d\n",i,count);
		while(!q.empty())q.pop();
	}
	return 0;
}