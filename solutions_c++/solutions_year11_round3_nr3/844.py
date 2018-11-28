#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <fstream>
#include <numeric>
#include <iomanip>
#include <bitset>
#include <list>
#include <stdexcept>
#include <functional>
#include <utility>
#include <ctime>
using namespace std;

int cases;
int curcase;
int N,L,H;

int num[10000];

bool hexie(int a)
{
	for(int i = 0; i<N; i++){
		if(num[i] % a != 0 && a % num[i] != 0)
			return false;
	}

	return true;
}

int main()
{
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("out.txt", "w", stdout);

	scanf("%d", &cases);
	curcase = 1;

	while (curcase <= cases)
	{
		scanf("%d%d%d", &N, &L, &H);
		for(int i=0; i<N; i++)
			scanf("%d", &num[i]);

		int ans = -1;
		for(int i=L; i<=H; ++i){
			if(hexie(i))
			{
				ans = i;
				break;
			}
		}

		printf("Case #%d: ", curcase);
		if(ans == -1)
			printf("NO\n");
		else
			printf("%d\n", ans);
		curcase ++;
	}
}
