#include <iostream>
using namespace std;
int T,N;
pair<int,int> h[1024];
int main()
{
	scanf("%d",&T);
	for(int t=1;t<=T;t++)
	{
		scanf("%d",&N);
		for(int i=1;i<=N;i++)
		{
			int t1,t2;
			scanf("%d %d",&t1,&t2);	
			h[i] = make_pair(t1,t2);
		}	
		
		int cnt = 0;
		for(int i=1;i<=N;i++)
		{
			for(int j=i+1;j<=N;j++)
			{
				if(i==j) continue;
				if( (h[j].first-h[i].first)*(h[j].second-h[i].second) <0)
				{
				//	cout<<i<<":"<<j<<endl;
					cnt++;
				}
			}	
		}
		
		printf("Case #%d: %d\n",t,cnt);
	}
}
