#include<stdio.h>
#include<cmath>

FILE *in, *out;
int n;
int numbers[3];
int diffs[2];

int gcd(int a, int b){
	if(a < b)
		return gcd(b, a);
	else if(b == 0)
		return a;
	if(!(a % b))
		return b;
	return gcd(b, a % b);
}
int main(){
	in = fopen("input.txt", "r");
	out = fopen("output.txt", "w");

	int casecnt, curcasecnt;
	fscanf(in, "%d", &casecnt);
	curcasecnt = casecnt;
	int i;

	while(curcasecnt--){
		fscanf(in, "%d", &n);
		for(i = 0; i < n; i++)
			fscanf(in, "%d", &numbers[i]);
		for(i = 0; i < n - 1; i++)
			diffs[i] = abs(numbers[i] - numbers[i + 1]);

		int t = diffs[0];
		if(n == 3){
			t = gcd(diffs[0], diffs[1]);
		}
		
		int val = -numbers[0];
		while(val < 0)
			val += t;
		fprintf(out, "Case #%d: %d\n", casecnt - curcasecnt, val);
	}

	return 0;
}