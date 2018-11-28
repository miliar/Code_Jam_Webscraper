#include<stdio.h>
#include<algorithm>
using namespace std;
const int MAXN = 10005;
int p[MAXN], l[MAXN];
int nmax[MAXN], n, d;
inline bool fuck()
{
	if(p[0] > l[0])
		return false;
	nmax[0] = p[0];
	if(nmax[0] >= d - p[0])
		return true;
    for(int i = 0; i < n; ++i)
    {
        if(nmax[i] >= d - p[i])
            return true;
        for(int j = i + 1; j < n; ++j)
        {
            int tmp = p[j] - p[i];
            if(nmax[i] < tmp)
                continue;
			nmax[j] = max(min(tmp,l[j]), nmax[j]);
        }
    }
    return false;
}
int main()
{
    freopen("in.in","r",stdin);
    freopen("out.txt","w",stdout);
    int c, sc = 0;
    for(scanf("%d",&c); c; --c)
    {
        scanf("%d",&n);
        for(int i = 0; i < n; ++i)
        {
            scanf("%d%d",&p[i],&l[i]);
            nmax[i] = -1;
        }
        scanf("%d",&d);
		printf("Case #%d: ",++sc);
        puts(fuck()?"YES":"NO");
    }
    return 0;
}

