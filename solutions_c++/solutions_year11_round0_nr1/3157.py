#include <cstdio>
int n;
struct command {
	int w;
	int order;
};
command real[110];
int nb,no;
int abs(int x) {
	return x<0?-x:x;
}
int main() {
	freopen("input.txt","rt",stdin);
	freopen("output.txt","wt",stdout);
	int Ti,T;
	scanf("%d",&T);
	for(Ti=0;Ti<T;Ti++) {
		scanf("%d ",&n);
		int i,dv;
		char tp;
		for(i=0;i<n;i++) {
			scanf("%c %d ",&tp,&dv);
			if(tp=='O') {
				real[i].order=0;
				real[i].w=dv;
			}
			else {
				real[i].order=1;
				real[i].w=dv;
			}
		}
		int ans=0;
		int bw=1,ow=1,lastgap=0,lastturn=-1;
		for(i=0;i<n;i++) {
			if(real[i].order==0) {
				ans+=abs(ow-real[i].w);
				if(lastturn==real[i].order) {
					lastgap+=abs(ow-real[i].w)+1;
				} else {
					lastturn=real[i].order;
					if(lastgap>abs(ow-real[i].w)) {
						ans-=abs(ow-real[i].w);
						lastgap=1;
					} else {
						ans-=lastgap;
						lastgap=abs(ow-real[i].w)+1-lastgap;
					}
				}
				ans++;
				ow=real[i].w;
			} else {
				ans+=abs(bw-real[i].w);
				if(lastturn==real[i].order) {
					lastgap+=abs(bw-real[i].w)+1;
				} else {
					lastturn=real[i].order;
					if(lastgap>abs(bw-real[i].w)) {
						ans-=abs(bw-real[i].w);
						lastgap=1;
					} else {
						ans-=lastgap;
						lastgap=abs(bw-real[i].w)+1-lastgap;
					}
				}
				ans++;
				bw=real[i].w;
			}
		}
		printf("Case #%d: %d\n",Ti+1,ans);
	}
	return 0;
}