#include <cstdio>
#include <algorithm>
using namespace std;
int TT;
int M,V;

int change[100000];
int bit[100000];
int leaf[100000];

int calculate(int p) {
	if(leaf[p]==true)
		return bit[p];
	int a=calculate(p*2+1);
	int b=calculate(p*2+2);
	if(bit[p]==0)
		return a or b;
	return a and b;
}

int changes(int p) {
	if(leaf[p]==1) {
		if(bit[p]!=V)
			return -1;
		return 0;
	}
	int a=calculate(p*2+1);
	int b=calculate(p*2+2);
	int ans=20000;
	int troca=bit[p]==1 and change[p]==1;
	//or
	if(bit[p]==0 or (troca)) {
		int v=a or b;
		if(v==V)
			ans=min(ans,troca);
		if(V==0) {
			int v1=changes(p*2+1);
			int v2=changes(p*2+2);
			if(v1!=-1 and v2!=-1)
				ans=min(ans,v1+v2+troca);
		}
		if(V==1) {
			int v1=changes(p*2+1);
			int v2=changes(p*2+2);
			if(v1==-1 and v2!=-1)
				v1=v2;
			if(v1!=-1 and v2==-1)
				v2=v1;
			if(v1!=-1 and v2!=-1)
				ans=min(ans,min(v1,v2)+troca);
		}

	}
	troca=bit[p]==0 and change[p]==1;
	if(bit[p]==1 or (troca) ) {
		int v=a and b;
		if(v==V)
			ans=min(ans,troca);
		if(V==1) {
			int v1=changes(p*2+1);
			int v2=changes(p*2+2);
			if(v1!=-1 and v2!=-1)
				ans=min(ans,v1+v2+troca);
		}
		if(V==0) {
			int v1=changes(p*2+1);
			int v2=changes(p*2+2);
			if(v1==-1 and v2!=-1)
				v1=v2;
			if(v1!=-1 and v2==-1)
				v2=v1;
			if(v1!=-1 and v2!=-1)
				ans=min(ans,min(v1+troca,v2+troca));
		}
	}
	if(ans==20000)
		return -1;
	return ans;

}
int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
		memset(leaf,0,sizeof(leaf));
		scanf("%d %d",&M,&V);

		int base=(M-1)/2;
		for(int i=0;i<base;i++) {
			scanf("%d %d",&bit[i],&change[i]);
		}
		for(int i=0;i<(M+1)/2;i++) {
			scanf("%d",&bit[i+base]);
			leaf[i+base]=true;
		}
		int ans=changes(0);
		if(ans!=-1)
			printf("Case #%d: %d\n",T,ans);
		else
			printf("Case #%d: IMPOSSIBLE\n",T);
	}

	return 0;
}
