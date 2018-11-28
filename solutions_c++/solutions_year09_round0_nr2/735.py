#include <queue>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <vector>
#include <cstdio>
#include <complex>
#include <stack>
#include <cctype>
#include <cstdlib>
#include <iostream>

#define X real()
#define Y imag()
#define FR(i,n) for( long long i = 0; i < n; i ++ )
#define FOR(i,a,n) for(long long i = a; i < n; i ++)
#define FREACH(it,v) for( typeof(v.end()) it = v.begin(); it != v.end(); it ++ )
#define EPS 1e-12
#define EPS2 1e-3
#define MP make_pair

using namespace std;

typedef long long ll;
typedef long double ld;
typedef pair<ll,ll> pii;
    
int w,h;
int mp[100][100];
int col[100][100];
char key[26];
int dx[]={-1,0,0,1};
int dy[]={0,-1,1,0};
int curcol;

int ok(int x,int y)
{
    return (x>-1&&y>-1&&x<h&&y<w);
}

pii nxet(int x, int y)
{
    pair<int,int> res=MP(x,y);
    int mh=mp[x][y];
    FR(i,4)
    {
        if(ok(x+dx[i],y+dy[i])&&mp[x+dx[i]][y+dy[i]]<mh)
        {
            mh=mp[x+dx[i]][y+dy[i]];
            res=MP(x+dx[i],y+dy[i]);
        }
    }
    return res;
}


void expl(ll x,ll y)
{
    FR(i,4)
    {
        if(ok(x+dx[i],y+dy[i])&&col[x+dx[i]][y+dy[i]]==-1&&nxet(x+dx[i],y+dy[i])==MP(x,y))
        {
            
            col[x+dx[i]][y+dy[i]]=curcol;
            expl(x+dx[i],y+dy[i]);
        }
    }
}

int main()
{
    int t;
    scanf("%d",&t);
    FR(i,t)
    {
        
        curcol=-1;
        scanf("%d %d",&h,&w);
        FR(i,h) FR(j,w)
        {
            scanf("%d",&mp[i][j]);
            col[i][j]=-1;
        }
        FR(i,h) FR(j,w) 
        {
            if(col[i][j]==-1)
            {
                if(nxet(i,j)==MP(i,j))
                {
                   // cout << "basin " << i << " " << j << endl;
                    col[i][j]=++curcol;
                    expl(i,j);
                   /* FR(i2,h)
                    {
                        FR(j2,w) cout << col[i2][j2] << " ";
                        cout << endl;
                    }*/
                }
            }
        }
        
        int nxt='a';
        FR(i,26) key[i]='A';
        FR(i,h) FR(j,w)
        {
            if(key[col[i][j]]=='A') key[col[i][j]]=nxt++;
        }
        
        printf("Case #%d:\n",i+1);
        FR(i,h)
        {
            FR(j,w)
            {
                if(j!=0) putchar(' ');
                printf("%c",key[col[i][j]]);
            }
            putchar('\n');
        }
    }
}