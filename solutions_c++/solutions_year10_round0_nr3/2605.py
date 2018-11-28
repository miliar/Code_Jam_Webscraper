#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	for(int i=1;i<=t;i++)
	{
		int r,k,n;
		long long int result=0;
		queue<int> Q;
		queue<int> nQ;
		//initialize
		Q=queue<int> ();
		nQ=queue<int> ();
		//
		scanf("%d%d%d",&r,&k,&n);
		for(int j=0;j<n;j++)
		{
			int temp;
			scanf("%d",&temp);
			Q.push(temp);
		}
		for(int j=0;j<r;j++)
		{
			int rollerC=k;
			while(!Q.empty() && rollerC>=Q.front())
			{
				result+=Q.front();
				rollerC-=Q.front();
				nQ.push(Q.front());
				Q.pop();
			}
			while(!nQ.empty())
			{
				Q.push(nQ.front());
				nQ.pop();
			}
		}
		printf("Case #%d: ",i);
		cout << result << endl;
	}
	return 0;
}
