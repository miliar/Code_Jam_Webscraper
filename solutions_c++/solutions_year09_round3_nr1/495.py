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


char buf[1024];
int mapI[256];

int newO[1024];
int main()
{
	int cases;
	int Case = 0;
	scanf("%d" ,&cases); gets(buf);
	int base;

	while(cases--)
	{
		gets(buf);
		memset(mapI,-1,sizeof(mapI));
		int len = strlen(buf);
		int app = 0;
		for(int i=0;i<len;i++)
		{
			if( mapI[ buf[i] ] ==-1 )
			{
				if( app == 1 )
				{
					mapI[ buf[i] ] = 0;
				}
				else if( app == 0 )
				{
					mapI[ buf[i] ] = 1;
				}
				else
					mapI[ buf[i] ] = app;
				app++;
			}
			newO[i] = mapI[ buf[i] ];
		}
		if( app == 1)
			app++;
		//	puts(buf);

		//printf("%d\n" , app);
		long long  ans = 0;
		for(int i=0;i<len;i++)
		{
			ans *=(long long)app;
			ans += (long long) newO[i];
		}

		printf("Case #%d:" , ++Case);
		printf(" %lld\n" , ans);




	}





	return 0;
}

