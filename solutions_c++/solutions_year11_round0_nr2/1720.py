#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <numeric>
#include <cmath>
#include <cstring>
#include <complex>
#include <cstdlib>
#include <climits>
using namespace std;

#define REP(i,n) for (int i=0; i<(int)(n); ++i)
#define REPS(p,s) for (char * p = s; *p ; p++)
#define FOR(var,start,end) for (int var=(start); var<=(int)(end); ++var)
#define FORD(var,start,end) for (int var=(start); var>=(int)(end); --var) 
#define PB push_back
#define PF push_front
#define BP pop_back
#define FP pop_front
#define BN begin()
#define RN rbegin()
#define RD rend()
#define ED end()
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define IT(X) __typeof((X).BN)
#define RIT(X) __typeof((X).RN) 
#define REF(X) __typeof(__typeof(X)::reference) 
#define FORIT(it, X) for(IT(X) it = (X).BN; it != (X).ED; ++it)
#define FORITR(it, X) for(RIT(X) it = (X).RN; it != (X).RD; ++it) 
#define VV(X) vector < vector< X > >
#define PIB(X)  pair<IT(X),bool >  

typedef long long LL;
typedef unsigned long long ULL;
typedef istringstream ISS;
typedef vector<int> VI;
typedef pair<int,int> PII;
typedef vector< PII > VPII;	

int main()
{
    int cases,count;
    cin >> cases;
    count = 1;
    while(cases>0)
    {
        int c,d,n,ff;
        char tof;
        string ip,word,rep;
        vector <string> dv;
        map <string, char> cv;
        size_t found;
        cin >> c;
        REP(i,c)
        {
            cin >> ip;
            cv[ip.substr(0,2)]=ip[2];
        }
        cin >> d;
        REP(i,d)
        {
            cin >> ip;
            dv.PB(ip);
        }
        cin >> n;
        cin >> word;
        for(int i=1;i<word.length();i++)
        {

            if(cv[word.substr(i-1,2)])
            {
                rep=cv[word.substr(i-1,2)];
                word.replace(i-1,2,rep);
                i--;
                continue;
            }
            else
            {
                rep=word[i];
                rep+=word[i-1];
                if(cv[rep])
                {
                    rep=cv[rep];
                    word.replace(i-1,2,rep);
                    i--;
                    continue;
                }
            }
            for(int j=0;j<dv.size();j++)
            {
                ff=0;
                if(dv[j][0]==word[i])
                {
                    rep=dv[j][1];
                    ff=1;
                }
                else if(dv[j][1]==word[i])
                {
                    rep=dv[j][0];
                    ff=1;
                }
                if(ff)
                {
                    found=word.substr(0,i).find(rep);
                    if(found!=string::npos)
                    {
                        word=word.substr(i+1);
                        i=0;
                        break;
                    }
                }
            }
//            cout << word << endl;
        }
        cout << "Case #"<<count<<": ["; 
        for(int i=0;i<word.length();i++)
        {   
            if(i+1==word.length())
                cout<<word[i];
            else
                cout << word[i]<<", ";
        }
        cout <<"]"<<endl;


        count ++;
        cases--;
    }
    return 0;
}
