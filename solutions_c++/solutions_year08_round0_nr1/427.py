//////////
//
//	Auther: hazy
//	Pro ID:	
//	Pro Profile:  
//	Created @ 2008_6
//
//////////
#include <cstdio>
#include <cstring>
#include <utility>
#include <algorithm>
using namespace std;
const int MAXS = 110;
const int MAXQ = 1010;
const int MAXLEN = 200;

int 	cas, T = 0;

int 	s, q;
char	eng[MAXS][MAXLEN], qry[MAXQ][MAXLEN], buff[MAXLEN];
int 	pre[MAXS], next[MAXS];

int main()
{
	int 	i, j, k;
	
	freopen("A-large.in", "r", stdin);
	freopen("a_large.txt", "w", stdout);
	
	for (scanf("%d", &cas); cas; cas--)
	{
		scanf("%d", &s);
		gets(buff);
		for (i=0; i<s; i++)
			gets(eng[i]);
		scanf("%d", &q);
		gets(buff);
		for (i=0; i<q; i++)
			gets(qry[i]);
		
		memset(pre, 0, sizeof(pre));
		memset(next, 0x7f, sizeof(next));
		for (i=0; i<q; i++)
		{
			for (j=0; j<s; j++)			//	pre
			{
				if (strcmp(eng[j], qry[i]) == 0)	continue;
				
				for (k=0; k<s; k++)		//	next
				{
					int 	temp = (j == k ? pre[k]:(pre[k]+1));
					next[j] = (temp<next[j] ? temp:next[j]);			
				}
			}
			
			memcpy(pre, next, sizeof(next));
			memset(next, 0x7f, sizeof(next));	
		}
		
		int 	rnt = 1 << 20;
		for (i=0; i<s; i++)
			rnt = (pre[i] < rnt ? pre[i]:rnt);
		
		printf("Case #%d: %d\n", ++T, rnt);
	}
	return 0;
}
