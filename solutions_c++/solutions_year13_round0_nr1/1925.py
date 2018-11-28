/* ***************************
Author: Abhay Mangal (abhay26)
*************************** */
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <cstring>
#include <cassert>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
using namespace std;
 #define tr(container, it) \
	for(typeof(container.begin()) it = container.begin(); it != container.end(); it++)
#define maX(a,b) (a) > (b) ? (a) : (b)
#define pii pair< int, int >
#define pip pair< int, pii >
#define FOR(i,n) for(int i=0; i<(int)n ;i++)
#define pb push_back
//int dx[]= {-1,0,1,0};
//int dy[]= {0,1,0,-1};
char ar[4][4];
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
	int t;
	scanf("%d",&t);
	int cas=0;
	while(t--)
	{
        for(int i=0;i<4;i++)
            scanf("%s",ar[i]);
        int O=0,X=0;
        cas++;
        for(int i=0;i<4;i++)
        {
            if((ar[i][0]=='X' || ar[i][0]=='T') && (ar[i][1]=='X' || ar[i][1]=='T') && (ar[i][2]=='X' || ar[i][2]=='T') && (ar[i][3]=='X' || ar[i][3]=='T'))
                X = 1;
            if((ar[i][0]=='O' || ar[i][0]=='T') && (ar[i][1]=='O' || ar[i][1]=='T') && (ar[i][2]=='O' || ar[i][2]=='T') && (ar[i][3]=='O' || ar[i][3]=='T'))
                O = 1;
        }
        for(int j=0;j<4;j++)
        {
            if((ar[0][j]=='X' || ar[0][j]=='T') && (ar[1][j]=='X' || ar[1][j]=='T') && (ar[2][j]=='X' || ar[2][j]=='T') && (ar[3][j]=='X' || ar[3][j]=='T'))
                X = 1;
            if((ar[0][j]=='O' || ar[0][j]=='T') && (ar[1][j]=='O' || ar[1][j]=='T') && (ar[2][j]=='O' || ar[2][j]=='T') && (ar[3][j]=='O' || ar[3][j]=='T'))
                O = 1;
        }
        if((ar[0][0]=='X' || ar[0][0]=='T') && (ar[1][1]=='X' || ar[1][1]=='T') && (ar[2][2]=='X' || ar[2][2]=='T') && (ar[3][3]=='X' || ar[3][3]=='T'))
            X=1;
        if((ar[0][3]=='X' || ar[0][3]=='T') && (ar[1][2]=='X' || ar[1][2]=='T') && (ar[2][1]=='X' || ar[2][1]=='T') && (ar[3][0]=='X' || ar[3][0]=='T'))
            X=1;
        if((ar[0][0]=='O' || ar[0][0]=='T') && (ar[1][1]=='O' || ar[1][1]=='T') && (ar[2][2]=='O' || ar[2][2]=='T') && (ar[3][3]=='O' || ar[3][3]=='T'))
            O=1;
        if((ar[0][3]=='O' || ar[0][3]=='T') && (ar[1][2]=='O' || ar[1][2]=='T') && (ar[2][1]=='O' || ar[2][1]=='T') && (ar[3][0]=='O' || ar[3][0]=='T'))
            O=1;
        int over = 1;
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            {
                if(ar[i][j]=='.')
                    over = 0;
            }
        }
        printf("Case #%d: ",cas);
        if(X)
        {
            printf("X won\n");
        }
        else if(O)
        {
            printf("O won\n");
        }
        else if(over)
        {
            printf("Draw\n");
        }
        else
            printf("Game has not completed\n");
	}
return 0;
}
