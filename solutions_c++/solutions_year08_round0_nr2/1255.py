#include <iostream>
#include <algorithm>

struct SCH
{
	int bg , ed;
	bool dir;
};

bool cmp(SCH a , SCH b)
{
	if( a.bg == b.bg ) return a.ed < b.ed;
	return a.bg < b.bg;
}

SCH q[220];
bool b[220];
int suma , sumb , tt;

int main()
{
	freopen("B-large.in" , "r" , stdin);
	freopen("B-large.out" , "w" , stdout);
	int n , nq , na , nb , bgh , bgm , edh , edm , ca = 1, i , j , cn;
	scanf("%d" , &n);
	while(n--)
	{
		scanf("%d" , &tt);
		scanf("%d%d" , &na , &nb);
		nq = na + nb;
		for( i = 0 ; i < na ; i++)
		{
			scanf("%d:%d %d:%d" , &bgh, &bgm , &edh, &edm);
			q[i].bg = bgh * 60 + bgm;
			q[i].ed = edh * 60 + edm;
			q[i].dir = 1;
		}
		for( i = na ; i < nq ; i++)
		{
			scanf("%d:%d %d:%d" , &bgh, &bgm , &edh, &edm);
			q[i].bg = bgh * 60 + bgm;
			q[i].ed = edh * 60 + edm;
			q[i].dir = 0;
		}
		std::sort(q , q + nq , cmp);
		cn = suma = sumb = 0;
		memset( b , 0 , sizeof(b));
		
		while( cn < nq )
		{
			j = 0;
			while(b[j])j++;
			b[j] = 1;
			cn++;
			if(q[j].dir) suma++;
			else sumb++;
			
			for( i = j + 1 ; i < nq && cn < nq; i++)
			{
				if(b[i] || q[i].dir == q[j].dir) continue;
				if( q[i].bg >= q[j].ed + tt )
				{
					j = i;
					b[j] = 1;
					cn++;
				}
			}
		}
		printf("Case #%d: %d %d\n" , ca , suma , sumb);
		ca++;
		
	}

}

