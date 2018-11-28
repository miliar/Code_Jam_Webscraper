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

int N,M,A;


int main()
{
	freopen("B-small-attempt0.in","r",stdin);
	freopen("B-small-attempt0.out","w",stdout);

	//freopen("B-large.in","r",stdin);
	//freopen("B-large.out","w",stdout);
	int T = 0;
	scanf("%d",&T);
	for(int i=0;i<T;i++)
	{
		scanf("%d",&N);
		scanf("%d",&M);
		scanf("%d",&A);
		bool pos = false;

		for(int a=0;a<=N;a++)
		{
			for(int c=0;c<=M;c++)
			{
				for(int b=0;b<=N;b++)
				{
					for(int d=0;d<=M;d++)
					{
						if(b*c-a*d == A)
						{
							printf("Case #%d: 0 0 ",i+1);
							printf("%d %d %d %d\n",a,c,b,d);
							pos = true;
							goto here;
							
						}
					}
				}
			}
		}
		

here:	if(!pos)		
		{
			printf("Case #%d: IMPOSSIBLE\n",i+1);
			
		}
	}
	return 0;
}