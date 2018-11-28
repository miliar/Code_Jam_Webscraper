#include <stdio.h>
#include <string.h>
#include <math.h>
#include <string>
#include <set>
#include <map>
#include <algorithm>

using namespace std;

const int maxn = 10000;
const int INF = 1000000000;
const double eps = 1e-10;

#define nul(a) memset(a,0,sizeof(a))
#define fill(a,b) memset(a,b,sizeof(a))
#define sqr(a) ((a)*(a))

int k;
char s[maxn];
int l;

void init(){
	scanf("%d\n",&k);
	gets(s);
	l = strlen(s);
}

int f(char *s, int *per){
	int i;
	char ts[10];
	char s2[maxn];
	strcpy(s2,s);
	for (i = 0 ; i<l ; i+=k){
		int j;
		for (j = 0 ; j<k ; j++){
			ts[j] = s2[per[j]+i-1];
		}
		for (j = 0 ; j<k ; j++){
			s2[j+i] = ts[j];
		}
	}
	int res = 0;
	for (i = 0 ; i<l ; i++){
		if (s2[i]!=s2[i+1])
			res++;
	}
	return res;
}

void solve(){
	int per[10];
	int i;
	for (i = 0 ; i<k ; i++)
		per[i] = i+1;
	int res = INF;
	do
	{
		res = min(res,f(s,per));
	}
	while (next_permutation(per,per+k));
	printf("%d",res);
}

int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	int t,i;
	scanf("%d",&t);
	for (i = 0 ; i<t ; i++){
		printf("Case #%d: ",i+1);
		init();
		solve();
		printf("\n");
	}
	return 0;
}