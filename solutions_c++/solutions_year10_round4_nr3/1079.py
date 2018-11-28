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

#define SMALL
//#define LARGE

int mm[1000][1000];

int main()
{
#ifdef SMALL
    //ifstream fin("D-small-practice.in");ofstream fout("D-small-practice.out");
    //ifstream fin("D-small-attempt0.in");ofstream fout("D-small-attempt0.out");
    //freopen("C-small-attempt0.in","r",stdin);//freopen("C-small-attempt0.out","w",stdout);
    freopen("C-small-attempt1.in","r",stdin);freopen("C-small-attempt1.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("D-large-practice.in");ofstream fout("D-large-practice.out");
    //ifstream fin("D-large.in");ofstream fout("D-large.out");
    freopen("C-large","r",stdin);freopen("C-large.out","w",stdout);
#endif
    int N;
    cin>>N;
    REP(i,1000)
    {
        REP(j,1000)
        {
            mm[i][j]=0;
        }
    }
    REP(z,N)
    {

        cout<<"Case #"<<z+1<<": ";
        //////////////////////////////////////
        int r;
        cin>>r;
        int x1,y1,x2,y2;
        int m1=0,m2=0;
        while(r--)
        {

            cin>>x1>>y1>>x2>>y2;
            if (x2>m1)m1=x2;
            if (y2>m2)m2=y2;
            for(int i=x1;i<=x2;i++)
            {
                for(int j=y1;j<=y2;j++)
                {
                    mm[i][j]=1;
                }
            }
        }
        int num=0;
        REP(i,m1)
        {
            REP(j,m2)
            {
                if(mm[i+1][j+1]==1)++num;
            }
        }
        int res=0;
        if (m1==0&&m2==0)
        {
            cout<<res<<endl;
            continue;
        }

        while(num)
        {
            res++;

            for(int i=m1;i>0;i--)
            {
                for (int j=m2;j>0;j--)
                {

                    if(mm[i-1][j]==1&&mm[i][j-1]==1&&mm[i][j]==0)
                    {

                        num++;
                        mm[i][j]=1;
                    }
                    if(mm[i-1][j]==0&&mm[i][j-1]==0&&mm[i][j]==1)
                    {
                        num--;
                        mm[i][j]=0;
                    }
                }
            }
    /*
                    REP(i,m1)
            {
                REP(j,m2)
                {
                    cout<<mm[i+1][j+1]<<" ";
                }
                cout<<endl;
            }
            cout<<endl;*/
        }


        cout<<res;
        //////////////////////////////////////
        cout<<endl;
    }
    return 0;
}
