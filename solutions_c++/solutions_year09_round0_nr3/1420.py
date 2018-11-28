#include <iostream>
#include <vector>

#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;

string x ="$welcome to code jam";

char S[512];
int D[512][21];

int solve()
{
    int n=0;
    S[n]='#';
    while(1)
    {
        ++n;
        scanf("%c",&S[n]);
        if(S[n]=='\n' || S[n]==EOF) break;
    }
    if(n<20) return 0;
    S[n]=0;
    fru(i,n) D[i][0]=1;
    for(int i=1;i<n;++i)for(int k=1;k<x.size();++k)
        {
            D[i][k]=D[i-1][k];
            if(S[i]==x[k]) D[i][k]=(D[i][k]+D[i-1][k-1])%10000;
        }
   return D[n-1][x.size()-1];
}

int main()
{
    int t;
    scanf("%d ",&t);
    fru(i,t) printf("Case #%d: %04d\n",i+1,solve());
#ifdef __WIN32
//    system ("pause");
#endif
return 0;
}
