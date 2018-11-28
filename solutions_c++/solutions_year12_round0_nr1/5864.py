// program.cpp : Defines the entry point for the console application.
//

#include <stdio.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <deque>
#include <math.h>
using namespace std;

char sub[26] = {'y','h','e','s','o','c','v','x','d','u','i', \
                'g','l','b','k','r','z','t','n','w','j','p', \
				'f','m','a','q'};

int main()
{
	int tc;
    
	freopen( "C:\\Users\\Amit\\Downloads\\A-small-attempt2.in", "r", stdin );
	freopen( "A-small-attempt0.txt", "w", stdout );

	scanf( "%d\n", &tc );
    
	for( int i = 1; i <= tc; ++i )
	{
		printf( "Case #%d:", i );
        char buf[100005];
		fgets(buf, 100005, stdin );
        int len=strlen(buf);
		for(int j=0;j<len; ++j)
		{
           char c = buf[j];
		   if(c != ' ')
             buf[j] = sub[c-97];
		}

		printf(" %s\n", buf);
	}
	return 0;
}

