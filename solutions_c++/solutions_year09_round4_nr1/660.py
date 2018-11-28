#include <iostream>
#include <algorithm>
#include <bitset>
#include <string>
#include <string.h>
#include <stdlib.h>
#include <map>
#include <vector>
#include <queue>
#include <cmath>
using namespace std;


#define MAXN 1700001
unsigned int BKDRHash(char* str)
{
    unsigned int seed = 131 ; 
    unsigned int hash = 0 ;
    while (*str)
    {
        hash = hash*seed + (*str ++ );
    }
    return (hash & 0x7FFFFFFF );
}

int hash[MAXN];
inline bool hashit(char *str)
{
    int k,t;
    //while( *str == '0' )    str++;
    k = BKDRHash(str);
    t = k % MAXN;
    while( hash[t] != k && hash[t] != -1 )
        t = ( t + 10 ) % MAXN;
    if( hash[t] == -1 ) {
		hash[t] = k;
		return 0;
	}
	else return 1;
}
int n;
char str[100][100];
bool can(int index, int k)
{
	int i, j;
	for(i = k + 1; i < n; i ++)
	{
		if( str[index][i] == '1')
			return false;
	}
	return true;
}	
char tmp[100];
int main()
{
	int i, j, k,t, cas = 0;
	freopen("A-large.in","r", stdin);
	freopen("outl.txt","w",stdout);
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d", &n);
		for(i = 0 ; i < n; i ++)
			scanf("%s", &str[i]);
		int count = 0;
		for( i = 0; i < n; i ++)
		{
			int index = -1;
			for(j = i; j < n; j ++)
			{
				if( can(j, i) )
				{
					count += j - i;
					index = j;
					break;
				}
			}
			strcpy(tmp, str[index]);
			for(; j > i; j --)
			{
				strcpy(str[j], str[j-1]);
			}
			strcpy(str[i], tmp);
		}
		printf("Case #%d: %d\n", ++cas, count);
	}
	
}