#include <cstdio>
#include <queue>

using namespace std;

struct node_t
{
	int s;
	int t;
	int st;
	bool operator<(const node_t &v1) const
	{
		return s>v1.s;
	}
};

int main()
{
	priority_queue<node_t> qS,qA,qB;
	int N,NA,NB,T;
	int h1,m1,h2,m2;
	node_t C,C1,C2;
	scanf("%d ",&N);
	for(int X=1;X<=N;X++)
	{
		scanf("%d %d %d ",&T,&NA,&NB);
		for(int i=0;i<NA;i++)
		{
			scanf("%d:%d %d:%d ",&h1,&m1,&h2,&m2);
			C.s = h1*60+m1;
			C.t = h2*60+m2;
			C.st = 1;
			qS.push(C);
		}
		for(int i=0;i<NB;i++)
		{
			scanf("%d:%d %d:%d ",&h1,&m1,&h2,&m2);
			C.s = h1*60+m1;
			C.t = h2*60+m2;
			C.st = 2;
			qS.push(C);
		}
		int countA = 0,countB = 0;
		while(!qS.empty())
		{
			C = qS.top(); qS.pop();
			//printf("%d %d %d\n",C.s,C.t,C.st);
			if(C.st == 1)
			{
				if(!qA.empty())
				{
					C1 = qA.top();
					if(C.s < C1.s)
						countA++;
					else
						qA.pop();
				}
				else
					countA++;
				C.s = C.t + T;
				qB.push(C);
			}
			else
			{
				if(!qB.empty())
				{
					
					C1 = qB.top();
					//printf("x %d %d\n",C.s,C1.t);
					if(C.s < C1.s)
						countB++;
					else
						qB.pop();
				}
				else
					countB++;
				C.s = C.t + T;
				qA.push(C);
			}
		}
		while(!qA.empty())
			qA.pop();
		while(!qB.empty())
			qB.pop();
		printf("Case #%d: %d %d\n",X,countA,countB);
			
	}
	return 0;
}
