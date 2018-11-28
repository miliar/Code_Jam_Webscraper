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

int n,m;
VVI data;
int mask[1<<16];

bool comp(const VI &a, const VI &b)
{
    for(int i=0;i<a.size();i++)
        if(a[i] >= b[i]) return false;
    return true;
}

void btrace(int i)
{
    for(int j=0;j<i;j++) if(mask[j]==1) if((j & i) == j)
    {
        int k = (i ^ j);
        if(mask[k] == 0) continue;
        if(mask[i] == mask[j] + mask[k])
        {
            cout << i << " " << j << " " << k << endl;
            for(int kk=0;kk<n;kk++)
                if(j & (1<<kk)) cout << kk << " ";
            cout << endl;
            if(mask[k] != 1)
            {
                btrace(k);
                return;
            }
        }
    }
}

void process(void)
{
    cin >> n >> m;
    data.clear();
    memset(mask,0,sizeof(mask));
    for(int i=0;i<n;i++)
    {
        VI vv;
        vv.clear();
        for(int j=0;j<m;j++)
        {
            int tmp;
            cin >> tmp;
            vv.pb(tmp);
        }
        data.pb(vv);
    }

    sort(data.begin(),data.end());

    for(int i=0;i<(1<<n);i++)
    {
        vector<VI> tmp;
        tmp.clear();
        for(int j=0;j<n;j++) if(i & (1<<j))
            tmp.pb(data[j]);

        mask[i] = 1;
        for(int j=1;j<tmp.size();j++)
        {
            if(comp(tmp[j-1],tmp[j]) == false)
            {
                mask[i]=0;
                break;
            }
        }
    }

    for(int i=0;i<(1<<n);i++)
    {
        for(int j=0;j<i;j++) if(mask[j]) if((j & i) == j)
        {
            int k = (i ^ j);
            if(mask[k] == 0) continue;
            if(mask[i] == 0 || mask[i] > (mask[j] + mask[k])) 
            {
                mask[i] = mask[j]+mask[k];
            }
        }
    }

    cout << mask[(1<<n)-1] << endl;
//    btrace((1<<n)-1);
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
