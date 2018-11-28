# include<iostream>
# include<cstdio>
# include<queue>
using namespace std;

int main()
{
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	
	int t,r,n,k,test;
	cin>>t;
	for(int p=1;p<=t;p++)
	{
		cin>>r>>k>>n;
		queue<int >q;
		for(int i=0;i<n;i++)
		{
			cin>>test;
			q.push(test);
		}
		//end of i/o
		int euro=0;
		for(int i=0;i<r;i++)
		{
			int ppl=0,s=0;
			while(ppl+q.front()<=k && s++<q.size())
			{
				ppl+=q.front();
				test=q.front();
				q.pop();
				q.push(test);
			}
			euro+=ppl;
			//cout<<i<<"  "<<ppl<<"  "<<euro<<endl;
					
		}
		printf("Case #%d: %d\n",p,euro);
	}
}

