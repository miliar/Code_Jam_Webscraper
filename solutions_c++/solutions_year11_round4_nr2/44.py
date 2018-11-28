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
#define BIT(x) (1LL<<(x))

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;
typedef long long LL;
typedef complex<double> Point;

template<typename T> inline int size(const T &a) { return a.size(); }
template<typename T> inline bool operator<(const int &a,const vector<T> &b) { return a<b.size(); }

int data[505][505];
int rowsum[505][505];
int colsum[505][505];

bool chk1(int rowsum[][505], int a,int b,int sz)
{
    LL rd = 0;
    rd += (sz-1) * (rowsum[a][b+sz-1] - rowsum[a][b+1]);
    for(int i=a+1;i<a+sz-1;i++)
    {
        rd += (sz-1-2*(i-a)) * (rowsum[i][b+sz] - rowsum[i][b]);
    }
    rd += (1-sz) * (rowsum[a+sz-1][b+sz-1] - rowsum[a+sz-1][b+1]);

    return rd == 0;
}

bool check(int a,int b,int sz)
{
    LL rd=0,cd=0;

    if(chk1(rowsum, a, b, sz) == false) return false;
    return chk1(colsum, b, a, sz);
}

void process(void)
{
    int r,c,d;
    scanf("%d %d %d",&r,&c,&d);
    for(int i=0;i<r;i++)
    {
        for(int j=0;j<c;j++)
        {
            char tmp;
            scanf(" %c", &tmp);
            data[i][j] = (tmp - '0');
        }
    }

    for(int i=0;i<r;i++)
    {
        rowsum[i][0] = 0;
        for(int j=1;j<=c;j++)
        {
            rowsum[i][j] = rowsum[i][j-1] + data[i][j-1];
        }
    }

    for(int i=0;i<c;i++)
    {
        colsum[i][0] = 0;
        for(int j=1;j<=r;j++)
        {
            colsum[i][j] = colsum[i][j-1] + data[j-1][i];
        }
    }

    for(int i=min(r,c);i>=3;i--)
    {
        for(int j=0;j+i<=r;j++)
        {
            for(int k=0;k+i<=c;k++)
            {
                if(check(j,k,i))
                {
                    cout << i << endl;
                    return;
                }
            }
        }
    }

    cout << "IMPOSSIBLE" << endl;
    return;
}

int main(void)
{
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        cout << "Case #" << i+1 << ": ";
        process();
        cerr << i << endl;
    }
	return 0;
}

