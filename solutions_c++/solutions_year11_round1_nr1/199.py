#include <cstdio>
#include <iostream>

using namespace std;

long long N;
int PD,PG;

bool Work(){
	scanf("%I64d %d %d",&N,&PD,&PG);
	if (PG==0) return (PD==0);
	if (PG==100) return (PD==100);
	for (int D=1;D<=N;D++){
		if (PD*D%100==0) return true;
	}
	return false;
}

int main(){
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	int Test;scanf("%d",&Test);
	for (int kase=1;kase<=Test;kase++){
		if (Work()) printf("Case #%d: Possible\n",kase);
		else printf("Case #%d: Broken\n",kase);
	}
	return 0;
}
	
	
