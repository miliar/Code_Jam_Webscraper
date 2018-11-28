/* 
 * File:   GCJ_numgame.cpp
 * Author: nikhil
 *
 * Created on 22 May, 2010, 6:42 AM
 */

//Data Structure includes
#include<vector>
#include<stack>
#include<set>
#include<map>
#include<queue>
#include<deque>
#include <bitset>
#include<bitset>

//Other Includes
#include<sstream>
#include<fstream>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cmath>
#include<cstdio>


using namespace std;


#define FOR(i,a,b)                              for(int i=a;i<b;i++)
#define REP(i,n)                                FOR(i,0,n)
#define pb                                      push_back
#define s(n)					scanf("%d",&n)
#define sl(n) 					scanf("%lld",&n)
#define sf(n) 					scanf("%lf",&n)
#define fill(a,v) 				memset(a, v, sizeof a)
#define sz                                      size()
#define INF                                     (int)1e9

typedef vector<int> VI;
typedef vector<vector<int> > VVI;
typedef long long LL;
typedef vector<string> VS;
typedef pair<int, int > PII;

/* A simple Fast Integer reader */
int nextInt() {
    bool neg = false;
    int ans = 0;
    char c = getchar();
    while (isspace(c)) c = getchar();

    if (c == '-') neg = true;
    else ans = (int) (c - '0');

    c = getchar();
    while (isdigit(c)) {
        ans = (ans << 3)+(ans << 1)+ (int) (c - '0');
        c = getchar();
    }
    if (neg) return -ans;
    else return ans;
}

char nextChar() {
    char c = getchar();
    while (isspace(c)) c = getchar();
    return c;
}

/* Main code begins from here */



bool isWinning(int A,int B)
{
    int q=A/B;
    int r=A%B;
    if(r==0 && q==1) return false;
    if(r==0 && q>1) return true;
    if(r>0 && q>1) return true;
    return !isWinning(B,r);
}



int main(int argc, char** argv)
{
    int T; s(T);
    int x1,y1,x2,y2;
    for(int t=1;t<=T;t++)
    {
        int count=0;
        s(x1); s(x2); s(y1); s(y2);
        for(int i=x1;i<=x2;i++)
        {
            for(int j=y1;j<=y2;j++)
            {
                if(isWinning(max(i,j),min(i,j)))
                    count++;
            }
        }
        printf("Case #%d: %d\n",t,count);

    }
    return (EXIT_SUCCESS);
}

