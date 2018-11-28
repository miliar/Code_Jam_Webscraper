#include<cstdio>
#include<algorithm>
#include<queue>
using namespace std;

#define oo (1LL<<60)
long long gcd(long long a,long long b){
		long long t;
	if (a>b){
	
		t=a;
		a=b;
		b=t;
	}
	while (a){
		t = b%a;
		b = a;
		a = t;
	}
	return b;
}

priority_queue<pair<long long , long long> > pq;
pair<long long,long long> p1,p2;
int Zz,z;
long long N,L,B[105],list[100005],mn[100005],ans=oo;

int main(){
//	printf("%I64d\n",oo);
	scanf("%d",&Zz);
	for (z=1;z<=Zz;++z){
		ans = oo;
		printf("Case #%d: ",z);
		scanf("%I64d%I64d", &L, &N);
		for (int i=0;i<N;++i){
			scanf("%I64d",&B[i]);
		}
		sort(B,B+N);
		long long G=B[0];
		for (int i=1;i<N;++i) G=gcd(G,B[i]);
		
		if (L%G!=0){
			puts("IMPOSSIBLE");
			continue;
		}
		
		if (L%B[N-1]==0) ans=L/B[N-1];
		
		while (pq.size()) pq.pop();
		
		for (int j=0;j<=100000;++j){
			list[j] = mn[j] = (oo);
		}
		mn[0] = list[0] = 0;
		pq.push(make_pair(0,0));
		
		while (pq.size()){
			p1 = pq.top();
			pq.pop();
			long long used = -p1.first;
			long long least = -p1.second;
//			printf("%I64d %I64d\n",used,least);
			for (int i=0;i<N-1;++i){
				long long u2 = used+1;
				long long l2 = least + B[i];
				long long tmp = l2%B[N-1];
				if (l2>L) continue;
				
				if (tmp==L%B[N-1]){
					if (u2+(L-l2)/B[N-1]<ans) ans=u2+(L-l2)/B[N-1];
					continue;
				}
				
				if (l2>=list[tmp] && u2>=mn[tmp]) continue;
				
				
				if ((L-l2)/B[N-1]+u2-3 >= ans) continue;
				
				mn[tmp] = u2; 
				list[tmp] = l2;
				
				pq.push(make_pair(-u2,-l2));
			}
		}
		
		
		if (ans!=oo) printf("%I64d\n",ans);
		else printf("IMPOSSIBLE\n");
	}	
	return 0;
}
