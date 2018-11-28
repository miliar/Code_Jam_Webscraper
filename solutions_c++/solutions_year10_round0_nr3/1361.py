#include <stdio.h>
#include <string.h>
#include <set>
using std::set;

int R,K,N;
int G[1010];
long long sum;
struct node {
	int a,b,sum;
	
	bool operator < (const node &t)const {
		return a < t.a || ( a == t.a && b < t.b);
	}
		
}pp[1000010];

int main() {
	int t,c=0;
	
	scanf("%d",&t);
	while(t--) {
		sum = 0;
		scanf("%d%d%d",&R,&K,&N);
		for(int i=0;i<N;i++)
			scanf("%d",G+i);
		set< node > Q;
		set< node >::iterator it;
		it = NULL;
		
		int first,last;
		int i=0,j=0,pre=0;
		long long temp=0;
		long long total = 0;
		for(int i=0;i<N;i++)
			total += G[i];
		//printf("%lld\n",total);
		//puts("AFDSA");
		if(total > K) {
			while(1) {
				if(temp+G[j] > K) {
					int tp = (j+N-1)%N;
					//printf("%d %d %d\n",pre,tp,temp);
					//scanf("%*d");
					it = Q.find((node){pre,tp,temp});
					//puts("AFSDASDF");
					if(it != Q.end()) {
						//first = it->c;
						for(int k=0;k<i;k++)
							if(pp[k].a == pre && pp[k].b == tp) {
								first = k;
								break;
							}
						last = i;
						break;
					}
					// puts("AFDS");
					Q.insert((node){pre,tp,temp});
					pp[i] = (node){pre,tp,temp};
					pre = j;
					temp = 0;
					++i;
				}
				temp += G[j];
				j = (j+1)%N;
			}
			//printf("first = %d, last = %d\n",first,last);
			if(last >= R) {
				//puts("ASFDAS");
				for(i=0;i<R;i++)
					sum += pp[i].sum;
			} else {
				int num = last-first;
				long long ttotal = 0;
				for(i=0;i<first;i++)
					sum += pp[i].sum;
				
				for(i=first;i<last;i++)
					ttotal += pp[i].sum;
				
				//printf("%lld %lld\n",sum,total);
				int count = (R-first)%num;
				long long tt = (R-first)/num;
				//printf("%
				sum += ttotal*tt;
				for(i=first;i<last && count > 0;i++,--count)
					sum += pp[i].sum;
			}
		} else {
			sum = total*R;
		}	
		
		printf("Case #%d: %lld\n",++c,sum);
	}
	
	return 0;
}
