#include<iostream>
#include<cstdio>
#include<cstdlib>
#include<cstring>
#include<algorithm>
using namespace std;

int d[15000], l[15000], k[15000];
inline int MIN(int a, int b){
	return a<b?a:b;
}
int main(){
	int t, time=0, n, D, i, j, now, dis, tmp, tmpdis;
	scanf("%d", &t);
	while(t--){
		scanf("%d", &n);
		for(i=0; i<n; i++){
			scanf("%d%d", &d[i], &l[i]);
			k[i] = 0;
		}
		scanf("%d", &D);

		for(i=0, now=dis=k[0]=d[0]; i<n; i++){
			j=i;
			dis = d[i];
			now = k[i];
			//printf("now dis = %d, now = %d\n", dis, now);
			while(j+1<n&&dis+now>=d[j+1]){
				j++;
				if(k[j]<MIN(d[j]-d[i], l[j])){
					k[j] = MIN(d[j]-d[i], l[j]);
				}
			}
		}
		for(i=0; i<n; i++){
			//printf("now i = %d,  dis = %d, k = %d\n", i, d[i], k[i]);
			if(d[i]+k[i]>=D)
				break;
		}
		if(i==n)
			printf("Case #%d: NO\n", ++time);
		else
			printf("Case #%d: YES\n", ++time);
	}
    return 0;
}
