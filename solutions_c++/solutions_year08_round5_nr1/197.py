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

int testCase;

set<piii> p1,p2,p3,p4;

int dir[4][2]={1,0,0,1,-1,0,0,-1};

int main()
{
        cin>>testCase;
        REP(testIndex,testCase)
        {
                int L;
                cin>>L;
                int x=0,y=0,d=0;
                p1.clear();
                int size=0;
                REP(i,L)
                {
                        string s;int rep;
                        cin>>s>>rep;
                        REP(j,rep)
                                REP(k,s.size())
                                {
                                        char c=s[k];
                                        if (c=='L')
                                                d=(d+1)%4;
                                        if (c=='R')
                                                d=(d+3)%4;
                                        if (c=='F')
                                        {
                                                int x2=x,y2=y;
                                                x+=dir[d][0];
                                                y+=dir[d][1];
                                                size+=(x*y2-x2*y);
                                                p1.insert(make_pair(x,y));
                                        }
                                }
                }
                cerr<<p1.size()<<endl;
                p2.clear();
                for (int x=-101;x<=101;x++)
                        for (int y=-101;y<=101;y++)
                        {
                                int p=0;
                                REP(d,4)
                                {
                                        int x1=x,y1=y,suc=0;
                                        while (1)
                                        {
                                                if (p1.find(make_pair(x1,y1))!=p1.end())
                                                {
                                                        suc=1;
                                                        break;
                                                }
                                                if (x1<=-102  || x1>=102 || y1<=-102 || y1>=102)
                                                        break;
                                                x1+=dir[d][0];
                                                y1+=dir[d][1];
                                        }
                                        if (suc)
                                                p+=(1<<d);
                                }
                                //cout<<x<<' '<<y<<' '<<p<<endl;
                                if ((p&5)==5 || (p&10)==10)
                                        //cout<<x<<' '<<y<<' '<<p<<endl;
                                        p2.insert(make_pair(x,y));
                        }
                cerr<<p2.size()<<endl;
                        if (size<0)
                                size=-size;
                int sol=0;
                for (int x=-101;x<=101;x++)
                        for (int y=-101;y<=101;y++)
                                if (p2.find(make_pair(x,y))!=p2.end() &&
                                        p2.find(make_pair(x+1,y))!=p2.end() &&
                                p2.find(make_pair(x,y+1))!=p2.end() &&
                                p2.find(make_pair(x+1,y+1))!=p2.end() )
                                sol++;
                printf("Case #%d: %d\n",testIndex+1,sol-size/2);
        }
}
