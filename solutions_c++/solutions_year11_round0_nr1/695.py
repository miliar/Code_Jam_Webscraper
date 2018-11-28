#include <cstdio>
#include <limits.h>
#include <vector>
#include <string.h>
#include <stdlib.h>
using namespace std;

#define SZ(v) ((int)(v).size())
#define PB push_back

void run(int casenr) {
	int at[2]; at[0]=at[1]=1;
	int t[2]; t[0]=t[1]=0;

	int n; scanf("%d",&n);
	for(int i=0;i<n;++i) {
		char who; int where; scanf(" %c%d",&who,&where);
		int me=who=='O'?0:1;
		t[me]+=abs(where-at[me]); at[me]=where;
		if(t[1-me]>t[me]) t[me]=t[1-me];
		t[me]++;
	}
	printf("Case #%d: %d\n",casenr,max(t[0],t[1]));
}

int main() {
	int n; scanf("%d",&n); for(int i=1;i<=n;++i) run(i);
	return 0;
}
