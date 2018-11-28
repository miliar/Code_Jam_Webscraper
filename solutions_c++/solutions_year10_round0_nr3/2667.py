#include <iostream>
#include <queue>
using namespace std;

int main(void)
{
	freopen("C-small-attempt5.in","r",stdin);
	freopen("C-small-out.out","w",stdout);
	int T,R,k,n;
	int C = 1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d %d %d",&R,&k,&n);
		queue <int> que;
		for ( int i = 0; i < n; i++ )
		{
			int num;
			scanf("%d",&num);
			que.push(num);
		}
		int res = 0;
		while(R--)
		{
			int sum = 0;
			queue <int> pend;
			while( !que.empty() )
			{
				int top = que.front();
				if ( sum+top>k )
					break;
				que.pop();
				sum += top;
				pend.push(top);
			}
			res += sum;
			while( !pend.empty() )
			{
				que.push( pend.front() );
				pend.pop();
			}
		}
		printf("Case #%d: %d\n",C++,res);
	}
//	system("pause");
	return 0;
}