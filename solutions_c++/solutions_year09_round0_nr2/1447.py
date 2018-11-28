/* B Large
* @author Mircea Dima
*/
#include <cstdio>
#include <cstring>

int a[101][101];
int n, m;
char s[101][101];

int T;

const int xx[]={1, 0, 0, -1};
const int yy[]={0, 1, -1, 0};

char ch = 'a'-1;
char C;

void pushFlow(int i, int j)
{
    int mn = 0x3f3f3f3f;
    int k;
    int nx, ny;
    int pi, pj;

    for(k = 0; k < 4; ++k)
    {
	nx = i + xx[k];
	ny = j + yy[k];

	if(nx >= 1 && nx <= n && ny >= 1 && ny <= m)
	    if(a[nx][ny] < a[i][j])
		if(mn >= a[nx][ny])
		    mn = a[nx][ny],
		    pi = nx,
		    pj = ny;
    }

        
    if(mn != 0x3f3f3f3f && s[pi][pj] != 0)
    {
	C= s[pi][pj];
	s[i][j] = C;
	return;
    }
    if(mn != 0x3f3f3f3f)
    {
	pushFlow(pi,pj);
	s[i][j] = C;
    }
    else
    {
	if(s[i][j] == 0)
	{
	    C = ++ch;
	    s[i][j] = C;
	}
	else C = s[i][j];
	
    }

}

void solve(int t)
{
    int i, j, k;
   
    ch = 'a'-1; 
    char c = 'a' - 1;

    for(i = 1; i <= n; ++i)
	for(j = 1; j <= m; ++j)
	if(s[i][j] == 0)
	{
	    pushFlow(i,j);
    	}

    printf("Case #%d:\n", t);
    for(i = 1; i <= n; ++i)
    {
	for(j = 1; j <= m; ++j)
	    printf("%c ", s[i][j]);
	printf("\n");
    }

}

int main()
{
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);    
    scanf("%d\n", &T);
    for(int t = 1; t <= T; ++t)
    {
	memset(a, 0, sizeof(a));
	memset(s, 0, sizeof(s));

	scanf("%d %d\n", &n, &m);
	for(int i = 1; i <= n; ++i)
	    for(int j = 1; j <= m; ++j)
		scanf("%d ", &a[i][j]);
	solve(t);
    }
    return 0;
}

