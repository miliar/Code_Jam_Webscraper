#include <stdio.h>
#include <stdlib.h>
#include <string>

char S[70]={0};
__int64 process(void)
{
	int N;
	int i;
	int dig=0;
	int mat[40]={0};
	N = strlen(S);
	if (S[N-1] == '\n') --N;
	for (i=0;i<40;++i) mat[i] = -1;

	i=0;
	if ('a'<=S[i] && S[i]<='z'){
		mat[S[i]-'a'+10] = 1;
	}else{
		mat[S[i]-'0'] = 1;
	}

	for (i=1;i<N;++i){
		if ('a'<=S[i] && S[i]<='z'){
			if (mat[S[i]-'a'+10] == -1) mat[S[i]-'a'+10] = dig++;
		}else{
			if (mat[S[i]-'0'] == -1) mat[S[i]-'0'] = dig++;
		}
		if (dig == 1) ++dig;
	}

	if (dig < 2) dig = 2;
	__int64 ret=0;
	__int64 d=1;
	for (i=N-1;i>=0;--i,d=d*dig){
		if ('a'<=S[i] && S[i]<='z'){
			ret = ret + mat[S[i]-'a'+10]*d;
		}else{
			ret = ret + mat[S[i]-'0']*d;
		}
	}
	return ret;
}
int main(void)
{
	FILE *fin = fopen("input.txt", "r");
	FILE *fout = fopen("output.txt", "w");

	int test_case, T;
	fscanf(fin, "%d", &T);
	fgets(S,70,fin);
	for (test_case=1;test_case<=T;++test_case){
		fgets(S,70,fin);
		fprintf(fout, "Case #%d: %I64d\n", test_case, process());
	}

	fclose(fout);
	fclose(fin);
	return 0;
}