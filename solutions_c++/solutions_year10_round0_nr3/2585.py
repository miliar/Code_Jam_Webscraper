#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;

int main()
{
	freopen("in3.txt","r",stdin);
	freopen("out3.txt","w",stdout);
	int t,ca=1;
	int r,k,n;
	int a,b;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d%d%d",&r,&k,&n);
		deque<int> q1;
		while(n--)
		{
			scanf("%d",&a);
			q1.push_back(a);
		}
		long long ans=0;
		while(r--)
		{
			int num=0;
			deque<int> q2;
			while(num<k && !q1.empty())
			{
				if(num+q1.front()<=k)
				{
					q2.push_back(q1.front());
					num+=q1.front();
					q1.pop_front();
				}
				else break;
			}
			ans+=num;
			q1.insert(q1.end(),q2.begin(),q2.end());
		}
		printf("Case #%d: %lld\n",ca++,ans);
	}
	return 0;
}