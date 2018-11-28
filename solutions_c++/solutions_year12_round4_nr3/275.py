#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
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
#include <utility>

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
inline int min(int a, int b){return a < b? a: b;}
inline int max(int a, int b){return a > b? a: b;}

const int dis =  1000000;
const int size = 2222;

int height[size], num[size];
int n;


void getRes()
{
    int i,j;
    for(i = 1; i < n; i++)
    {
        for(j = num[i] - 1; j > i; j --)
        {
            height[j] -= (num[i] - j);
        }
    }
}

bool gao()
{
    int i,j;
    for(i = 1; i < n - 1; i++)
        for(j = i + 1; j < num[i]; j++)
        {
            if(num[j] > num[i])
                return true;
        }
    return false;
}
int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("small.out", "w", stdout);


    int cas,cn;
    cin >> cas;
    for(cn = 1; cn <= cas; cn ++)
    {
        cin >> n;
        for(int i = 1; i < n; i++)
        {
            cin >> num[i];
        }
        for(int i = 1; i <= n ;i++)
        {
            height[i] = i * dis;
        }
        printf("Case #%d:",cn);
        if( gao() == true){
            printf(" Impossible\n");
            continue;
        }
        getRes();

        for(int i = 1; i <= n ;i++)
        {
            printf(" %d",height[i]);
        }
        printf("\n");
    }
    return 0;
}
