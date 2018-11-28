#include <iostream>
#include <cmath>
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

int n;
VI x,y,r;

double calc(int a,int b)
{
    double dist = sqrt(sqr(x[a]-x[b]) + sqr(y[a]-y[b]));
    return (dist + r[a] + r[b]) / 2;
}

void process(void)
{
    cin >> n;
    x=y=r=VI(n,0);
    for(int i=0;i<n;i++)
    {
        cin >> x[i] >> y[i] >> r[i];
    }

    if(n==1)
    {
        cout << r[0] << endl;
        return;
    }
    if(n==2)
    {
        cout << max(r[0],r[1]) << endl;
        return;
    }

    double tmp = max(calc(0,1),(double)r[2]);
    double ret = tmp;
    tmp = max(calc(0,2),(double)r[1]);
    if(tmp < ret) ret = tmp;
    tmp = max(calc(2,1),(double)r[0]);
    if(tmp < ret) ret = tmp;
    printf("%.12lf\n",ret);
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
