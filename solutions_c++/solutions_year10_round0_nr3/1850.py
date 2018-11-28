#include <cstdio>

int c,r,n,m,s,x,a[1005],S[1005],L[1005];
long long int AC;

int main(){
	scanf("%d",&c);
	for (int tc=1;tc<=c;tc++){
		scanf("%d%d%d",&r,&m,&n);
		for (int i=0;i<n;i++) scanf("%d",&a[i]);

		for (int i=0;i<n;i++){
			x=i;
			s=0;
			while (s+a[x]<=m&&(x!=i||s==0)){
				s+=a[x];
				x++;
				if (x==n) x=0;
			}
			S[i]=s;
			L[i]=x;
		}

		x=AC=0;
		for (int i=0;i<r;i++){
			AC+=S[x];
			x=L[x];
		}
		
		printf("Case #%d: %I64d\n",tc,AC);
	}
	return 0;
}
