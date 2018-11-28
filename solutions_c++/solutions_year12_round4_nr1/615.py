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

//BEGINTEMPLATE_BY_ACRUSH_TOPCODER
#define SIZE(X) ((int)(X.size()))//NOTES:SIZE(
#define LENGTH(X) ((int)(X.length()))//NOTES:LENGTH(
#define MP(X,Y) make_pair(X,Y)//NOTES:MP(
typedef long long int64;//NOTES:int64
typedef unsigned long long uint64;//NOTES:uint64
#define two(X) (1<<(X))//NOTES:two(
#define twoL(X) (((int64)(1))<<(X))//NOTES:twoL(
#define contain(S,X) (((S)&two(X))!=0)//NOTES:contain(
#define containL(S,X) (((S)&twoL(X))!=0)//NOTES:containL(

typedef long long ll;
const int MAXN = 12345;
struct Node
{
    int x, d;
}node[MAXN];
int dp[MAXN];
int n;

bool isSucn(int dis)
{
    for(int i = 0; i < n; i++)
        if(dp[i] >= dis)
            return true;
    return false;
}
void getRes(int id)
{
    for(int i = id + 1; i < n; i ++)
    {
        if(node[i].x > dp[id])
            return ;
        int dis = min(node[i].d, node[i].x - node[id].x)
            + node[i].x;
        dp[i] = max(dp[i], dis);
    }
}
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("large.out", "w", stdout);
    int cas,dis,cn;
    cin >> cas;
    for(cn = 1; cn <= cas; cn ++)
    {
        cin >> n;
        for(int i = 0; i < n; i++)
        {
            cin >> node[i].x >> node[i].d;
        }
        cin >> dis;
        memset(dp, -1, sizeof(dp));
        dp[0] = node[0].x << 1;
        for(int i = 0; i < n ;i++)
            getRes(i);
        cout << "Case #" << cn << ": " <<
            (isSucn(dis)? "YES": "NO") << endl;
    }
    return 0;
}
