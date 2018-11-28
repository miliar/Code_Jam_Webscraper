/*****************************

******************************/
#include<cstdio>
#include<cstring>
#include<cstdlib>
#include<cctype>

#include<cmath>
#include<iostream>
#include<fstream>

#include<string>
#include<vector>
#include<queue>
#include<map>
#include<algorithm>
#include<set>
#include<sstream>
#include<stack>
using namespace std;

#define FOR(i,n) for( i = 0 ; i<n ; i++)
#define RFOR(i,a,b)  for( i = a ; i<b ; i++)
#define CLR(a) memset(a,0,sizeof(a))
#define MCLR(a) memset(a,-1,sizeof(a))
#define i64 __int64
struct node{
	node(){ k = 0;}
	string s;
	node *next[ 300 ];
	int k;
};
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.ans","w",stdout);
	int tc;
	int n, k, cs = 1;
	cin >> tc;
	while( tc -- )
	{

		node *head = new node();
		head ->s =".";
		cin >> n >> k ;
		int i,ii, t;
		for(ii = 0; ii < n; ii ++ )
		{
			string ss;
			cin >> ss;
			ss =  ss + "/";
		
			string now = "";
			node *p = head;
			bool fl;
			for(i = 1; i < ss.size(); i ++ )
			{
				
				if(ss[ i ] == '/' )
				{
					fl = 1;
			
					for(t = 0; t < (p-> k) ; t ++ )
						if( p -> next[ t ] -> s == now )
						{
							p = p -> next[ t ];
							fl = 0;
							break;
						}
					
					
					if( fl )
					{
						p -> next[ p-> k ] = new node();
						p -> next[ p-> k ] -> s = now;
						p -> k ++;
						p = p -> next[ p-> k - 1 ];
					}
					now = "";
				}
				else now += ss[ i ];
				
			}

		}
		int cnt = 0;
		for(ii = 0; ii < k; ii ++ )
		{
			string ss;
			cin >> ss;
			ss =  ss + "/";
			
			string now = "";
			node *p = head;
			bool fl;
			for(i = 1; i < ss.size(); i ++ )
			{
				
				if(ss[ i ] == '/' )
				{
					fl = 1;
				
					for(t = 0; t < (p-> k) ; t ++ )
						if( p -> next[ t ] -> s == now )
						{
							p = p -> next[ t ];
							fl = 0;
							break;
						}
					
					if( fl )
					{
						p -> next[ p-> k ] = new node();
						p -> next[ p-> k ] -> s = now;
						p -> k ++;
						cnt ++;
						p = p -> next[ p-> k - 1 ];
					}
					now = "";
				}
				else now += ss[ i ];
			
				
			}

		}
		printf("Case #%d: %d\n",cs ++, cnt );
	}
	return 0;
}