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

int main()
{
        int T;
        int K;
        string S,S2;
        cin>>T;
        REP(cas,T)
        {
                printf("Case #%d: ",cas+1);
                int per[100];
                cin>>K;
                cin>>S;
                S2=S;
                REP(i,K)
                        per[i]=i;
                int res=1000000;
                do
                {
                        REP(i,S.size()/K)
                                REP(j,K)
                                        S2[i*K+j]=S[i*K+per[j]];
                        int local=0;
                        REP(i,S.size())
                        {
                                if (i==0 || S2[i]!=S2[i-1])
                                        local++;
                        }
                        res=min(res,local);
                } while (next_permutation(per,per+K));
                printf("%d\n",res);
        }
        return 0;
}
