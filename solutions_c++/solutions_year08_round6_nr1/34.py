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

int d1,d2,x1,x2;
vector<int> t1,t2;

int main()
{
        int caseNumber;
        cin>>caseNumber;
        REP(caseIndex, caseNumber)
        {
                int N,M;
                cin>>N;
                d1=d2=-1;x1=x2=1000000;
                t1.clear();t2.clear();
                REP(i,N)
                {
                        int p1,p2;
                        string s;
                        cin>>p1>>p2>>s;
                        if (s=="BIRD")
                        {
                                d1=max(d1,p1);
                                x1=min(x1,p1);
                                d2=max(d2,p2);
                                x2=min(x2,p2);
                        }
                        else
                        {
                                cin>>s;
                                t1.push_back(p1);
                                t2.push_back(p2);
                        }
                }
                cin>>M;
                printf("Case #%d:\n", caseIndex+1);
                REP(i,M){
                        int p1,p2;
                        cin>>p1>>p2;
                        if (p1<=d1 && p1>=x1 && p2<=d2 && p2>=x2)
                                puts("BIRD");
                        else
                        {
                                int bad=0;
                                int nd1,nd2,nx1,nx2;
                                nd1=max(d1,p1);
                                nd2=max(d2,p2);
                                nx1=min(x1,p1);
                                nx2=min(x2,p2);
                                REP(j,t1.size())
                                {
                                        if (t1[j]<=nd1 && t1[j]>=nx1 && t2[j]<=nd2 && t2[j]>=nx2)
                                                bad=1;
                                }
                                if (bad)
                                        puts("NOT BIRD");
                                else
                                        puts("UNKNOWN");
                        }
                }
        }
}
