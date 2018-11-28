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

int n,m;
char data[105][105];
int flow[105][105];
LL cnt = 0;

int dx[][2] = { { -1, 1}, {0,0}, {-1,1}, {-1,1}};
int dy[][2] = { { 0,0}, {-1,1}, {-1,1}, {1,-1}};

void go(int a,int b)
{
    if(a == n)
    {
        cnt++;
        return;
    }
    if(b == m)
        go(a+1,0);
    
    int cc = data[a][b];
    for(int i=0;i<2;i++)
    {
        int nx = (a + dx[cc][i] + n) % n;
        int ny = (b + dy[cc][i] + m) % m;
        if(flow[nx][ny] == 0)
        {
            flow[nx][ny]++;
            go(a,b+1);
            flow[nx][ny]--;
        }
    }
}

void process(void)
{
    memset(flow, 0, sizeof(flow));
    scanf("%d %d",&n,&m);
    cnt = 0;
    for(int i=0;i<n;i++)
    {
        scanf("%s", data[i]);
        for(int j=0;j<m;j++)
        {
            switch(data[i][j])
            {
                case '|':
                    data[i][j] = 0;
                    break;
                case '-':
                    data[i][j] = 1;
                    break;
                case '\\':
                    data[i][j] = 2;
                    break;
                case '/':
                    data[i][j] = 3;
                    break;
            }
        }
    }

    go(0,0);

    cout << (cnt % 1000003) << endl;
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

