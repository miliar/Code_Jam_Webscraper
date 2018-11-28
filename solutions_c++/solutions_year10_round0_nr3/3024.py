#include <iostream>
#include <queue>

using namespace std;

int main()
{
	int t;
	scanf("%d",&t);
	
	long R,k,g,count;
	long left;
	
	int N;
	long cost=0;
	
	queue<long> line;
	
	for(int i=0;i<t;i++)
	{
		scanf("%ld",&R);
		scanf("%ld",&k);
		scanf("%d",&N);
		
		/* Input the line */
		for(int j=0;j<N;j++)
		{
			scanf("%ld",&g);
			line.push(g);
		}
		
		
		for(long run=0;run<R;run++)
		{
			left = k;
			long* p = &(line.front());
			
			count = 0;
			//while( (left >= (*p)) && (count < g) )
			for(long loop = 0;loop < N ; loop++)
			{
				left = left-(*p);
				cost += (*p);
				
				line.push((*p));
				line.pop();
				p = &(line.front());
				
				if(left < (*p))
					break;
				
			}
			//cout<<left<<"---"<<cost<<"\n";
		}
		
		printf("Case #%d: %ld\n",(i+1),cost);
		
		while(!line.empty())
			line.pop();
		
		//fflush(stdin);
		cost = 0;
		
	}
	return 0;
}
