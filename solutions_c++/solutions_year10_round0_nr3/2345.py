#include <iostream>
#include <queue>
using namespace std;
int main(void)
{
	int T;
	int R,K,N;
	int i,j,k,m,n;
	queue<int> q;
	int sum;
	
	cin>>T;
	for(i=1;i<=T;i++)
	{
		cin>>R>>K>>N;
		for(j=0;j<N;j++)
		{
			cin>>k;
			q.push(k);
		}
		sum=0;
		for(j=0;j<R;j++)
		{
			k=q.front();
			m=1;
			while(k<=K && m<q.size())
			{
				n=q.front();
				q.pop();
				q.push(n);
				k+=q.front();
				m++;
			}
			if(k>K)
			{
				k-=q.front();
			}
		
			sum+=k;
		}
		cout<<"Case #"<<i<<": "<<sum<<endl;
		while(!q.empty())
			q.pop();
	}
//	system("PAUSE");
	return 0;
}
