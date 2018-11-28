#include<iostream>
#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
#define maxn 2010
#define maxe 1000100
#define INF 0x7fffffff
int a[1010];
int main()
{
	int i,j,p,t,s,n,cnt,tt=0,tk;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d",&t);
	while(t--){
		scanf("%d%d%d",&n,&s,&p);
		for(i=0;i<n;i++)
			scanf("%d",&a[i]);
		sort(a,a+n); cnt=tk=0;
		for(i=0;i<n;i++){
			if(a[i]<2){
				if(a[i]>=p){ cnt++; }
					continue;
			}
			if(tk<s){
				if(a[i]%3==2){
					int k=a[i]/3+2;
					if(k>=p){ cnt++; tk++; }
				}else if(a[i]%3==1){
					int k=a[i]/3+1;
					if(k>=p){ cnt++; tk++; }
				}else{
					int k=a[i]/3+1;
					if(k>=p){ cnt++; tk++; }
				}
			}else{
				if(a[i]%3==2){
					int k=a[i]/3+1;
					if(k>=p){ cnt++; tk++; }
				}else if(a[i]%3==1){
					int k=a[i]/3+1;
					if(k>=p){ cnt++; tk++; }
				}else{
					int k=a[i]/3;
					if(k>=p){ cnt++; tk++; }
				}
			}
		}
		printf("Case #%d: %d\n",++tt,cnt);
	}
	return 0;
}


