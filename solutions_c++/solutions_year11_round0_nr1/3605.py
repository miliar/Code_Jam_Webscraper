#include<cstdio>
#include<queue>
#include<cmath>

using namespace std;

int main()
{
	int t,n,time, boto, botb, k;
	char color;
	queue<int> qboto, qbotb;
	queue<char> com;
	scanf("%d",&t);
	for(int i=0; i<t; i++)
	{
		time = 0;		boto = 1;		botb = 1;
		scanf("%d",&n);
		for(int j=1; j<=n; j++)
		{
			scanf("%c%c %d",&color, &color, &k);			
			//printf("\ttime:%d, Q>O:%d B:%d, L>O:%d B:%d\n",time,qboto.size(), qbotb.size(), boto, botb);
			//printf("\tk=%d\n",k);
			if( color == 'O' )
			{	
				if( qbotb.empty() && j==n )
				{
					while( !qboto.empty() )
					{
						int inq = qboto.front();
						time += 1 + abs(inq-boto);
						boto = inq;
						qboto.pop();
						
						//printf("\t O do\n");
						//printf("%d,%d\n",boto, botb);
						//printf("time:%d\n",time);
					}
					
					time += 1 + (boto > k ? boto-k : k-boto);
					boto = k;
					//printf("\t O do\n");
					//printf("%d,%d\n",boto, botb);
					//printf("time:%d\n",time);
					
				}
				else if( qbotb.empty() && j!=n )
				{
					//printf("\t O wait\n");
					qboto.push(k);
				}
				else
				{
					while( !qbotb.empty() )
					{
						int difftime = 1 + abs(qbotb.front()-botb);
						if( boto != k )
							if( abs(boto-k) <= difftime )
								boto = k;
							else
								boto += k > boto ? difftime : -difftime;
						
						time += difftime;
						botb = qbotb.front();
						qbotb.pop();
						
						//printf("\t B do, O wait\n");
						//printf("%d,%d\n",boto, botb);
						//printf("time:%d\n",time);
					}
					if( j!=n )
						qboto.push(k);
					else
					{
						//if( boto != k )
							time += 1 + abs(boto - k);
						//printf("O do \n");
					}
					/*
					int difftime = 1 + (boto > k ? boto-k : k-boto);
					if( qbotb.front() != botb )
						if( abs(qbotb.front()-botb) <= difftime )
							botb = qbotb.front();
						else
							botb = qbotb.front() > botb ? botb+difftime : botb-difftime;
					
					time += difftime;
					boto = k;
					*/
					
				}
			}
			else
			{
				if( qboto.empty() && j==n )
				{
					while( !qbotb.empty() )
					{
						int inq = qbotb.front();
						time += 1 + abs(inq-botb);
						botb = inq;
						qbotb.pop();
						
						//printf("\t B do\n");
						//printf("%d,%d\n",boto, botb);
						//printf("time:%d\n",time);
					}
				
					time += 1 + (botb > k ? botb-k : k-botb);
					botb = k;
					
					//printf("\t B do\n");
					//printf("%d,%d\n",boto, botb);
					//printf("time:%d\n",time);
				}
				else if( qboto.empty() && j!=n )
				{
					qbotb.push(k);
					//printf("\t B wait\n");
					//printf("%d,%d\n",boto, botb);
				}
				else
				{
					while( !qboto.empty() )
					{
						int difftime = 1 + abs(qboto.front()-boto);
						if( botb != k )
							if( abs(botb-k) <= difftime )
								botb = k;
							else
								botb += k > botb ? difftime : -difftime;
						
						time += difftime;
						boto = qboto.front();
						qboto.pop();

						//printf("\t O do, B wait\n");
						//printf("%d,%d\n",boto, botb);
						//printf("time:%d\n",time);
					}
					
					if( j!=n )
						qbotb.push(k);
					else
					{
						//if( botb != k )
							time += 1 + abs(botb - k);
						//printf("B do\n");
					}
				/*
					int difftime = 1 + (botb > k ? botb-k : k-botb);
					if( qboto.front() != boto )
						if( abs(qboto.front()-boto) <= difftime )
							boto = qboto.front();
						else
							boto = qboto.front() > boto ? boto+difftime : boto-difftime;
					
					time += difftime;
					boto = k;
					printf("\t B para\n");*/
				}
			
				
			}
			
			//printf("%c %d\n",color,k);
		}
		//printf("\ttime:%d, Q>O:%d B:%d, L>O:%d B:%d\n",time,qboto.size(), qbotb.size(), boto, botb);
		printf("Case #%d: %d\n", i+1, time);
	}
	return 0;
}