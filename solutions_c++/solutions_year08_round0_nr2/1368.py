#include	<cstdio>
#include	<cstdlib>
#include	<cstring>
#include	<string>
#include	<vector>
#include	<cmath>
#include	<algorithm>
#include	<cassert>
#include	<set>
#include	<map>
#include	<queue>
#include	<iostream>
#include <fstream>
using namespace std;
#define pb push_back
#define REP(i,n) for(int i=0;i<(n);i++ ) 

typedef long long LL;
typedef pair<int,int> piii;

struct train
{
        int a,b;
        int dir;
};

bool operator<(const train&a, const train&b){
        return a.a<b.a;
}

int c1(string c)
{
        int t1=(c[0]-'0')*10+c[1]-'0';
        int t2=(c[3]-'0')*10+c[4]-'0';
        return t1*60+t2;
}

train tt[300];

int main()
{
        int N;
        cin>>N;
        REP(nn,N)
        {
                int T;
                cin>>T;
                int Na,Nb;
                cin>>Na>>Nb;
                string s1,s2;
                REP(i,Na)
                {
                        cin>>s1>>s2;
                        tt[i].a=c1(s1);
                        tt[i].b=c1(s2)+T;
                        tt[i].dir=0;
                }
                REP(i,Nb)
                {
                        cin>>s1>>s2;
                        tt[Na+i].a=c1(s1);
                        tt[Na+i].b=c1(s2)+T;
                        tt[Na+i].dir=1;
                }
                sort(tt,tt+Na+Nb);
                int r1=0,r2=0;
                priority_queue<int> l,r;
                REP(i,Na+Nb)
                {
                        train t=tt[i];
                        if (t.dir==0)
                        {
                                if  (l.size()==0 || (-l.top()>t.a))
                                        r1++;
                                else
                                        l.pop();
                                r.push(-t.b);
                        }
                        else
                        {
                                if  (r.size()==0 || (-r.top()>t.a))
                                        r2++;
                                else
                                        r.pop();
                                l.push(-t.b);
                        }
                }
                printf("Case #%d: %d %d\n",nn+1,r1,r2);
        }
        return 0;
}
