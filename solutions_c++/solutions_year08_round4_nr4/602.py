#include<iostream>
#include<algorithm>
#include<cmath>
#include<cassert>
using namespace std;

int p[8],n;

char str[1024],bak[1024];
int ll(int len){
	int cnt=0;
	for(int i=0;i<len;i++){
		cnt++;
		while(bak[i+1]==bak[i]) i++;
	}
	return cnt;
}
#define INF 65536
int main()
{	
#ifndef ONLINE_JUDGE
	freopen("D-small-attempt0.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
#endif
	int cas;
	scanf("%d",&cas);
	for(int ii=1;ii<=cas;ii++){
		printf("Case #%d: ",ii);
		scanf("%d %s",&n,str);
		int i;
		for(i=0;i<n;i++) p[i]=i;
		int re=INF;
		do{
			int len=strlen(str);
			for(i=0;i<len;i+=n){
				for(int j=0;j<n;j++){
					bak[i+j]=str[i+p[j]];
				}
			}
			bak[len]=0;
			int tmp=ll(len);
			if(tmp<re) re=tmp;
		}while(next_permutation(p,p+n));
		printf("%d\n",re);
	}
	return 0;
}