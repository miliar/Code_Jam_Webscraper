#include <cstdio>
#include <cstdlib>
#include <string>
#include <list>
#include <set>
#include <map>
#include <algorithm>
#include <vector>
#include <cmath>
#include <queue>
#include <cctype>
using namespace std;
#define inf 1100000000
int sc, nsc;
char eng[110][110];
char q[1100];
int neng, nq;
char work[110];
int next[1100][110];
void init(){
	int i;
	scanf("%d", &neng);
	gets(work);
	for(i=1;i<=neng;i++)
		gets(eng[i]);
}
int getind(char *s){
	int i;
	for(i=1;i<=neng;i++)
		if (strcmp(s, eng[i])==0) return i;
	return 0;
}
void solve(){
	int i,j;
	int best;
	int res;
	int curpos;
	int cureng;
	scanf("%d", &nq);
	gets(work);
	for(i=1;i<=nq;i++){
		gets(work);
		q[i]=getind(work);
	}
	printf("Case #%d: ", sc);
	if (nq==0){
		printf("0\n");
	}
	else{
		 for(i=1;i<=neng;i++)
			 next[nq+1][i]=inf;
		 for(i=nq;i>=1;i--){
			for(j=1;j<=neng;j++)
				next[i][j]=next[i+1][j];
			next[i][q[i]]=i;
		 }
		 res=0;
		 best=1;
		 for(i=2;i<=neng;i++)
			 if (next[1][best]<next[1][i])
				 best=i;
		 curpos=next[1][best];
		 cureng=best;
		 while (curpos<=nq){
			res++;
			best=1;
			for(i=2;i<=neng;i++)
				if (next[curpos][best]<next[curpos][i])
					best=i;
			curpos=next[curpos][best];
			cureng=best;
		 }
		 printf("%d\n", res);
	}
}
int main(){
	freopen("input.txt","r",stdin);
	freopen("output.txt","w",stdout);
	scanf("%d", &nsc);
	for(sc=1; sc<=nsc; sc++){
		init();
		solve();
	}
	return 0;
}