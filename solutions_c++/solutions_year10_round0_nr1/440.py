#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <map>
#include <set>
#include <iterator>
#include <algorithm>
#include <queue>
#include <functional>
#include <sstream>
#include <complex>
#include <ctype.h>
#include <math.h>
#include <stdlib.h>
#include <ctime>
#include <iomanip>
#include <time.h>

using namespace std;


#ifdef ONLINE_JUDGE
void init()
{
}
#else
FILE* inputstream;
FILE* outputstream;
void init()
{
	inputstream = freopen("in.txt", "r", stdin);
	outputstream = freopen("output.txt", "w", stdout);
}
#endif

int main()
{
	init();
	int a, b;
	int cases;
	scanf("%d", &cases);
	for (int i = 1; i <= cases; ++i)
	{
		printf("Case #%d: ", i);
		int n, k;
		scanf("%d %d", &n, &k);
		if (k % (1 << n) == ((1 << n) - 1))
		{
			printf("ON");
		}
		else
		{
			printf("OFF");
		}
		printf("\n");
	}
	return 0;
}
