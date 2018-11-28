#include<cstdio>
int N, T, L, H;
int l[10001];
int main(){
	scanf("%d", &T);
	for (int iT = 1; iT <= T; iT++){
		scanf("%d%d%d", &N, &L, &H);
		for (int i=0; i<N; i++){
			scanf("%d", l+i);
		}
		int k, i;
		for (k=L; k<=H; k++){
			for (i=0; i<N; i++)
				if (k%l[i]==0 || l[i]%k==0)
					;
				else
					break;
			if (i==N)
				break;
		}
		printf("Case #%d: ", iT);
		if (k<=H)
			printf("%d\n", k);
		else
			puts("NO");	
	}
	return 0;
}
