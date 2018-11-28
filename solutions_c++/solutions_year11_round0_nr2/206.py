#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

const int MaxN = 110;

char G[MaxN][MaxN];
bool rev[MaxN][MaxN];
char stk[MaxN];

int main()
{
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	
	
	int T;	cin >> T;
	for(int cas=1; cas<=T; cas++)
	{
		memset(G, 0, sizeof(G));
		int C;	cin >> C;
		while(C --)
		{
			string str;
			cin >> str;
			G[str[0]][str[1]] = str[2];
			G[str[1]][str[0]] = str[2];	
		}	
		
		memset(rev, 0, sizeof(rev));
		int D;	cin >> D;
		while(D --)
		{
			string str;
			cin >> str;
			rev[str[0]][str[1]] = rev[str[1]][str[0]] = 1;		
		}
		
		int N;	cin >> N;
		string str;	cin >> str;
		int top = 0;
		for(int i=0; i<N; i++)
		{
			if(!top)	stk[top++] = str[i];
			else
			{
				if(G[stk[top-1]][str[i]])	
				{
					stk[top-1] = G[stk[top-1]][str[i]];	
				}
				else
				{
					stk[top++] = str[i];
					for(int j=top-2; j>=0; j--)
					{
						if(rev[stk[j]][str[i]])
						{
							top = 0;
							break;	
						}	
					}	
				}
			}	
		}
		
		printf("Case #%d: [", cas);
		for(int i=0; i<top-1; i++)
		{
			printf("%c, ", stk[i]);	
		}
		if(top)	printf("%c]\n", stk[top-1]);
		else	puts("]");
	}
	
	
	return 0;	
}
