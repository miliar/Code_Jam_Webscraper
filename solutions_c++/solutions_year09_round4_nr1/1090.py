#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<math.h>

const int N = 50;
int mat[N];

int solve(int n)
{
	int i, j, k, c, res=0;
	char str[N];
	memset(mat, 0, sizeof(mat));
	for(i=0; i<n; i++){
		scanf("%s", str);	
		for(j=n-1; j>=0; j--)
			if(str[j]=='1') break;
		if(j<0) j++;
		mat[i] = j;
	}
	
	for(i=0; i<n; i++){
		if(mat[i]<=i) continue;
		for(j=i+1; j<n; j++)
			if(mat[j]<=i) break;
		c = mat[j];
		for(k=j-1; k>=i; k--)
			mat[k+1] = mat[k];
		mat[i] = c;
		res+=j-i;
	}
	return res;
}

int main()
{
	int test, ca=0, n;
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);

	scanf("%d", &test);
	while(test--){
		ca++;
		scanf("%d", &n);
		printf("Case #%d: %d\n", ca, solve(n));
	}
	return 0;
}

