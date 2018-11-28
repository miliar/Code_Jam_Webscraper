#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <ctime>

using namespace std;

int main()
{
	int T;
	scanf("%d", &T);
	
	for(int caso=1; caso<=T; caso++)
	{
		int N, S, p, cnt = 0;
		scanf("%d %d %d", &N, &S, &p);
		
		for(int i=0; i<N; i++)
		{
			int tot;
			scanf("%d", &tot);
			
			int a = tot/3, b = tot/3, c = tot/3;
			if(tot % 3 == 1) a++;
			if(tot % 3 == 2) a++, b++;
			
			if(a >= p) cnt++;
			else if(a == b && b >= 1 && S >= 1 & a + 1 >= p) cnt++, S--;
		}
		
		printf("Case #%d: %d\n", caso, cnt);
	}
	
	return 0;
}
