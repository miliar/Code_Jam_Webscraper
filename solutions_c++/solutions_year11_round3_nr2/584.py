#include<cstdio>
#include<cstring>
int L, t, N, C, T;
int a[1001];
long ansL[1001][3];
long getAns(int n, int l){
	if (n==0)
		return 0;
	if (ansL[n][l]>0)
		return ansL[n][l];
	long r = a[(n-1)%C];
	long t1 = getAns(n-1, l) + r * 2;
	long tt = t1;
	if (l>0){
		long t2 = getAns(n-1, l-1); 
		if (t2>=t)
			t2 += r;
		else {
			if ( t-t2 > r * 2)
				t2 = t;
			else{
				t2 = t + (r - (t-t2)/2);
			}
		}
		if (t2<tt)
			tt = t2;
	}
	ansL[n][l] = tt;
	return tt;
}
int main(){
	scanf("%d", &T);
	for (int iT = 1; iT <= T; iT++){
		scanf("%d%d%d%d", &L, &t, &N, &C);
		for (int i=0; i<C; i++){
			scanf("%d", a+i);
		}
		memset(ansL, 0, sizeof(ansL));
		printf("Case #%d: %d\n", iT, getAns(N, L));
	}
	return 0;
}
