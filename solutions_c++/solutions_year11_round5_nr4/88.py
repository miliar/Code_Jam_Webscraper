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

LL mask, cur, candi;
int len;

bool go(int a)
{
    if(a == len)
    {
        LL tmp = (LL)sqrt((double)cur);
        for(LL tt = tmp - 5; tt <= tmp +5; tt++)
        {
            if(tt * tt == cur) return true;
        }
        return false;
    }
    if(mask & (1LL<<a)) 
    {
        if(go(a+1)) return true;
        return false;
    }
    cur |= (1LL << a);
    if(go(a+1)) return true;
    cur ^= (1LL << a);
    if(go(a+1)) return true;
    return false;
}

void process(void)
{
    mask = cur = candi = 0;
    char instr[1024];
    scanf(" %s",instr);
    len = strlen(instr);
    for(int i=0;i<len;i++)
    {
        mask <<= 1;
        cur <<= 1;
        candi <<= 1;

        mask |= 1;
        if(instr[i] == '?')
        {
            mask ^= 1;
        } 
        else if(instr[i] == '1')
        {
            cur |= 1;
        }
    }

    go(0);
    for(int i=len-1;i>=0;i--)
    {
        cout << ((cur & (1LL<<i)) >> i);
    }
    cout << endl;
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

