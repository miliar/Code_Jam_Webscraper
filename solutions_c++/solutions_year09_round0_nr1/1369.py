#include <iostream>
#include <set>
#include <vector>

#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;

const int DD=5005;

string a[DD];
char buf [512];

int L,d;
set<char> S[20];
int solve()
{
    scanf(" %s",buf);
    string q(buf);
    string::iterator it=q.begin();
    fru(i,L) S[i].clear();
    int ret=0;
    fru(i,L)
    {
        if(*it=='(')
        {
            ++it;
            do
            {
                S[i].insert(*it);
                ++it;
            }
            while(*it!=')');
        }
        else  S[i].insert(*it);
        ++it;
    }
    int w;
    fru(i,d) 
    {
        for(w=0;w<L;++w) if(S[w].find(a[i][w])==S[w].end()) break;
        if(w==L) ++ret;
    }
    return ret;
}

int main()
{
    int n;
    scanf("%d%d%d",&L,&d,&n);
    fru(i,d)
    {
        scanf(" %s",buf);
        a[i]=string(buf);
    }
    fru(i,n) printf("Case #%d: %d\n",i+1,solve());
#ifdef __WIN32
//    system ("pause");
#endif
return 0;
}
/*
3 5 4
abc
bca
dac
dbc
cba
(ab)(bc)(ca)
abc
(abc)(abc)(abc)
(zyx)bc
*/
