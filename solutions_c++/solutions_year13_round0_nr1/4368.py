
#include <iostream>
#include <sstream>
#include <cstdio>
#include <climits>
#include <cstdlib>
#include <algorithm>
#include <cmath>
#include <cstring>
#include <string>
#include <map>
#include <set>
#include <stack>
#include <list>
#include <vector>
#include <queue>
 
using namespace std;
#define VI vector < int >
#define LL long long
#define LLU unsigned long long int
#define SI ({int x;scanf("%d",&x);x;})
#define SC ({char x;scanf("%c",&x);x;})
#define SLL ({LL x;scanf("%lld",&x);x;})
#define SLLU ({LLU x;scanf("%llu",&x);x;})
#define INF 1000000007

int main()
{
	int t = SI;
	char a[4][4], temp;
	int i, j, k;
	
	int countx , counto, flag, ct = 1, done;
	
	int abc = t;
	for(k=1; k<=abc; k++)
	{
		
		done = 0;
		for(i=0; i<4; i++)
		{
			scanf("%s", a[i]);
		}
		
	
		flag = 0;
	
		for(i=0; i<4; i++)
		{
			counto = 0;
			countx = 0;
			for(j=0; j<4; j++)
			{
				if(a[i][j] == '.')
				{
					flag = 1;
				}
				else if(a[i][j] == 'X')
				{
					countx++;
				}
				else if(a[i][j] == 'O')
				{
					counto++;
				}
				else if(a[i][j] == 'T')
				{
					counto++;
					countx++;
				}
			}
			if(countx==4)
			{
				printf("Case #%d: X won\n",k );
				done =1;
				break;
			}
			if(counto ==4)
			{
				printf("Case #%d: O won\n",k );
				done =1;
				break;
			}
		}
		if(done)
		{
			
			continue;
		}

		for(j=0; j<4; j++)
		{
			counto = 0;
			countx = 0;
			for(i=0; i<4; i++)
			{
				if(a[i][j] == 'X')
				{
					countx++;
				}
				else if(a[i][j] == 'O')
				{
					counto++;
				}
				else if(a[i][j] == 'T')
				{
					counto++;
					countx++;
				}
			}
			if(countx==4)
			{
				printf("Case #%d: X won\n",k );
				done =1;
				break;
			}
			if(counto ==4)
			{
				printf("Case #%d: O won\n",k );
				done =1;
				break;
			}
		}
		if(done)
			continue;
		
		counto = 0;
		countx = 0;
			
		for(i=0; i<4; i++)
		{
				if(a[i][i] == 'X')
				{
					countx++;
				}
				else if(a[i][i] == 'O')
				{
					counto++;
				}
				else if(a[i][i] == 'T')
				{
					counto++;
					countx++;
				}
		}
		if(countx==4)
		{
			printf("Case #%d: X won\n",k );
			done =1;
		
		}
		if(counto ==4)
		{
			printf("Case #%d: O won\n",k );
			done =1;
		
		}
		if(done)
			continue;

		counto = 0;
		countx = 0;
			
		for(i=0; i<4; i++)
		{
				if(a[i][3-i] == 'X')
				{
					countx++;
				}
				else if(a[i][3-i] == 'O')
				{
					counto++;
				}
				else if(a[i][3-i] == 'T')
				{
					counto++;
					countx++;
				}
		}
		if(countx==4)
		{
			printf("Case #%d: X won\n",k );
			done =1;
		
		}
		if(counto ==4)
		{
			printf("Case #%d: O won\n",k );
			done =1;
		
		}
		if(done)
			continue;

		if(flag)
			printf("Case #%d: Game has not completed\n",k);
		else
			printf("Case #%d: Draw\n",k);

		ct++;
	}
	return 0;
}
