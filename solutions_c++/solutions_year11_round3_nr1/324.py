#include <set>   
#include <deque>   
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
#include <ctime>   
#include <queue>   
#include <map> 
#include <string.h> 
#include <queue> 
using namespace std;


/*  
bool arr[N];  
void getprim(){ arr[0]=1;arr[1]=1;int i;long long j;for(i=2;i<N;i++){if(arr[i]==0){ for(j=i,j=j*i;j<N;j+=i){arr[j]=1;}}}}  
*/  
//priority_queue  
//lower_bound,upper_bound  
//#define vs vector<string>
//#define N 4500005
//#define vi vector<int>
//typedef long long ll;
//next_permutation

//bool cmp(int a,int b)//从小到大
//{
//	return a<b;
//}

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <algorithm>

using namespace std;

#define N  100
#define M  100
int n, m;
char g[N][M];
bool rep(int x, int y)
{
    if(x == n - 1 || y == m - 1) return false;
    if(g[x][y+1] == '#' && g[x+1][y] == '#' && g[x+1][y+1] == '#')
        return true;
    return false;
}
int main()
{
    freopen("1.in", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; cas++)
	{
        scanf("%d%d", &n, &m);
        for(int i = 0; i < n; i ++)
		{
            scanf("%s", g+ i);
        }
        bool over = false;

        for(int i = 0; i < n && !false; i ++)
		{
            for(int j = 0; j < m && !false; j ++)
			{
                if(g[i][j] == '#')
				{
                    if(rep(i, j))
					{
                        g[i][j] = '/';
                        g[i][j+1] = '\\';
                        g[i+1][j] = '\\';
                        g[i+1][j+1] = '/';
                    }
                    else over = true;
                }
            }
        }
        printf("Case #%d:\n", cas);
        if(over) puts("Impossible");
        else
		{
            for(int i = 0; i < n; i ++)
			{
                puts(g[i]);
            }
        }
    }
    return 0;
}
