#include <iostream>

using namespace std;

int findNext(int robot, int moves[][2], int from, int max)
{
		for(int i = from; i < max; i++)
	{
		if(moves[i][0] == robot)
			return moves[i][1];
	}
	return -1;
}

int main () 
{
	
        int cs = 1;
	int T;
	cin>>T;
	
	int moves[150][2] = {0};
	char ch;
	int N, z;
	
	while(T--)
	{
		cin>>N;
		z = 0;
		
		int time = 0, timeTaken;
		
		int nTemp = N;
		while(nTemp--)
		{
			
			cin>>ch;
			if(ch == 'O')
			{
				moves[z][0] = 0;
			}
			else 
			{
				moves[z][0] = 1;
			}
			
			cin>>moves[z][1];
			z++;
		}
		
		int oPos = 1, bPos = 1;
		int oNext, bNext;
		
		for(z = 0; z < N; z++)
		{
			int cur = moves[z][0];
			oNext = findNext(0, moves, z, N);
			bNext = findNext(1, moves, z, N);
		
			if(cur == 0)
			{
				if(oNext >= oPos)
				{
					timeTaken = (1 + oNext - oPos);
				}
				
				else if(oPos > oNext)
				{
					timeTaken = (1 + oPos - oNext);
					
				}
				
				oPos = oNext;
				
				if(bNext > bPos)
				{
					if(timeTaken >= (bNext - bPos))
					{
						bPos = bNext;
					}
					
					else 
					{
						bPos += timeTaken;
					}
				}
				
				else if((bNext < bPos) && (bNext >= 0))
				{
					if(timeTaken >= (bPos - bNext))
					{
						bPos = bNext;
					}
					else 
					{
						bPos -= timeTaken;
					}
				}
				time += timeTaken;
			}
			else if(cur == 1)
			{
				if(bNext >= bPos)
				{
					timeTaken = (1 + bNext - bPos);
				}
				
				else if(bPos > bNext)
				{
					timeTaken = (1 + bPos - bNext);
				}
				
				bPos = bNext;
				
				if(oNext > oPos)
				{
					if(timeTaken >= (oNext - oPos))
					{
						oPos = oNext;
					}
					
					else 
					{
						oPos += timeTaken;
					}
				}
				else if((oNext < oPos) && (oNext >= 0))
				{
					if(timeTaken >= (oPos - oNext))
					{
						oPos = oNext;
					}
					else
					{
						oPos -=timeTaken;
					}
				}
				time += timeTaken;
			}
		}
		
                cout<<"Case #"<<cs<<": "<<time<<endl;
                cs++;
	}
	
    return 0;
}
