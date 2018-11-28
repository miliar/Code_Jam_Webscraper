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
string words[10005];

int check(int a, char lang[])
{
    bool no[10005];
    memset(no, 0, sizeof(no));
    int len = words[a].size();

    int ret = 0;

    for(int i=0;i<n;i++) if(words[i].size() != len) no[i] = true;

    for(int i=0;i<26;i++)
    {
        char chr = lang[i];
        bool go = false;
        for(int j=0;j<n;j++) if(no[j] == false)
        {
            for(int k=0;k<len;k++)
            {
                if(words[j][k] == chr)
                {
                    go = true;
                    break;
                }
            }
            if(go) break;
        }
        if(go == false) continue;

        bool found = false;
        for(int j=0;j<len;j++)
        {
            if(words[a][j] == chr)
            {
                found = true;
                break;
            }
        }
        if(!found)
        {
            ret++;
        }

        for(int j=0;j<n;j++) if(no[j] == false)
        {
            for(int k=0;k<len;k++)
                if( (words[a][k] == chr) != (words[j][k] == chr) )
                {
                    no[j] = true;
                    break;
                }
        }
    }

    return ret;
}

bool process(void)
{
    char buffer[1024];
    scanf("%d %d", &n, &m);

    for(int i=0;i<n;i++)
    {
        scanf(" %s", buffer);
        words[i] = buffer;
    }

    for(int i=0;i<m;i++)
    {
        scanf(" %s", buffer);
        int maxscore = -1;
        int idx = -1;
        for(int j=0;j<n;j++)
        {
            int tmp = check(j, buffer);
            if(tmp > maxscore)
            {
                maxscore = tmp;
                idx = j;
            }
        }

        cout << words[idx] << " ";
    }
    cout << endl;
	return true;
}

int main(void)
{
    int T;
    cin >> T;
    for(int i=0;i<T;i++)
    {
        cout << "Case #" << i+1 << ": ";
        process();
    }
	return 0;
}

