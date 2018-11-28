#include<iostream>
#include<map>
#include<vector>
#include<fstream>
using namespace std;

#define PB push_back
#define SZ(a) ((int)((a).size()))
#define MP make_pair
#define FOR(i,a,b) for(int i=(a);i<(b);++i)
#define FORD(i,a,b) for(int i=(b)-1;i>=(a);--i)
#define FORE(it,x) for(__typeof((x).begin()) it=(x).begin(),it!=(x).end();++it)

int h,w,r;

int dp[105][105];
const int dx[]={1,2};
const int dy[]={2,1};


int go(int x,int y)
{
    if(x==h && y==w)return 1;
    int &ret=dp[x][y];
    if(ret==-1)
    {
        ret=0;
        for(int i=0;i<2;++i)
        {
            int nx=x+dx[i];
            int ny=y+dy[i];    
            if(nx<=0 || ny<=0 || nx>h || ny>w)continue;
            ret=(ret+go(nx,ny))%10007;
        }
    }
    return ret;    
}

int main()
{
    ifstream fin;
    fin.open("C:\\data\\D-small-attempt0.in");
    ofstream fout;
    fout.open("C:\\data\\ds.txt");
    int t;
    fin>>t;
    int x,y;
    for(int cas=1;cas<=t;++cas)
    {
        fin>>h>>w>>r;
        memset(dp,-1,sizeof(dp));
        for(int i=0;i<r;++i)
        {
            fin>>x>>y;
            dp[x][y]=0;
        }
        int ret=go(1,1);
        fout<<"Case #"<<cas<<": "<<ret<<endl;    
    }
    fin.close();
    fout.close();
    return 0;    
}
