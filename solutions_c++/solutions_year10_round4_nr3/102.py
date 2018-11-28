#include <iostream>
#include <algorithm>
#include <cstring>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <sstream>
#include <queue>
#include <set>
#include <map>
#include <vector>
#include <complex>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

int mark1[2][505][505];

void process(void)
{
    memset(mark1,0,sizeof(mark1));
    int n;
    scanf("%d",&n);
    for(int i=0;i<n;i++)
    {
        int x1,y1,x2,y2;
        scanf("%d %d %d %d",&x1,&y1,&x2,&y2);
        if(x1 > x2) swap(x1,x2);
        if(y1 > y2) swap(y1,y2);
        for(int j=x1;j<=x2;j++)
        {
            for(int k=y1;k<=y2;k++)
            {
                mark1[0][j][k]=1;
            }
        }
    }

    for(int i=0;;i++)
    {
        bool good = false;
        int cur = i%2;
        int nex = (i+1)%2;
        memset(mark1[nex],0,sizeof(mark1[nex]));
        for(int j=0;j<505;j++)
        {
            for(int k=0;k<505;k++)
            {
                if(mark1[cur][j][k])
                {
                    good=true;
                    if(j && mark1[cur][j-1][k])
                    {
                        mark1[nex][j][k] = 1;
                    }
                    if(k && mark1[cur][j][k-1])
                    {
                        mark1[nex][j][k] = 1;
                    }
                }
                else
                {
                    if(j && k && mark1[cur][j-1][k] && mark1[cur][j][k-1])
                    {
                        mark1[nex][j][k] = 1;
                    }
                }
            }
        }

        if(!good)
        {
            cout << i << endl;
            return;
        }
    }
}

int main(void)
{
    int T;
    scanf("%d",&T);
    for(int i=1;i<=T;i++)
    {
        printf("Case #%d: ",i);
        process();
    }
}

