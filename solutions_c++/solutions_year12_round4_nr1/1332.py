#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>
#include <queue>
using namespace std;

int n;
int love;
int d[10000];
int l[10000];
int atteint[10000];

bool parcours(int liane, int taille)
{
    if(atteint[liane] >= taille) return false;
    if(d[liane] + taille >= love) return true;
    if(liane == n-1) return false;
    int next = liane+1;
    while(next < n && d[next] <= d[liane] + taille)
    {
	if(parcours(next, min(d[next] - d[liane], l[next])))
	    return true;
	next++;
    }
    return false;
}

int main()
{
    int nbcas;
    scanf("%d", &nbcas);
    for(int cas = 1; cas <= nbcas; cas++)
    {
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
	    scanf("%d%d", &d[i], &l[i]);
	scanf("%d", &love);
	for(int i = 0; i < n; i++)
	    atteint[i] = -1;
	if(parcours(0,d[0]))
	    printf("Case #%d: YES\n", cas);
	else 
	    printf("Case #%d: NO\n", cas);
    }
    return 0;
}
