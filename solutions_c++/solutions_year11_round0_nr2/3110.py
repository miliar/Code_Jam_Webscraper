/* 
 * File:   main.cpp
 * Author: NIKUNJ
 *
 * Created on May 7, 2011, 3:43 PM
 */

#include <vector>
#include <string>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <ctype.h>
#include <bitset>
#include <assert.h>

using namespace std;

#define REP(i, n) for(int i=0; i<(n); i++)
#define FOR(i, a, b) for(int i=(a); i<(b); i++)
#define IFOR(i, a, b) for(int i=(a); i>=(b); i--)
#define FORD(i, a, b, c) for(int i=(a); i<(b); i+=(c))

#define SS ({int x;scanf("%d", &x);x;})
#define SI(x) ((int)x.size())
#define PB(x) push_back(x)
#define MP(a,b) make_pair(a, b)
#define SORT(a) sort(a.begin(),a.end())
#define ITER(it,a) for(typeof(a.begin()) it = a.begin(); it!=a.end(); it++)
#define ALL(a) a.begin(),a.end()
#define INF 1000000000
#define V vector
#define S string
#define FST first
#define SEC second

typedef V<int> VI;
typedef V<S> VS;
typedef long long LL;
typedef pair<int, int> PII;


/*
 * 
 */
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("output.txt","w",stdout);
    int t=SS,flag;
    REP(i,t)
    {
        map < pair<char,char> , char > combine;
        map < pair<char,char> , int > oppose;
        int c,d,n;
        c=SS;
        REP(j,c)
        {
            string s;
            cin>>s;
            combine[MP(s[0],s[1])]=s[2];
            combine[MP(s[1],s[0])]=s[2];
        }
        d=SS;
        REP(j,d)
        {
            string s;
            cin>>s;
            oppose[MP(s[0],s[1])]=1;
            oppose[MP(s[1],s[0])]=1;
        }
        n=SS;
        vector <char> seq(n);
        int sp=-1;
        char ch;
        REP(j,n)
        {
            cin>>ch;
            flag=0;
            if(sp>-1)
            {
                if(combine[MP(ch,seq[sp])])
                {
                    seq[sp]=combine[MP(ch,seq[sp])];
                    flag=1;
                }
                else
                {
                    REP(k,sp+1)
                    {
                        if(oppose[MP(ch,seq[k])])
                        {
                            seq.clear();
                            sp=-1;
                            flag=1;
                            break;
                        }
                    }
                }
                if(flag==0)
                {
                    seq[++sp]=ch;
                    //sp++;
                }
            }
            else
            {
                seq[++sp]=ch;
            }
        }
        printf("Case #%d: [",i+1);
        if(sp==-1)
            printf("]\n");
        else
        REP(j,sp+1)
        {
            if(j==sp)
            {
                printf("%c]\n",seq[j]);
            }
            else
                printf("%c, ",seq[j]);
        }
    }
    fclose(stdout);
    return 0;
}

