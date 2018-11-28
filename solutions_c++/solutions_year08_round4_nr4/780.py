/*
	Problem		::	B
	Date		::	2nd August, 2008
	Author		::	MIB
	Environment	::	Microsoft Visual Studio 2005
*/

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cctype>
#include <cmath>
#include <cassert>
#include <algorithm>
#include <stack>
#include <queue>
#include <vector>

using namespace std;

typedef __int64 i64;
const int INF = 0x7F7F7F7F;

int R, C;

#define mini(x,y) ((x)<(y)?(x):(y))
#define maxi(x,y) ((x)>(y)?(x):(y))
#define valid(x,y) ((x)>=0 && (x)<R && (y)>=0 && (y)<C)
#define CLR(x, v) memset((x), (v), sizeof((x)))


class compare_desc
{
	public:
	bool operator () (const int &obj1, const int &obj2)
	{
		return obj1 > obj2;	
	}
};


const int MAX = 1005;
char arr[MAX], str[MAX];
int num[20];


int compute(char * s, int len)
{
	int i;

	if(len == 1)
		return 1;

	int res = 1;

	for(i=1; i<len; i++)
	{
		if(s[i-1] != s[i])
			res++;
	}

	return res;
}

int main(void)
{
	// freopen( "..//..//codejam//D-small.in", "rt", stdin );
	// freopen( "..//..//codejam//D-small.out", "wt", stdout );

	int t, test;

	int i, j, k;
	int res, temp, len;

	scanf( " %d" ,&test);

	for(t=1; t<=test; t++)
	{
		scanf( " %d " ,&k);

		for(i=0; i<k; i++)
			num[i] = i;

		gets(arr);
		len = strlen(arr);

		res = compute(arr, len);

		while(next_permutation(num, num+k))
		{
			for(i=0; i<len; i+=k)
			{
				for(j=0; j<k; j++)
					str[i+j] = arr[i+num[j]];
			}

			temp = compute(str, len);
		
			if(temp < res)
				res = temp;
		}

		printf( "Case #%d: %d\n" ,t ,res);	
	}

	return 0;
}