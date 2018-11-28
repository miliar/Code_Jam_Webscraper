//compiled in vc
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;
#define N 20000000

#define FOR(_a,_b,_c) for(int _a = _b;_a<_c;_a++)


struct Node
{
	char feature[90];
	double val;
	char here;
	//Node( string haha ="" , Node *y =0 , Node *n=0) : feature(haha) , yes(y) , no(n){}
}nodes[1000000];


/*void Del(Node *&a)
{
	if( a->yes)
		Del(a->yes);
	if( a->no)
		Del(a->no);
	delete a;
	a = 0;
}*/

int n , q;
char buf[1024] , b2[1024];
int _stack[1024] , stackPtr;
void readIt(int nIdx = 1)
{
	int prev = 0;
	int cur = 1;

	int i ;
	stackPtr = 0;
	double td;
	for(i=0;i<n;i++)
	{
		gets(buf);

		int len = strlen(buf);
		for(int j=0; j <len;j++)
		{
			if( buf[j] == ' ' ) continue;
			if( buf[j] == '(' )
			{
				_stack[stackPtr++] = cur;
			}
			else if( buf[j] >='0' && buf[j] <= '9' )
			{
				int sht;
				sscanf( buf+j ,"%lf%n" , &td,&sht);
				j+=sht-1;
			}
			else if( buf[j] == ')')
			{
				int s = _stack[--stackPtr];
				if( s == 1 )
				{
					if( !nodes[s].here )
					{
						nodes[s].here = 1;
						nodes[s].val = td;
					}
					continue;
				}
				if( s & 1 )
				{
					if( nodes[s].here == 0 )
					{
						nodes[s].here =1;
						nodes[s].val =td;
					}
					cur = s>>1;
				}
				else
				{
					if( nodes[s].here )
					{
						cur = s+1;
					}
					else
					{
						nodes[s].here =1;
						nodes[s].val =td;
						cur = s+1;
					}
				}
			}
			else
			{
				int sht;
				sscanf( buf+j ,"%s%n" , &b2,&sht);
				j+=sht-1;
				strcpy( nodes[cur].feature , b2);
				nodes[cur].here = 1;
				nodes[cur].val = td;

				cur <<=1;
			}


		}

	}
}


char feat[100][128];


int main()
{
	
	int cases;
	int Case = 0;
	
	int i ,j;

	scanf("%d" , &cases); gets(buf);
	while(cases--)
	{
		scanf("%d" , &n); gets(buf);
		memset(nodes,0,sizeof(nodes));
		readIt();
		scanf("%d" , &q);gets(buf);
		printf("Case #%d:\n" , ++Case);
		while( q-- )
		{
			//gets(buf);
			scanf("%s" , buf);
			int cur = 1;
			int fn;
			double ans = 1;
			scanf("%d" , &fn);
			for(i=0;i<fn;i++)
			{
				scanf("%s" , feat[i]);
			}
			

			while( ( nodes[cur].here ) )
			{
				ans *= nodes[ cur].val;

				for(i=0;i<fn;i++)
				{
					if( !strcmp( nodes[cur].feature , feat[i] ) )
						break;
				}
				if(  i < fn )
						cur <<=1;
					else
					{
						cur <<=1;
						cur++;
					}

			}


			printf("%.7lf\n" , ans);


		}


		
	}




	return 0;
}