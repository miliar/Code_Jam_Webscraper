#include <cstdio>
#include <cstring>
using namespace std;

int d[10010],l[10010],len[10010];
int T,n,target;

int main(){
	scanf("%d",&T);
	for (int cases=0;cases<T;++cases){
		scanf("%d",&n);
		for (int i=0;i<n;++i) scanf("%d%d",&d[i],&l[i]);
		memset(len,0,sizeof(len));
		len[0]=d[0];
		scanf("%d",&target);
		int head=0;
		int tail=0;
		int max=0;
		while (head<=tail){
			for (int i=tail+1;i<n;++i){
				if (len[head]+d[head]>=d[i]){
					len[i]=d[i]-d[head];
					if (l[i]<len[i]) len[i]=l[i];
					tail++;
				}
				else break;
			}
			if (len[head]+d[head]>max) max=len[head]+d[head];
			++head;
		}
		if (max>=target) printf("Case #%d: YES\n",cases+1);
		else printf("Case #%d: NO\n",cases+1);
	}
	return 0;
}
