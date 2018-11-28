#include <algorithm>
#include <string>
#include <vector>
#include <queue>
#include <iostream>
#include <cmath>
#include <sstream>
#include <map>
#include <set>
#include <numeric>
#include <memory.h>
#include <cstdio>
#include <assert.h>

using namespace std;

#define pb push_back
#define INF 101111111
#define FOR(i,a,b) for (int _n(b), i(a); i < _n; i++)
#define rep(i,n) FOR(i,0,n)
#define ford(i,a,b) for(int i=(a),_b=(b);i>=_b;--i)
#define CL(a,v) memset((a),(v),sizeof(a))
#define mp make_pair
#define X first
#define Y second
#define all(c) (c).begin(), (c).end()
#define SORT(c) sort(all(c))

typedef long long ll;
typedef vector<int> VI;
typedef pair<int,int> pii;

string in[] = {"ejp mysljylc kd kxveddknmc re jsicpdrysi",
              "rbcpc ypc rtcsra dkh wyfrepkym veddknkmkrkcd",
              "de kr kd eoya kw aej tysr re ujdr lkgc jv"};

string out[] = {"our language is impossible to understand",
                "there are twenty six factorial possibilities",
                "so it is okay if you want to just give up"
                };

int main()
{
	#ifndef ONLINE_JUDGE
        //freopen("input.txt","r",stdin);
        freopen("A-small-attempt0.in","r",stdin);
        freopen("A_output.txt","w",stdout);
	#endif

    char F[256];
    rep(i,256) F[i] = '?';

    F[' '] = ' '; F['y'] = 'a'; F['e'] = 'o'; F['q'] = 'z'; F['z'] = 'q';

    rep(i,3)
    {
        rep(j,in[i].size())
        {
            if(F[in[i][j]] == '?')
            {
                F[in[i][j]] = out[i][j];
            }
            else
            {
                if(F[in[i][j]] != out[i][j])
                {
                    cout << F[in[i][j]] << " : " << out[i][j] ;
                }
                assert(F[in[i][j]] == out[i][j]);
            }
        }
    }

    //set<char> ss;
    //for(char c = 'a'; c <= 'z'; ++c) ss.insert(c); //cout << c << " : " << F[c] << endl;
    //for(char c = 'a'; c <= 'z'; ++c) ss.erase(F[c]);

    //cout << *(ss.begin()) << endl;


    int T;
    cin >> T;
    char buff[1024];
    gets(buff);

    FOR(t,1,T+1)
    {
        gets(buff);
        printf("Case #%d: ",t);
        rep(i,strlen(buff)) cout << F[buff[i]]; cout << endl;
    }


	return 0;
}
