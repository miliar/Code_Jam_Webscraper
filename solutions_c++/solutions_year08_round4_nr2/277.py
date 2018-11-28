#include <cstdio>

FILE *in, *out;

int main(){
	in = fopen("B.in", "r");
	out = fopen("B.out", "w");
	int n;
	fscanf(in, "%d", &n);
	for(int t=1;t<=n;t++){
		int N, M, A;
		fscanf(in, "%d %d %d", &N, &M, &A);
		int i, j, k, l;
		bool find=false;
		for(i=0;i<=N && !find;i++)
			for(j=0;j<=M && !find;j++)
				for(k=0;k<=N && !find;k++)
					for(l=0;l<=M && !find;l++)
						if(i*l - j*k == A)
							find=true;
		if(find)
			fprintf(out, "Case #%d: %d %d %d %d %d %d\n", t, 0, 0, i-1, j-1, k-1, l-1);
		else
			fprintf(out, "Case #%d: IMPOSSIBLE\n", t);
	}
	fclose(in);
	fclose(out);
	return 0;
}
