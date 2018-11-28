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

//#define SMALL
#define LARGE

int main()
{
#ifdef SMALL
    //ifstream fin("A-small-practice.in");ofstream fout("A-small-practice.out");
    //ifstream fin("A-small-attempt0.in");ofstream fout("A-small-attempt0.out");
    freopen("A-small-attempt0.in","r",stdin);freopen("A-small-attempt0.out","w",stdout);
#endif
#ifdef LARGE
    //ifstream fin("A-large-practice.in");ofstream fout("A-large-practice.out");
    //ifstream fin("A-large.in");ofstream fout("A-large.out");
    freopen("A-large.in","r",stdin);freopen("A-large.out","w",stdout);
#endif
    int Z;
    cin>>Z;
    REP(z,Z)
    {

        cout<<"Case #"<<z+1<<": "<<endl;
        //////////////////////////////////////
        int N;
        cin>>N;
        vector<string>v;
        string str;
        while(N--)
        {
            cin>>str;
            v.push_back(str);
        }

        vector<double>wp;
        vector<double>owp;
        vector<double>oowp;

        for(int i = 0; i != v.size(); i++)
        {
            double t = 0.0;
            double w = 0.0;
            for (int j = 0; j < v[i].size(); j++)
            {
                if (v[i][j]=='1' || v[i][j] == '0')t+=1.0;
                if (v[i][j]=='1')w+=1.0;
            }
            wp.push_back(w/t);
        }

        for(int i = 0; i != v.size(); i++)
        {
            double t = 0.0;
            double w = 0.0;
            for (int j = 0; j < v[i].size(); j++)
            {
                if (v[i][j]=='1' || v[i][j] == '0')
                {
                    t += 1.0;
                    double st = 0.0;
                    double sw = 0.0;
                    for (int k = 0; k < v[j].size(); k++)
                    {
                        if ((v[j][k] == '0' || v[j][k] == '1') && k!=i)
                        {
                            st += 1.0;
                        }
                        if (v[j][k] == '1' && k!=i)
                        {
                            sw += 1.0;
                        }
                    }
                    if (abs(st -0.0)<EPS) w = 0;
                    else w += sw/st;
                }
            }
            owp.push_back(w/t);
        }

        for(int i = 0; i != v.size(); i++)
        {
            double t = 0.0;
            double w = 0.0;
            for (int j = 0; j < v[i].size(); j++)
            {
                if (v[i][j]=='1' || v[i][j] == '0')
                {
                    t += 1.0;
                    w += owp[j];
                }
            }
            oowp.push_back(w/t);
        }

        for (int i = 0; i != wp.size(); i++)
        {
            //cout<<wp[i]<<" "<<owp[i]<<" "<<oowp[i]<<endl;
            printf("%0.12f\n", 0.25 * wp[i] + 0.50 * owp[i] + 0.25 * oowp[i]);
        }

        //////////////////////////////////////
    }
    return 0;
}
