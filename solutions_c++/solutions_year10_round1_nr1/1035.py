#include <iostream>
#include <string>
#include <map>
#include <queue>
#include <stack>
#include <algorithm>
#include <list>
#include <set>
#include <cmath>
#include <cstring>
#include <stdio.h>
#include <string.h>
#include <sstream>
#include <stdlib.h>
#include <vector>

using namespace std;

#define INF 1<<28
#define SIZE 10000

#define REP(i,n) for (int i=0; i<n; ++i)
#define FOREACH(it,x) for(__typeof((x).begin()) it=(x.begin()); it!=(x).end(); ++it)
#define FOR(i,p,k) for (int i=p; i<=k; ++i)

#define MP(a,b) make_pair(a,b)

#define CLEAR(x,with) memset(x,with,sizeof(x))
#define SZ(x) (int)x.size()
#define PB push_back

#define gcd(a,b)    __gcd(a,b)

typedef long long ll;
typedef pair<int,int> pii;
typedef pair<double,double> pdd;
typedef vector<int> vi;
typedef vector<string> vs;
typedef map<string,int> msi;

char board[100][100],temp[100][100];
int blue,red,K;

//Eight Direction
int dx[]={1,1,0,-1,-1,-1,0,1};
int dy[]={0,1,1,1,0,-1,-1,-1};

void gravity(int n)
{
    int i,j,k,check;

    for(i=0;i<n;i++)
    {

        for(j=n-1;j>=0;j--)
            if(board[j][i]=='.')
                break;
        k=j;
        while(true)
        {
            check=0;
            for(;j>=0;j--)
                if(board[j][i]!='.')
                {
                    board[k--][i]=board[j--][i];
                    board[j+1][i]='.';
                    check=1;
                    break;
                }
            if(check==0)
                break;
        }
    }
}

void rotate(int n)
{
    int i,j,k,p,q;

    for(i=n-1,q=0;i>=0;i--,q++)
    {
        for(j=0,p=0;j<n;j++,p++)
        {
            temp[p][q]=board[i][j];
        }
    }
    for(i=0;i<n;i++)
    {
        temp[i][n]='\0';
        strcpy(board[i],temp[i]);
    }
}

int Search(int N)
{
    int i,j,k,l,m,n,check;

    for(i=0;i<N;i++)
    {
        for(j=0;j<N;j++)
        {
            if(board[i][j]!='.')
            {
                for(k=0;k<8;k++)
                {
                    check=1;
                    for(l=1;l<K;l++)
                    {
                        m=i+dx[k]*l;
                        n=j+dy[k]*l;
                        if(m>=0 && m<N && n>=0 && n<N)
                        {
                            if(board[i][j]!=board[m][n])
                                check=0;
                        }
                        else check=0;
                    }
                    if(check)
                    {
                        if(board[i][j]=='B')
                            blue=1;
                        if(board[i][j]=='R')
                            red=1;
                    }
                }
            }
        }
    }
}

int main()
{
    freopen("A.in","r",stdin);
    freopen("A.out","w",stdout);

    int i,j,test,m,n,Case=1;

    scanf("%d",&test);
    while(test--)
    {
        scanf("%d %d",&n,&K);

        for(i=0;i<n;i++)
            scanf("%s",board[i]);
        gravity(n);
        rotate(n);
        gravity(n);
        blue=red=0;
        Search(n);
        if(blue==0 && red==0)
            printf("Case #%d: Neither\n",Case++);
        if(blue==1 && red==1)
            printf("Case #%d: Both\n",Case++);
        if(blue==0 && red==1)
            printf("Case #%d: Red\n",Case++);
        if(blue==1 && red==0)
            printf("Case #%d: Blue\n",Case++);
        //for(i=0;i<n;i++)
            //printf("%s\n",board[i]);
    }

    return 0;
}
/*
5
3 2
.AB
..B
.B.

5
7 3
.......
R......
BB.....
BRRR...
RBB....
.......
.......
*/
