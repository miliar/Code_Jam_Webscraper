#include <cstdio>
#include <cstring>

int g[2010], nxt[2010], val[2010], vst[2010];
long long rec[2010];
int rear, sum;
int t,r,k,n,c,st;

int main(){
	scanf("%d", &t);
	for(int cnt=1; cnt<=t; cnt++){
		memset(vst,0,sizeof(vst));
		scanf("%d%d%d", &r, &k, &n);
		for(int i=0; i<n; i++){
			scanf("%d", &g[i]);
			g[i+n]= g[i];
		}
		sum=rear=0;
		for(int i=0; i<n; i++){
			while(rear-i<n && sum+g[rear]<=k)
				sum+= g[rear++];
			nxt[i]= rear%n;
			val[i]= sum;
	//		printf("%d: %d %d\n", i, nxt[i], val[i]);
			sum-= g[i];
		}
		for(c=1,rec[0]=st=0; !vst[st]; st=nxt[st],c++){
			vst[st]= c;
			rec[c]= rec[c-1]+val[st];
	//		printf("%d: %d  %d\n", c, st, rec[c]);
		}
		st=vst[st];
	//	printf("cycle %d to %d\n", st, c);
		if(st>r){printf("Case #%d: %lld\n", cnt, rec[r]);}
		else{
			r-= st;
			printf("Case #%d: %lld\n", cnt, (long long)(rec[c-1]-rec[st-1])*(r/(c-st)) + rec[st+r%(c-st)]);
		}
	}
}
