#include <algorithm>
#include <bitset>
#include <deque>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <functional>
#include <iomanip>
#include <iostream>
#include <list>
#include <map>
#include <numeric>
#include <queue>
#include <set>
#include <sstream>
#include <stack>
#include <utility>
#include <vector>

using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> VI;
typedef pair<int,int> PI;
typedef vector<pair<int,int> > VPI;
typedef vector<string> VS;


#define ST          first
#define ND          second
#define ALL(x)      (x).begin(), (x).end()
#define FOR(i,s,n)  for(i=s;i<(n);++i)
#define LOOP(i,x)   for(i=0;i<SZ(x);++i)
#define IT(i,x)     for(typeof(x.begin()) i=x.begin();i!=x.end();++i)
#define PB          push_back
#define MP          make_pair
#define SZ(x)       (int)(x.size())
#define DISP(x)     cout << #x << ": " << x << endl;

int N,K;
char board[100][100],temp[100][100];

bool isvalid(int i,int j)
{
    return i>=0 && i<N && j>=0 && j<N;
}

void disp(int b)
{
    int i,j;
    if(b)
    {
        FOR(i,0,N)
            printf("%s\n",board[i]);
    } else
    {
        FOR(i,0,N)
            printf("%s\n",temp[i]);

    }
    printf("\n");
}

void rotate()
{
    int i,j,ni,nj;
    //disp(1);

    for(i=0;i<N;++i)
    {
        ni=i;
        for(nj=j=N-1;j>=0;--j)
        {
            if(board[i][j]!='.')
            {
                board[ni][nj]=board[i][j];
                --nj;
            }
        }
        for(j=0;j<=nj;++j) board[i][j]='.';

    }
    //disp(1);
    for(i=0;i<N;++i)
    {
        for(j=0;j<N;++j)
        {
            temp[j][N-i-1]=board[i][j];
        }
        temp[i][N]='\0';
    }
    //disp(0);
}

string solve()
{
    int R=0,B=0,cnt=0;
    int i,j,ni,nj,k;
    int di[4]={0,1,1,1},dj[4]={1,0,1,-1};
    char first;
    rotate();

    FOR(i,0,N)
    {
        FOR(j,0,N)
        {
            first=temp[i][j];
            if(first=='.') continue;
            FOR(k,0,4)
            {
                cnt=0;ni=i;nj=j;
                while(cnt<K)
                {
                    if(!isvalid(ni,nj)) break;
                    if(temp[ni][nj]==first)
                    {
                        ++cnt;
                        ni+=di[k];nj+=dj[k];
                    } else
                    {
                        break;
                    }
                }
                if(cnt==K)
                {
                    if(first=='R')
                        R=1;
                    else if(first=='B')
                        B=1;
                }
            }
        }
    }

    if(R+B==0)
        return "Neither";
    else if(R+B==2)
        return "Both";
    else if(R==1)
        return "Red";
    else
        return "Blue";
}

int main()
{
    int i,j,t,kase,n,k;

    //FILE * fin=fopen("sample.txt","r");
    //FILE * fin=fopen("A-small-attempt0.in","r");
    FILE * fin=fopen("A-large.in","r");
    FILE * fout=fopen("out.txt","w");

    fscanf(fin,"%d",&t);
    DISP(t);
    for(kase=1;kase<=t;++kase)
    {
        fscanf(fin,"%d %d",&N,&K);
        fgets(board[0],100,fin);
        FOR(i,0,N)
        {
            fgets(board[i],100,fin);
        }
        fprintf(fout,"Case #%d: %s\n",kase,solve().c_str());
    }

	return 0;
}
