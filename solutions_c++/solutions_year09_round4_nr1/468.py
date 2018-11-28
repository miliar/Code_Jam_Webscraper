#include<cstdio>
#include<algorithm>
using namespace std;
#define FOR(i,n) for(int i=0;i<(n);++i)
const int MAXN = 50;
char s[MAXN];
int num[MAXN];
int n;
inline int computeNum(){
	int res = 0;
	for(int i=0;s[i];i++)
		if(s[i] == '1') res = i+1;
	return res;
}

void read(){
	scanf("%d",&n);
	FOR(i,n){
		scanf("%s",s);
		num[i] = computeNum();
	}
}

void compute(int cas){
	int res = 0;
	FOR(i,n){
		for(int j=i;j<n;j++)
			if(num[j]<=i+1){
				for(int k=j;k>i;--k){
					swap(num[k],num[k-1]);
					res ++;
				}
				break;
			}
	}
	printf("Case #%d: %d\n",1+cas,res);
}

int main(){
	int t;
	scanf("%d",&t);
	FOR(i,t){
		read();
		compute(i);
	}
	return 0;
}




