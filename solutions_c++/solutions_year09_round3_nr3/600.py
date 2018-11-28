#include <iostream>
#include <algorithm>
#define REP(i,n) for(int i=0;i<n;i++)
#define FOR(i,f,t) for(int i=f;i<=t;i++)
using namespace std;
int n,p,q;
int w[110];
bool t[10010];
int res;
int mini;

int main(){	
	scanf("%d",&n);
	REP(z,n){
		scanf("%d %d",&p,&q);
		REP(i,q) scanf("%d",&w[i]);
		mini=1000000000;
		do{
		//printf("hopsa\n");
		res=0;
		FOR(i,1,p) t[i]=1;
		for(int i=q-1;i>=0;i--){
			t[w[i]]=0;
			int k=w[i]+1;
			while(k<=p){
				if(t[k]) res++;
				else break;
				k++;
			}
			k=w[i]-1;
			while(k>=1){
				if(t[k]) res++;
				else break;
				k--;
			}
		}
		if(mini>res) mini=res;
		}while(next_permutation(w,w+q));
		printf("Case #%d: %d\n",z+1,mini);
	}
	return 0;
}

