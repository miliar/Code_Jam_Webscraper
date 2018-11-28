#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;
int TT;
int k;
char str[50001];
char aux[50001];
int perm[16];

int main(void) {
	scanf("%d",&TT);
	for(int T=1;T<=TT;T++) {
        printf("Case #%d: ", T);
		scanf("%d %s",&k,str);
		int tam=strlen(str);
		for(int i=0;i<k;i++)
			perm[i]=i;
		int ans=500000;

		do {
            for(int i=0;i<tam;i+=k) {
				//permute
                for(int j=0;j<k;j++) {
                    aux[i+j] = str[i+perm[j]];
                }
            }
			int tmp=1;
			for(int i=1;i<tam;i++)
				if(aux[i]!=aux[i-1])
					tmp++;

            ans = min(ans, tmp);
        } while(next_permutation(perm, perm+k));

        printf("%d\n", ans);

	}

	return 0;
}
