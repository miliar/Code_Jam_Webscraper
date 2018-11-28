#include <iostream>
#include <vector>

#define fru(j,n) for(int j=0;j<n;++j)
#define tr(it,x) for(typeof(x.begin())it=x.begin();it!=x.end();++it)
#define x first
#define y second

using namespace std;
typedef pair<int,int> pii;
typedef long long LL;

const int N=102;
int W[N][N];
char C[N][N];
int A,B;
bool ok(int a, int b) { return a>=0 && b>=0 && a<A && b<B; }

//North, West, East, South.

int x[] = {-1,0,0,1};
int y[] = {0,-1,1,0};

char ten;

char go(int a, int b)
{
    if(C[a][b]) return C[a][b];
    int ja=W[a][b];
    fru(k,4) if(ok(a+x[k],b+y[k])) if(W[a+x[k]][b+y[k]]<ja) ja=W[a+x[k]][b+y[k]];
    if(ja==W[a][b])
    {
        C[a][b]=ten;
        ++ten;
    }
    else fru(k,4) if(ok(a+x[k],b+y[k])) if(W[a+x[k]][b+y[k]]==ja)
    {
        C[a][b]=go(a+x[k],b+y[k]);
        break;
    }
    return C[a][b];
}

void solve(int test)
{
    ten='a';
    scanf("%d%d",&A,&B);
    fru(i,A) fru(j,B) scanf("%d",&W[i][j]);
    fru(i,A) fru(j,B) C[i][j]=0;
    printf("Case #%d:\n",test+1);
    fru(i,A) fru(j,B) printf("%c%c",go(i,j),j+1<B?' ':'\n');
}

int main()
{
    int t;
    scanf("%d",&t);
    fru(i,t) solve(i);
#ifdef __WIN32
 //   system ("pause");
#endif
return 0;
}
