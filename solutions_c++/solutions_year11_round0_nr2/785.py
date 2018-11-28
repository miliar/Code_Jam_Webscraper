#include <cstdio>
#include <vector>
using namespace std;

int C,D,N,cnt[26];
char t[4],s[102],give[26][26];
bool op[26][26];
vector<char> V;
int main ()
{
    freopen("input.in","r",stdin);freopen("input.out","w",stdout);
    int T;
    scanf("%d",&T);
    for (int z=1;z<=T;++z)
    {
    for (int i=0;i<26;++i)
    {
        cnt[i]=0;
        for (int j=0;j<26;++j) give[i][j]=op[i][j]=0;
    }
    V.clear();
    scanf("%d",&C);
    for (int i=1;i<=C;++i) scanf("%s",t),give[t[0]-'A'][t[1]-'A']=give[t[1]-'A'][t[0]-'A']=t[2];
    scanf("%d",&D);
    for (int i=1;i<=D;++i) scanf("%s",t),op[t[0]-'A'][t[1]-'A']=op[t[1]-'A'][t[0]-'A']=1;
    scanf("%d %s",&N,s);
    for (int i=0;i<N;++i)
    {
        if (V.empty()) V.push_back(s[i]),cnt[s[i]-'A']=1;
        else if (give[s[i]-'A'][V[V.size()-1]-'A']) --cnt[V[V.size()-1]-'A'],V[V.size()-1]=give[s[i]-'A'][V[V.size()-1]-'A'];
        else
        {
            bool ok=0;
            for (int j=0;j<26;++j) if (op[j][s[i]-'A'] && cnt[j])
            {
                V.clear();
                for (int k=0;k<26;++k) cnt[k]=0;
                ok=1;
                break;
            }
            if (ok) continue;
            V.push_back(s[i]);++cnt[s[i]-'A'];
        }
    }
    printf("Case #%d: ",z);
    if (V.empty()) printf("[]\n");
    else
    {
        printf("[%c",V[0]);
        for (int i=1;i<V.size();++i) printf(", %c",V[i]);
        printf("]\n");
    }
    }
    return 0;
}
