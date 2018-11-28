#include <iostream>
#include <queue>
#include <set>
#include <map>
#include <vector>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))
#define foreach(it,c) for(typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

using namespace std;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<string> VS;
typedef pair<int,int> PII;

template<typename T> int size(const T &a) { return a.size(); } 

int N;
vector<int> vec;

bool solvable(const vector<int> &V, int pos)
{
    vector<int> tmp(V.begin()+pos, V.end());
    sort(tmp.begin(),tmp.end());
    for(int i=0;i<size(tmp);i++)
    {
        if(tmp[i] > i + pos) return false;
    }
    return true;
}

void process(void)
{
    cin >> N;
    vec.clear();
    for(int i=0;i<N;i++)
    {
        string str;
        cin >> str;

        for(int j=str.size()-1;j>=0;j--)
        {
            if(str[j] == '1')
            {
                vec.pb(j);
                break;
            }
        }
        if(vec.size() <= i) vec.pb(-1);
    }

    int cnt=0;

    for(int i=0;i<N;i++)
    {
        for(int j=i;j<N;j++)
        {
            if(vec[j] <= i)
            {
                vector<int> tt = vec;
                for(int k=j-1;k>=i;k--)
                {
                    swap(tt[k],tt[k+1]);
                    cnt++;
                }
                if(solvable(tt,i+1))
                {
                    vec = tt;
                    break;
                }
            }
        }
    }

    cout << cnt << endl;
}

int main(void)
{
    int N;
    cin >> N;
    for(int i=1;i<=N;i++)
    {
        printf("Case #%d: ",i);
        process();
        cerr << i << endl;
    }
}
