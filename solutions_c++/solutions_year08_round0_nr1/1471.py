#include <cstdio>
#include <map>
#include <string>
using namespace std;

const int MAXS = 101;
const int MAXQ = 1001;
const int INF = 20000;
int S, Q;
map<string, int> eng;
char buf[10000];
int f[MAXQ][MAXS];

void init()
{
    eng.clear();
    scanf("%d\n", &S);
    for (int i=0; i<S; i++) {
	gets(buf);
	eng[string(buf)] = i;
    }
    scanf("%d\n", &Q);
}

void solve()
{
    for (int i=0; i<S; i++) f[0][i] = 0;
    for (int i=1; i<=Q; i++) {
	gets(buf);
	int q = eng[string(buf)];
	for (int j=0; j<S; j++) {
	    if (j!=q) {
		int Min = INF;
		for (int k=0; k<S; k++)
		    if (f[i-1][k] + (j!=k) < Min) Min = f[i-1][k] + (j!=k);
		f[i][j] = Min;
	    }
	    else f[i][j] = INF;
//	    printf("f[%d][%d] = %d\n", i,j,f[i][j]);
	}
    }
    int Min = INF;
    for (int i=0; i<S; i++)
	if (f[Q][i] < Min) Min = f[Q][i];
    printf("%d\n", Min);
}


int main(int argc, char* argv[])
{
    freopen(argv[1],"r",stdin);
    int cases;
    scanf("%d", &cases);
    for (int i=1; i<=cases; ++i) {
	init();
	printf("Case #%d: ", i);
       	solve();
    }
    return 0;
}

