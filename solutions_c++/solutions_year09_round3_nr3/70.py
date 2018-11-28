#include <iostream>
#include <set>
#include <map>
#include <vector>

#define mp make_pair
#define pb push_back
#define sqr(x) ((x)*(x))

using namespace std;

typedef vector<int> VI;
typedef pair<int,int> PII;

int n;
VI V;
map<PII,int> memo;

int calc(int s,int e)
{
    if(s>e) return 0;
    if(memo.count(mp(s,e))) return memo[mp(s,e)];
    int left = (s==0)?0:V[s-1];
    int right = (e==(int)V.size()-1)?n+1:V[e+1];

    int ret = right - left - 2;
    int min=-1;
    for(int i=s;i<=e;i++)
    {
        int tmp = calc(s,i-1) + calc(i+1,e);
        if(min < 0 || tmp < min) min = tmp;
    }
    ret += min;
    return memo[mp(s,e)] = ret;
}

void process(void)
{
    int m;
    cin >> n >> m;
    V.clear();
    memo.clear();
    for(int i=0;i<m;i++)
    {
        int tmp;
        cin >> tmp;
        V.push_back(tmp);
    }
    sort(V.begin(),V.end());
    cout << calc(0,V.size()-1) << endl;
}

int main(void)
{
    int N;
    cin >> N;
    for(int i=1;i<=N;i++)
    {
        printf("Case #%d: ",i);
        process();
    }
}
