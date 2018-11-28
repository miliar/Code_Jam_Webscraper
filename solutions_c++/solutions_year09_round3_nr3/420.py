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


int l[10];

int vis[128] , TRUE = 1;

int main()
{
	int cases;
	int Case = 0;
	scanf("%d" ,&cases); 

	int n ;
	int q;
	int i,j ;

	while(cases--)
	{
		scanf("%d%d"  , &n , &q);
		for(i=0;i<q;i++)
		{
			scanf("%d" , &l[i]);
		}
		int minn = 0x7FFFFFFF;
		
		do
		{
			int cur  = 0;
			for(i=0;i<q;i++)
			{
				vis[l[i]]=TRUE;
				for(j=l[i]-1; j>0;j--)
				{
					if( vis[j] ==TRUE )
						break;
					cur++;
				}
				for(j=l[i]+1; j<=n;j++)
				{
					if( vis[j] ==TRUE )
						break;
					cur++;
				}

			}
			if( cur < minn )
			minn = cur;

			TRUE++;
		}while( std::next_permutation( l , l+q));


		printf("Case #%d:" , ++Case);
		printf(" %d\n" , minn);
	}





	return 0;
}

