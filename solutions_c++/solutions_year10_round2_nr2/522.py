#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>

#include <sstream>
#include <fstream>
#include <iostream>
#include <iomanip>

#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cstring>
#include <cmath>
#include <ctime>

using namespace std;

//BEGINTEMPLATE_BY_SCORPIOLIU
const double PI  = acos(-1.0);
const double EPS = 1e-11;
const double INF  = 1E200;

typedef long long int64;
typedef unsigned long long uint64;

typedef pair<int,int> ipair;
#define MP(X,Y) make_pair(X,Y)
#define SIZE(X) ((int)(X.size()))
#define LENGTH(X) ((int)(X.length()))

#define REP(i,a) for(int i=0;i<int(a);++i)
#define REP2(i,n,m) for(int i=n;i<(int)(m);++i)
#define FORE(it,a) for (typeof((a).begin()) it=(a).begin();it!=(a).end();++it)
#define ALL(a) (a).begin(),(a).end()
//ENDEMPLATE_BY_SCORPIOLIU

//Temp function list begine
inline int comp(const double &a, const double &b) {
	if (fabs(a - b) < EPS)
		return 0;
	return a > b ? 1 : -1;
}
char alpha[27] = {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' '};
int  T9[27]    = {2,22,222,3,33,333,4,44,444,5,55,555,6,66,666,7,77,777,7777,8,88,888,9,99,999,9999,0};
//Temp function list end

//#define SMALL
#define LARGE

int main()
{
#ifdef SMALL
    //ifstream fin("B-small-practice.in");ofstream fout("B-small-practice.out");
    //ifstream fin("B-small-attempt0.in");ofstream fout("B-small-attempt0.out");
    freopen("B-small-attempt0.in","r",stdin);freopen("B-small-attempt0.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("B-large-practice.in");ofstream fout("B-large-practice.out");
    //ifstream fin("B-large.in");ofstream fout("B-large.out");
    freopen("B-large.in","r",stdin);freopen("B-large.out","w",stdout);
#endif
    int N;
    cin>>N;
    REP(z,N)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        int n,k,b,t;
        cin>>n>>k>>b>>t;
        vector<int>loc;
        vector<int>v;
        int temp;
        int res = 0;
        for(int i=0;i<n;i++)
        {
            cin>>temp;
            loc.push_back(temp);
        }
        for(int i=0;i<n;i++)
        {
            cin>>temp;
            v.push_back(temp);
        }
        temp = 0;
        int temp2=0;
        for(int i=n-1;i>=0;i--)
        {
            if (loc[i]+t*v[i]>=b)
            {
                temp++;
                res +=temp2;
            }
            else{temp2++;}
            if (temp>=k)break;
        }
        if(temp<k)cout<<"IMPOSSIBLE";
        else cout<<res;
        //////////////////////////////////////
        cout<<endl;
    }
    return 0;
}
