#include <iostream>
#include <cmath>
#include <string>
#include <sstream>
#include <algorithm>
#include <iomanip>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <fstream>

using namespace std;

int main()
{
	FILE* fin = freopen("a_in.txt","r",stdin);
	freopen("a_out.txt","w+",stdout);

	int T;
	scanf("%d", &T);
	for(int i=0; i < T; ++i)
	{
		int n, k;
		scanf("%d %d", &n, &k);
		int p = k%(int)powf(2,n);
		
		if( p == 0 )
		{
			printf("Case #%d: OFF\n",i+1);
			continue;
		}

		int b = logf(p)/logf(2) +1;
		if( b < n )
		{
			printf("Case #%d: OFF\n",i+1);
			continue;
		}
		
		if( powf(2,b)-1 == p )
			printf("Case #%d: ON\n",i+1);
		else
			printf("Case #%d: OFF\n",i+1);
	}
	return 0;
}