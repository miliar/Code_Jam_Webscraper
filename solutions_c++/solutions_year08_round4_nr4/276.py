#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

FILE *in, *out;
int fact[6] = {1, 1, 2, 6, 24, 120};

int main(){
	in = fopen("D.in", "r");
	out = fopen("D.out", "w");
	int n;
	fscanf(in, "%d", &n);
	for(int t=1;t<=n;t++){
		int i, j, k;
		char str[1002];
		char newstr[1002];
		int perm[6];
		int len;
		int result = 0x7fffffff;

		fscanf(in, "%d %s ", &k, str);
		len = strlen(str);

		for(i=0;i<k;i++)
			perm[i]=i;
		for(i=0;i<fact[k];i++){
			for(j=0;j<len/k;j++)
				for(int x=0;x<k;x++)
					newstr[j*k+perm[x]] = str[j*k+x];

			int tot=1;
			char prev=newstr[0];
			for(j=1;j<len;j++)
				if(prev != newstr[j]){
					prev = newstr[j];
					tot++;
				}
			if(result > tot)
				result = tot;
			if(i != fact[k]-1)
				next_permutation(perm, perm+k);
		}
		fprintf(out, "Case #%d: %d\n", t, result);
	}
	fclose(in);
	fclose(out);
	return 0;
}
