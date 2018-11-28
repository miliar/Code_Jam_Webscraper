#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int tc, ntc;
int n, k;
char s[100000];

int ndif[16][16];
int nd2[16][16];

void gen_ndif()
{
	memset(ndif,0,sizeof(ndif));
	int i;
	
	int a, b;
	for (i=0; i<n; i+=k)
	{
		for (a=0; a<k; a++) for (b=0; b<k; b++) if (a!=b)
			if (s[i+a] != s[i+b]) ndif[a][b]++;
	}
	
//	for (a=0; a<k; a++) for (b=0; b<k; b++) if (a!=b)
//		printf("%d %d %d\n",a,b,ndif[a][b]);
//	printf("\n");
	
	memset(nd2,0,sizeof(nd2));
	for (i=0; i+k<n; i+=k)
	{
		for (a=0; a<k; a++) for (b=0; b<k; b++) if (a!=b)
			if (s[i+a] != s[i+k+b]) nd2[a][b]++;
	}	
	
//	for (a=0; a<k; a++) for (b=0; b<k; b++) if (a!=b)
//		printf("%d %d %d\n",a,b,nd2[a][b]);
//	printf("\n");
	
}

#define INF 10000000
int dp[1<<16][16];

int first;
int doit(int mask, int last)
{
	if (mask == (1<<k)-1)
		return nd2[last][first];
		
	int& res = dp[mask][last];
	if (res != -1) return res;
	
	res = INF;
	int i;
	for (i=0; i<k; i++) if (!(mask&(1<<i)))
	{
		res <?= ndif[last][i] + doit(mask ^ (1<<i), i);
	}
	
//	printf("%d %d : %d\n",mask,last, res);
	
	return res;
}

int main()
{
	scanf("%d",&ntc);
	int i;
	int res;
	for (tc=1; tc<=ntc; tc++)
	{
		scanf("%d",&k);
		scanf("%s",s);		
		n = strlen(s);

		res = INF;
		
		gen_ndif();
		for (i=0; i<k; i++) 
		{
			memset(dp,-1,sizeof(dp));
			first = i;
			res <?= doit( 1<<i, i );
		}						
		res++;
		
		printf("Case #%d: %d\n",tc,res);
		fprintf(stderr,"Case #%d: %d\n",tc,res);
	}
}