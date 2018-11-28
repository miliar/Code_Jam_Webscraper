#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <climits>
#include <cassert>
#include <string>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <sstream>
#include <numeric>
#define MAX_LONG_LONG 9223372036854775807
#define MAX_INT  2147483647
#define MAX_LONG 2147483647
using namespace std;

typedef long long int64;
typedef unsigned long long uint64;

char buff[50];


void solve(char x[], char tmp[])
{
//	sprintf(buff, "%lld", x);
	//char *tmp = new char[50];
	int index = -1;
	for(int i = strlen(buff)-1; i > 0; i --)
	{
		if(buff[i] > buff[i-1])
		{
			index = i - 1;
			break;
		}
	}
	
	if(index == -1)
	{
		memcpy(tmp + 1, buff, (strlen(buff) + 1)*sizeof(char));

		tmp[0] = '0';
		index = 0;
	}
	else
	{
		memcpy(tmp, buff, (strlen(buff)+1)*sizeof(char));

	}
	sort(tmp + index + 1, tmp + strlen(tmp));

	for(int i = index + 1; i < strlen(tmp); i ++)
	{
		if(tmp[i] > tmp[index])
		{
			char m = tmp[i];
			tmp[i] = tmp[index];
			tmp[index] = m;
			break;
		}
	}

}

int main() {
	freopen("..//input.txt", "rt", stdin);
	freopen("..//output.txt", "wt", stdout);
	int tc; 
	scanf("%d", &tc);
	char x[50];
	char tmp[50];

	for(int t = 1; t <= tc; t ++)
	{
		scanf("%s", buff);
		solve(x, tmp);
		printf("Case #%d: %s\n", t, tmp);
	}
}
