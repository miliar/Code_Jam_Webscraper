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

int t[200][200][2];
int tot[200];

int main()
{
        int T;
        cin>>T;
        REP(t1,T)
        {
                int N;
                cin>>N;
                int M;
                cin>>M;
                REP(i,M)
                {
                        int P;
                        cin>>tot[i];
                        REP(j,tot[i])
                        {
                                cin>>t[i][j][0]>>t[i][j][1];
                                t[i][j][0]--;
                        }
                }
                int res=1000,resN=0;
                REP(i,(1<<N))
                {
                        int bit=0;
                        int B=i;
                        while (B)
                        {
                                bit+=B&1;
                                B/=2;
                        }
                        int sat=1;
                        REP(j,M)
                        {
                                int local=0;
                                REP(k,tot[j])
                                {
                                        if (t[j][k][1])
                                        {
                                                if (i&(1<<t[j][k][0]))
                                                        local=1;
                                        }
                                        else
                                        {
                                                if ((i&(1<<t[j][k][0]))==0)
                                                        local=1;
                                        }
                                }
                                sat&=local;
                        }
                        //cout<<i<<' '<<bit<<' '<<sat<<endl;
                        if (sat)
                                if (res>bit)
                                {
                                        res=bit;
                                        resN=i;
                                }
                }
                cout<<"Case #"<<t1+1<<": ";
                if (res>100)
                        cout<<"IMPOSSIBLE"<<endl;
                else
                {
                        REP(i,N)
                                if ((1<<i)&resN)
                                        cout<<"1 ";
                                else
                                        cout<<"0 ";
                        cout<<endl;
                }
        }
}
