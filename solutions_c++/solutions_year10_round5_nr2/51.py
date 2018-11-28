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

vector<int> arr;

void process(void)
{
    long long L;
    LL lcm = 1;
    int n;
    cin >> L >> n;
    arr.resize(n);
    for(int i=0;i<n;i++)
    {        
        cin >> arr[i];
    }

    sort(arr.begin(), arr.end());
    LL maxx = arr.back();
    arr.pop_back();

    vector<int> cnts(maxx, -1);
    cnts[0] = 0;
    queue<int> Q;
    Q.push(0);
    while(!Q.empty())
    {
        int pos = Q.front();
        Q.pop();

        for(int i=0;i<size(arr);i++)
        {
            int nex = (pos + arr[i]);
            int nc = cnts[pos] + 1;
            if(nex >= maxx)
            {
                nex -= maxx;
                nc --;
            }

            if(cnts[nex] < 0 || cnts[nex] > nc)
            {
                cnts[nex] = nc;
                Q.push(nex);
            }
        }
    }

    if(cnts[L%maxx] == -1)
    {
        cout << "IMPOSSIBLE" << endl;
    }
    else
    {
        cout << L/maxx + cnts[L%maxx] << endl;
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
	return 0;
}

