/* 
 * File:   Games.cpp
 * Author: nikhil
 *
 * Created on 5 June, 2010, 8:57 PM
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




int tree[5000];
int tickets[1200];
int prices[5000];
int p;

void initSegment(int i)
{
    if(i>=(1<<p) ) tree[i]=tickets[i-(1<<p)];
    else
    {
        initSegment(2*i); initSegment(2*i+1);
        tree[i]=max(tree[2*i],tree[2*i+1]);
    }
}
void init()
{
    initSegment(1);
}

LL solveSegment(int i,int k)
{
    if(tree[i]-k<=0) return 0;
    if(i>=(1<<p) ) return INF;
    
    LL ans1= solveSegment(2*i,k+1)+solveSegment(2*i+1,k+1)+prices[i];
    LL ans2= solveSegment(2*i,k)+solveSegment(2*i+1,k);
    return min(ans1,ans2);
}
int main(int argc, char** argv)
{
    int T=nextInt();
    for(int z=1;z<=T;z++)
    {
        p=nextInt();
        REP(i,(1<<p))
        {
            s(tickets[i]);
            tickets[i]=p-tickets[i];
        }
        int x;;
        for(int i=p-1;i>=0;i--)
        {
            int k=(1<<i);
            for(int j=0;j<(1<<i);j++)
                s(prices[k++]);
        }
        initSegment(1);

    printf("Case #%d: %lld\n",z,solveSegment(1,0));
    }
    return (EXIT_SUCCESS);
}

