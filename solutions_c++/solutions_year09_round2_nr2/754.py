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
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define N 20000000

#define FOR(_a,_b,_c) for(int _a = _b;_a<_c;_a++)


int readlineofint(int a[] , char intc[])
{
	int i , n;
	char *tok = intc;

	while( sscanf( tok,"%d%n" , &a[i] , &n)!=EOF )
	{
		tok += n;
		i++;
	}

	return i;
}


char buf[1024] , b2[1024];
int main()
{
	int cases , Case = 0;
	int len;
	int i;

	scanf("%d" , &cases);
	gets(buf);
	while( cases-- )
	{
		gets(buf);
		strcpy( b2, buf);
		len = strlen(buf);
		std::next_permutation( buf , buf+len );
		for(i = 0; i<len;i++)
		{
			if( buf[i] != b2[i])
			{break;
			}
		}

		if( !b2[i] || buf[i] < b2[i])
		{
			//printf("%s" , b2);
			std::sort( b2 , b2+len);
			memset(buf, '0' , sizeof(buf));
			int idx = 2;
			for(i=0;i<len;i++)
			{
				if( b2[i]!='0')
					break;
				idx++;
			}
			buf[len+1] = 0;
			buf[0] = b2[i++];
			for(;i<len;i++)
			{
				buf[idx++] = b2[i];
			}
			//printf("aa");
			buf[len+1] = 0;
		}

		printf("Case #%d: " , ++Case);

		printf("%s\n" , buf);

	}


	return 0;
}