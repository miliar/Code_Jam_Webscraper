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
        int caseNumber;
        cin>>caseNumber;
        REP(caseIndex, caseNumber)
        {
                int g1[10][10],g2[10][10];
                memset(g1,0,sizeof g1);memset(g2,0,sizeof g2);
                int N,M;
                cin>>N;
                REP(i,N-1)
                {
                        int t1,t2;
                        cin>>t1>>t2;t1--;t2--;
                        g1[t1][t2]=g1[t2][t1]=1;
                }
                cin>>M;
                REP(i,M-1)
                {
                        int t1,t2;
                        cin>>t1>>t2;t1--;t2--;
                        g2[t1][t2]=g2[t2][t1]=1;
                }
                int t[10];
                REP(i,N)
                        t[i]=i;
                int y=0;
                do
                {
                        int t1=1;
                        REP(i,M)
                                REP(j,M)
                                        if (g1[t[i]][t[j]]!=g2[i][j])
                                                t1=0;
                        y|=t1;
                        /*if (t1==1)
                        {
                                REP(i,N)
                                        cout<<t[i]<<"   ";
                                cout<<endl;
                        }*/
                }while (next_permutation(t,t+N));
                printf("Case #%d: ", caseIndex+1);
                if (y)
                        puts("YES");
                else
                        puts("NO");
        }
}
