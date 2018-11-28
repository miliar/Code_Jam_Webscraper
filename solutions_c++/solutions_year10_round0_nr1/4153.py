#include <string>
#include <vector>
#include <cstring>
#include <cctype>
#include <stack>
#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cstdlib>
#include <cmath>
#include <iostream>
#define MAX 100

using namespace std;

int main()
{
	freopen("input.in", "rt", stdin);
	freopen("output.out", "wt", stdout);

	int T, N, K;
	scanf("%d", &T);
	for(int test = 1; test <= T; test++)
	{
		scanf("%d%d", &N, &K);

		//int cnt = 0;
		/*while(1)
		{
			if((K&01) == 1){
				cnt++;
				K >>= 1;
			}else break;
		}*/

		long int cnt = K & ((1<<N) - 1);
		if(cnt == ((1<<N)-1)) printf("Case #%d: ON\n", test);
		else printf("Case #%d: OFF\n", test);
	}
	return 0;
}