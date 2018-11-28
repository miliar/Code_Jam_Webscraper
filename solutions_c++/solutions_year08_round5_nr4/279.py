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
int W,H,R;

int sol[200][200];

int main()
{
        cin>>testCase;
        REP(testIndex,testCase)
        {
                cin>>W>>H>>R;
                memset(sol,0,sizeof sol);
                while (R--)
                {
                        int t1,t2;
                        cin>>t1>>t2;
                        sol[t1-1][t2-1]=-1;
                }
                sol[0][0]=(sol[0][0]==-1)?-1:1;
                REP(i,W)
                        REP(j,H)
                                if (sol[i][j]!=-1)
                        {
                                //cout<<i<<' '<<j<<' '<<sol[i][j]<<endl;
                                if (sol[i+2][j+1]!=-1)
                                        sol[i+2][j+1]=(sol[i+2][j+1]+sol[i][j])%10007;
                                if (sol[i+1][j+2]!=-1)
                                        sol[i+1][j+2]=(sol[i+1][j+2]+sol[i][j])%10007;
                        }
                printf("Case #%d: %d\n",testIndex+1,sol[W-1][H-1]%10007);
        }
}
