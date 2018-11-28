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




char input[128][128];
char output[128][128];
int r , c;

int main()
{
	int cases , Case = 1;
	scanf("%d" , &cases);

	
	while( cases-- )
	{
		printf("Case #%d:\n " , Case++);   
		scanf("%d%d" , &r,&c);
		memset( input , 0 , sizeof(input));
		int isOk = 1;
		for(int i=0;i<r;i++)
		{
			scanf("%s" , &input[i]);
			int total = 0;
			for(int j = 0 ; j < c && isOk; j++)
			{
				if( input[i][j] == '#') total++;
			}
			if( total&1) isOk = 0;
		}

		if( !isOk)
			puts("Impossible");
		else
		{
			memset( output , 0 , sizeof(output));
			
			for(int i=0;i<r;i++)
			{
				for(int j = 0 ; j < c ; j++)
				{
					if( input[i][j] == '#')
					{
						if(  input[i][j+1] == '#' &&
							input[i+1][j+1] == '#' && input[i+1][j] == '#')
						{
							input[i][j] = input[i][j+1] =  input[i+1][j+1] =input[i+1][j] = 0;
							output[i][j] = '/';
							output[i][j+1] = '\\';
							output[i+1][j+1] = '/';
							output[i+1][j] = '\\';
						}
						else 
						{
							isOk = 0;
						}
					}
					else if( input[i][j] == '.' )
						output[i][j] = input[i][j];
				}

			}

			if( !isOk)
			puts("Impossible");
			else
			{
		
			for(int i=0;i<r;i++)
				puts(output[i]);
			}
		}

	}

	return 0;
}
