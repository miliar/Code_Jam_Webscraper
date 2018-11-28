#include<cstdio>
#include<algorithm>
using namespace std;

int Z,N,a[10005],b[10005],ok[10005];

int main(){
	scanf("%d",&Z);
	for (int z=1;z<=Z;++z){
		scanf("%d",&N);
		for (int i=1;i<=10000;++i) a[i] = 0;
		for (int i = 0;i<N;++i){
			int k;
			scanf("%d",&k);
			a[k]++;
		}
		
		
		int l = 0;
		int u = N;
		int m;
		
		while (l<u){
			
		//	printf("%d %d \n",l,u);
			
			m = (l+u+1)/2;
			bool OK = true;
			
			for (int i=1;i<=10000;++i){
				b[i] = a[i];
				ok[i] = 0;
			}
			ok[0] = 0;
			
			for (int i=1;i<=10000 && OK;++i){
				if (b[i]){
					int cnt = min(b[i],ok[i-1]);
					b[i] -= cnt;
					ok[i] += cnt;
				}
				int t = b[i];
				for (int j=0;t && OK && j<m;++j){
					
					if (i+j>10000) OK = false;
					b[i+j] -= t;
					if (b[i+j]<0) OK = false;
				}
				
				if (OK){
					ok[i+m-1] = t;
				}
				

				
			}
			
			if (OK){
				l = m;
			}else{
				u = m-1;
			}
			
		}
		
		printf("Case #%d: %d\n",z,l);
	}
	
	
	return 0;
}
