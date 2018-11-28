#include<cstdio>
#include<cstring>
#include<vector>
#include<algorithm>
using namespace std;
int L,D,N;
int main()
{
    int i,j,k;
    char W[5020][20],A[1024];
    bool can[20][26];
    scanf("%d %d %d\n",&L,&D,&N);
    for(i=0;i<D;++i)scanf("%s\n",W[i]);
    for(k=0;k<N;++k)
    {
        scanf("%s\n",A);
        for(i=0;i<L;++i)
            for(j=0;j<26;++j)can[i][j]=false;
        bool alter=false;
        int pos=0,ans=0;
        for(i=0;i<strlen(A);++i)
        {
            if(A[i]=='(')
            {
                alter=true;
                continue;
            }
            if(A[i]==')')
            {
                alter=false;
                ++pos;
                continue;
            }
            if(!alter)can[pos++][A[i]-'a']=true;
            else can[pos][A[i]-'a']=true;
        }
        for(i=0;i<D;++i)
        {
            for(j=0;j<strlen(W[i]);++j)if(!can[j][W[i][j]-'a'])goto ends;
            ++ans;
            ends:;
        }
        printf("Case #%d: %d\n",k+1,ans);
    }
    return 0;
}
