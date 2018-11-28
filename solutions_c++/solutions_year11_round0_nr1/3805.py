

#include <cstdio>
#include <algorithm>
using namespace std;

#define ABS(x) ((x)>0?(x):-(x))

const int MAXN = 110;
int B[MAXN];
bool R[MAXN];

int solve(void)
{
	int i, n, r, t0, t1, s0, s1;
	char ch;

	scanf("%d", &n);

	for(i=0; i<n; i++){
		getchar();
		ch = getchar();
		if(ch=='O') R[i] = false;
		else R[i] = true;
		scanf("%d", &B[i]);
	}
	
	t0 = t1 = 0;
	s0 = s1 = 1;
	for(i=0; i<n; i++){
		if(!R[i]){
			t0 += ABS(B[i]-s0)+1;
			s0 = B[i];
			if( t0 <= t1 ) t0 = t1+1;
		}
		else {
			t1 += ABS(B[i]-s1)+1;
			s1 = B[i];
			if( t1 <= t0 ) t1 = t0+1;
		}
	}

	if(t1>t0) return t1;
	return t0;
}

int main()
{

	freopen("A-large.in","r", stdin);
	freopen("A-large.out", "w", stdout);

	int t, i;
	scanf("%d", &t);
	
	for(i=1; i<=t; i++){
		printf("Case #%d: %d\n", i, solve());
	}

	return 0;
}