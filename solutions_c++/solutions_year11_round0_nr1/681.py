#include<iostream>
#include<cmath>
#include<stdio.h>
#include<cstring>
#include<map>
#include<algorithm>
using namespace std;
const int N = 1510 ;
const int M = 10001 ;
const int INF = 10005 ;
const double eps = 1e-8 ;
#define ll __int64
int n , m ;
typedef pair<int,int> P;

int a[2][N];

int abs(int x){
    return x > 0 ? x : -x;
}

int solve()
{
    int pos[2] = {1, 1}, i, j, flag, role, tmp ;
	int ans = 0;
    for (i = 1; i <= n; i++)
    {
        flag = -1, role = a[1][i];
        for (j = i + 1; j <= n; j++)
		{
            if (a[1][i] != a[1][j]) {
                flag = j;
                break;
            }
		}
        tmp = 1 + abs(a[0][i] - pos[role]);
        pos[role] = a[0][i];
        ans += tmp;
        if (flag > 0){
            int wantT = abs(a[0][flag] - pos[1 - role]), dir;
            if (a[0][flag] > pos[1 - role]){
                dir = 1;
			}
            else{
                dir = -1;
			}
            pos[1 - role] += wantT < tmp ? dir * wantT : dir * tmp;
        }
    }
    return ans;
}

int main()
{
	int i, j, k, tmp, cas = 1, t ,ans, state ;
	int s, mn ;
	char c[10] ;

	for( scanf("%d" , &t ), cas = 1 ; cas <= t ; cas++ )
	{
        scanf("%d", &n ) ;
        for ( i = 1; i <= n; i++)
        {
			scanf("%s %d", &c, &a[0][i] ) ;
            a[1][i] = (*c == 'O') ? 0 : 1;
        }
		printf("Case #%d: %d\n", cas, solve() ) ;
	}

	return 0;
}