#include<cstdio>
#include<algorithm>
using namespace std;

int Z,z,i,j,a[45],N,cnt;
char c[45];

void whh(int k){
	//printf("k = %d\n",k);
	if (a[k+1]>i)
		whh(k+1);
	
	swap(a[k],a[k+1]);
	++cnt;
}

int main(){
	scanf("%d",&Z);
	for (z=1;z<=Z;++z){
		cnt = 0;
		scanf("%d",&N);
		gets(c);
		for (i=1;i<=N;++i){
			gets(c);
			a[i] = 0;
			for (j=0;j<N;++j){
				if (c[j]=='1') a[i] = j+1;
			}
		}
		
		for (i=1;i<=N;++i){
			if (a[i]>i){
				whh(i);
			}
		}
		printf("Case #%d: %d\n",z,cnt);
	}

	return 0;
}
