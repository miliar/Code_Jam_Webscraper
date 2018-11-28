//compiled in vc
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <string>
#include <complex>
// C++
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <climits>
#include <ctime>
using namespace std;


char buf[1024];


char re[1024];


int changeToIdx(char c)
{
	switch( c)
	{
		case 'Q': return 1;
		case 'W': return 2;
		case 'E': return 3;
		case 'R': return 4;
		case 'A': return 5;
		case 'S': return 6;
		case 'D': return 7;
		case 'F': return 8;
	}
	return -1;
}
char changeFromIdx(int c)
{
	switch( c)
	{
		case 1: return 'Q';
		case 2: return 'W';
		case 3: return 'E';
		case 4: return 'R';
		case 5: return 'A';
		case 6: return 'S';
		case 7: return 'D';
		case 8: return 'F';
	}
	return -1;
}

char magicMap[256][256];
char nomagicMap[256][256];
int main()
{
	int cases , Case = 1;
	scanf("%d" , &cases);
	
	while( cases-- )
	{
		printf("Case #%d: " , Case++);
		int combin , opp , gogogo;
		
		memset(magicMap , 0 , sizeof(magicMap));
		memset(nomagicMap , 0 , sizeof(nomagicMap)); 

		scanf("%d" , &combin);
		for(int i = 0 ; i < combin ; i++)
		{
			scanf("%s" , buf);

			magicMap[ changeToIdx(buf[0]) ][ changeToIdx(buf[1]) ] = (buf[2]); //com
			magicMap[ changeToIdx(buf[1]) ][ changeToIdx(buf[0]) ] = (buf[2]); //com
		}

		scanf("%d" , &opp);
		for(int i = 0 ; i < opp ; i++)
		{
			scanf("%s" , buf);

			nomagicMap[ changeToIdx(buf[0]) ][ changeToIdx(buf[1]) ] = -1;
			nomagicMap[ changeToIdx(buf[1]) ][ changeToIdx(buf[0]) ] = -1;
		}

		int n;
		scanf("%d" , &n);
		scanf("%s" , buf);
		int reLen = 0;
		int here[10] = {0};
		for(int i = 0 ; i < n ; i++)
		{
			int nowIdx = changeToIdx( buf[i]);
			if( reLen )
			{
				int pre = changeToIdx(re[reLen-1]);

				if( pre > 0 && magicMap[pre][nowIdx] )
				{
					here[ pre]--;
					int to = ( magicMap[pre][nowIdx] );
					re[reLen-1] = to;
					//here[ magicMap[pre][nowIdx] ]++;
				}
				else
				{
					for(int prevIdx = 1; prevIdx < 9 ; prevIdx++)
					{
						if(here[prevIdx])
						{
							if( nomagicMap[prevIdx][nowIdx] == -1 ||
								nomagicMap[nowIdx][prevIdx] == -1 
								)
							{
								reLen = 0;
								memset( here , 0 , sizeof(here));
								goto nextMagic;
							}
						}
					}



					re[reLen++] = buf[i];
					here[ changeToIdx( buf[i] ) ] ++;
				}
			}
			else
			{
				re[reLen++] = buf[i];
				here[ changeToIdx( buf[i] ) ] ++;
			}



			

			nextMagic:;
		}

		printf("[");
		for(int i = 0 ;i< reLen; i++)
		{
			if(i)
				printf(", ");
			printf("%c" , re[i]);
		}
		puts("]");
		
	}







	return 0;
}