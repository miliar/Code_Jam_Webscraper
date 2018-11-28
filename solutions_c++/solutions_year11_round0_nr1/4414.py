#include <vector>
#include <map>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <queue>
#include <cstring>

using namespace std;

#define tfi "a.in"
#define tfo "a.out"
ifstream fi(tfi);
ofstream fo(tfo);
#define cin fi
#define cout fo

#define FOREACH(it,c) for( __typeof((c).begin()) it=(c).begin();it!=(c).end();it++)
#define FOR(i,a,b) for( int i=(a),_b=(b);i<=_b;i++) 
#define DOW(i,b,a) for( int i=(b),_a=(a);i>=_a;i--)
#define REP(i,n) FOR(i,0,(n)-1)
#define DEP(i,n) DOW(i,(n)-1,0)
#define all(a) (a).begin() , (a).end()

typedef vector<int> VI ;
typedef vector<string> VS ;
template<class T> inline int size(const T&c) { return c.size(); }  

long n, result;
string s;
vector <int> a, b, full_step;
int step, lasta, lastb;
int sleepa, sleepb, curra, currb;

main()
{
    cin>>n;
    getline(cin, s);
    REP(kk, n)
    {
        a.clear();
        b.clear();
        full_step.clear();
        lasta=0; lastb=0;
        getline(cin, s);
        stringstream ss (stringstream::in | stringstream::out);
        ss<<s;
        ss>>step;
        result=0;
        sleepa=0; sleepb=0;
        curra=1; currb=1;
        REP(i, step)
        {
            string tmp;
            long x;
            ss>>tmp; ss>>x;
            if (tmp=="O") a.push_back(x); else b.push_back(x);
            if (tmp=="O") full_step.push_back(x); else full_step.push_back(-x);
        }            
        REP(i, full_step.size())
            {
                int xx=full_step[i];
                if (xx>0)
                {
                        if (sleepa > abs(xx-curra)) {sleepa-=abs(xx-curra); curra=xx;} else
                        {
                        result+=abs(xx-curra)-sleepa;
                        sleepb+=abs(xx-curra)-sleepa    ;
                        sleepa=0;
                        }
                    result+=1;
                    sleepb+=1;
                    sleepa=0;
                    curra=xx;
                } else
                {
                    xx=-xx;
                        if (sleepb > abs(xx-currb)) {sleepb-=abs(xx-currb); currb=xx;} else
                        {
                            result+=abs(xx-currb)-sleepb;
                            sleepa+=abs(xx-currb)-sleepb;
                            sleepb=0;
                        }
                    result+=1;
                    sleepa+=1;
                    sleepb=0;
                    currb=xx;
                }
            }

        cout<<"Case #"<<kk+1<<": "<<result<<endl;
    }
    return 0;
}