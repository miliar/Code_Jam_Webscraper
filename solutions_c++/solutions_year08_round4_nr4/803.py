#include <stdio.h>

int Perm[5];
int N, K;
char Str[1001];
char Str2[1001];

template<class T>
void swap(T&a, T&b) { T c=a;a=b;b=c; }

int Size;

void ApplyPerm() {
	for(int i=0; Str[i]; ++i)
		Str2[i/K*K+Perm[i%K]] = Str[i];
	int size = 0;
	for(int i=0; Str[i]; ++i)
		if( i==0 || Str2[i-1]!=Str2[i] )
			++size;
	if( size<Size )
		Size = size;
}

void DoPerm(int d) {
	if( d==K ) {
		ApplyPerm();
		return;
	}
	for(int i=d; i<K; ++i) {
		swap(Perm[i], Perm[d]);
		DoPerm(d+1);
		swap(Perm[i], Perm[d]);
	}
}

int main() {
	scanf("%d", &N);
	for(int n=1; n<=N; ++n) {
		scanf("%d%s", &K, Str);
		for(int i=0; i<K; ++i)
			Perm[i] = i;
		Size = 1000000000;
		DoPerm(0);
		printf("Case #%d: %d\n", n, Size);
	}
	return 0;
}
