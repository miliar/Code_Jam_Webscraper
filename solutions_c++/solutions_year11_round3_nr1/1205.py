#include <cstdio>
#include <algorithm>
#include <utility>
#include <vector>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <sstream>
#include <ctime>
#include <cstring>
#include <cstdlib>
#include <cmath>

#define INF 2000000000
#define EPS 1e-11
#define MAX_N 100002
using namespace std;

#ifdef _WIN32 
typedef __int64 int64; 
#else 
typedef long long int64; 
#endif 

int
main()
{
	int T,R,C;
	bool cek;
	char petak[55][55];
	scanf("%d", &T);
	for(int tc = 1;tc <= T;tc++)
	{
		scanf("%d %d", &R, &C);
		for(int i = 0;i < R;i++)
		{
			scanf("%s", petak[i]);
		}
		cek = true;
		for(int i = 0;i < R;i++)
		{
			for(int j = 0;j < C;j++)
			{
				if(petak[i][j] == '#')
				{
					//region 1
					if(i-1 >= 0 && j-1 >= 0 && petak[i-1][j-1] == '#' && petak[i][j-1] == '#' && petak[i-1][j] == '#')
					{
							petak[i][j] = '/';
							petak[i-1][j-1] = '/'; 
							petak[i][j-1] = '\\'; 
							petak[i-1][j] = '\\';
					}
					else if(i-1>=0 && j+1 < C && petak[i-1][j+1] == '#' && petak[i][j+1] == '#' && petak[i-1][j] == '#')
					{
							petak[i][j] = '\\';
							petak[i-1][j+1] = '\\'; 
							petak[i][j+1] = '/'; 
							petak[i-1][j] = '/';
					}
					else if(i+1<R && j-1 >= 0 && petak[i+1][j-1] == '#' && petak[i][j-1] == '#' && petak[i+1][j] == '#')
					{
							petak[i][j] = '\\';
							petak[i][j-1] = '/'; 
							petak[i+1][j] = '/'; 
							petak[i+1][j-1] = '\\';				
					}
					else if(i+1<R && j+1 < C && petak[i+1][j+1] == '#' && petak[i][j+1] == '#' && petak[i+1][j] == '#')
					{
							petak[i][j] = '/';
							petak[i][j+1] = '\\'; 
							petak[i+1][j] = '\\'; 
							petak[i+1][j+1] = '/';				
					}
					else
					{
						cek = false;
						break;
					}
				}
			}
			if(cek == false)break;
		}
		printf("Case #%d:\n",tc);
		if(cek)
		{
			for(int i = 0;i < R;i++)
			{
				for(int j = 0;j < C;j++)
				{
					printf("%c", petak[i][j]);
				}
				printf("\n");
			}
		}
		else printf("Impossible\n");
	}
return 0;
}