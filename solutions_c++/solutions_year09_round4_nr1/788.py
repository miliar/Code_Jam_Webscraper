#include<iostream>
#include<vector>
#include<algorithm>
#include<cmath>
#include<string>
#include<sstream>
#include<map>
#include<queue>
#include<stack>
#include<cstring>
#include<cstdlib>
#include<list>
#include<set>
#define pb push_back
#define mp make_pair
#define x first
#define y second
#define vi vector<int>
#define vd vector<double>
#define pii pair<int,int>
#define pdd pair<double,double>
using namespace std;
int tests,tcounter;
int N;
bool can[64][64];
string A[64];
int last(int row)
{
    int i;
    for(i=N-1;i>=0;--i)if(A[row][i]=='1')return i;
    return -1;
}
int main()
{
    int i,j,k,ans;
    scanf("%d",&tests);
    for(tcounter=1;tcounter<=tests;++tcounter)
    {
        printf("Case #%d: ",tcounter);
        ans=0;
        scanf("%d\n",&N);
        for(i=0;i<N;++i)cin>>A[i];
        for(i=0;i<N;++i)
        {
            for(j=i;j<N;++j)if(last(j)<=i)break;
            ans+=j-i;
            for(k=j-1;k>=i;--k)swap(A[k],A[k+1]);
        }
        printf("%d\n",ans);
    }
    return 0;
}
