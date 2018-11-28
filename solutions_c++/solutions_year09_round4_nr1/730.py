#include <iostream>
#include <vector>

#define fru(j,n) for(int j=1;j<=n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;

const int M=50;
char s[M];

int t[M];

int solve()
{
    s[0]='1';
    int a;
    scanf("%d",&a);
    fru(k,a) 
    {
        scanf(" %s",s+1);
        for(int i=a;1;--i) if(s[i]=='1') {t[k]=i; break; }
    }
    int ret=0;
    fru(i,a) 
    {
        int j=i;
        while(t[j]>i) ++j;
        while(j>i)
        {
            swap(t[j],t[j-1]);
            --j;
            ++ret;
        }
//        fru(k,a) printf("%d\n",t[k]); printf("\n\n\n");
    }
    return ret;
}

int main()
{
    int t;
    scanf("%d",&t);
    fru(i,t) printf("Case #%d: %d\n",i,solve());
return 0;
}
/*
ID: bardek.1
LANG: C++
TASK: ___
*/
//FILE *plik = fopen("___.in","r");
//FILE *out = fopen("___.out","w");

//fclose(plik);fclose(out);
