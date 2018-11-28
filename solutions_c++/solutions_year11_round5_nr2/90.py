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

map<int,int> M;

bool check(int a)
{
    vector<int> V(a);
    int prev = -2;
    foreach(it, M)
    {
        if(it->first != prev + 1)
        {
            // new start
            for(int i=0;i<a-1;i++)
                if(V[i]) return false;
            V[a-1] = 0;
            V[0] = it->second;
        }
        else
        {
            int tmp = it->second;
            int tmp2 = V[a-1];
            V[a-1] = 0;
            for(int i=a-2;i>=0;i--)
            {
                if(tmp < V[i]) return false;
                V[i+1] += V[i];
                tmp -= V[i];
                V[i] = 0;
            }
            if(tmp > tmp2)
            {
                V[a-1] += tmp2;
                V[0] = tmp - tmp2;
            }
            else
            {
                V[a-1] += tmp;
            }
        }
        prev = it->first;
    }
    for(int i=0;i<a-1;i++)
        if(V[i]) return false;
    return true;
}

void process(void)
{
    M.clear();

    int N;
    scanf("%d",&N);
    for(int i=0;i<N;i++)
    {
        int a;
        scanf("%d",&a);
        M[a]++;
    }

    if(N == 0)
    {
        cout << 0 << endl;
        return;
    }

    for(int i=N;i>1;i--)
    {
        if(check(i))
        {
            cout << i << endl;
            return;
        }
    }
    cout << 1 << endl;
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

