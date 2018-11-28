/* 
 * File:   main.cpp
 * Author: NIKUNJ
 *
 * Created on May 7, 2011, 3:43 PM
 */

#include <cstdlib>
#include <cstdio>
#include <iostream>
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


/*
 * 
 */
int main()
{
    freopen("A-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t=SS;
    REP(i,t)
    {
        int n=SS,blu=1,ora=1,tim=0,blulast=0,oralast=0;
        
        REP(j,n)
        {
            char ch;
            cin>>ch;
            int b=SS;
            if(ch=='O')
            {
                if(tim-oralast)
                {
                    if(abs(ora-b)>(tim-oralast))
                    {
                        tim+=(abs(ora-b)-tim+oralast+1);
                    }
                    else
                        tim++;
                }
                else
                {
                    tim+=(abs(ora-b)+1);
                    
                }
                ora=b;
                oralast=tim;
            }
            else
            {
                if(tim-blulast)
                {
                    if(abs(blu-b)>(tim-blulast))
                        tim+=(abs(blu-b)+1-tim+blulast);
                    else tim++;
                    
                }
                else
                {
                    tim+=(abs(blu-b)+1);
                }
                blu=b;
                blulast=tim;
            }
        }
        printf("Case #%d: %d\n",i+1,tim);
    }
    fclose(stdout);
    return 0;
}

