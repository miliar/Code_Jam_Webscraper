// program1.cpp : Defines the entry point for the console application.
//
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <memory.h>
#include <assert.h>
#include <algorithm>
#include <functional>
#include <vector>
#include <string.h>
#include <map>
#include <set>
#include <deque>
#include <math.h>
using namespace std;


int main()
{
	int tc;
	freopen( "C:\\Users\\Amit\\Downloads\\C-small-attempt1.in", "r", stdin );
	freopen( "C-small-attempt1.txt", "w", stdout );

	scanf( "%d\n", &tc );
	
	for( int t = 1; t <= tc; ++t )
	{
		set<pair<int,int>> st;
		printf( "Case #%d:", t );
        int a,b;
        scanf( "%d", &a );
		scanf( "%d", &b );
        
        for(int n=a; n<=b; ++n)
		{
           char buf[1000];
		   itoa(n,buf,10);
		   int len = strlen(buf);		   
		   for(int k=1; k<len; ++k)
		   {
               char str1[1000];
			   char str2[1000];
               char str[1000];
			   strncpy(str1, buf, k);
			   str1[k] = '\0';
			   strncpy(str2, buf+k, len-k);
			   str2[len-k] = '\0';
			   strcpy(str, str2);
			   strcat(str, str1);
			   if(str[0] != '0'){
     			   int m = atoi(str);
				   if(m <= b && m > n)
				   {
					   pair<int,int> p(n,m);
					   st.insert(p);
				   }
			   
		   }
		} 		   
	}
		printf(" %d\n", st.size());
		
}
	return 0;
}

