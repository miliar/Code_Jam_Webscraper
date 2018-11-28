#include <cstdio>
#include <iostream>
#include <string>
#include <cstring>

#define N 256

using namespace std;

char repl[N][N];
bool rep_bool[N][N], ref[N][N];
char que[N];
string str;

int main()
{
	int t;
	cin >> t;	

	for (int j = 0; j < t; j++)
	{
		int c, d, n, l = -1, r = -1;

		memset(rep_bool, 0, sizeof(rep_bool));
		memset(ref, 0, sizeof(ref));

		cin >> c;
		for (int i = 0; i < c; i++)
		{
			cin >> str;
			repl[ str[0] ][ str[1] ] = repl[ str[1] ][ str[0] ] = str[2];
			rep_bool[ str[0] ][ str[1] ] = rep_bool[ str[1] ][ str[0] ] = true; 
		}

		cin >> d;
		for (int i = 0; i < d; i++)
		{
			cin >> str;
			ref[ str[0] ][ str[1] ] = ref[ str[1] ][ str[0] ] = true;			
		}

		cin >> n;
		for (int i = 0; i < n; i++)
		{
			char sym; 

			cin >> sym;
			bool ok = true;

			if (l < r)
			{
				if (rep_bool[sym][ que[r] ])
				{
					que[r] = repl[sym][ que[r] ];
					ok = false;
				}
				else
        		{
        			for (int k = l + 1; k <= r; k++)
        			{
        				if (ref[sym][ que[k] ])
        				{
        					l = r;

        					ok = false;
        					break;
        				}
        			}
        		}
			}

			if (ok)
        	{
       			que[++r] = sym;
       		}	
		}

		printf("Case #%d: [", j + 1);

		for (int i = l + 1; i <= r; i++)
		{
			printf("%c%c ", que[i], "],"[i < r] );
		}

		if (l >= r)
		{
			printf("]");
		}

		puts("");
	}

	return 0;
}
