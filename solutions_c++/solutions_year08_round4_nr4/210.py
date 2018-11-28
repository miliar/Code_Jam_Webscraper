#include <cstdio>
#include <cstdlib>
#include <algorithm>

#define MAXN 50500

using namespace std;

int perm[6];
char hehe[MAXN];
int n;
int k;
int best;
char duar[MAXN];
int jmlcase;
int a,b,c,d,e,f;

int main() {
	
	scanf("%d",&jmlcase);
	
	for (e = 0;e < jmlcase;e++) {
		printf("Case #%d: ",e + 1);
		scanf("%d\n",&k);
		scanf("%s",hehe);
		
		for (a = 0;a < k;a++) {
			perm[a] = a;
			}
		int answer = 9999999;
		int zzz = strlen(hehe);
		//printf("ini : %d\n",zzz);
		do {
		//printf("ini : %d\n",zzz);
			for (b = 0;b < zzz;) {
				for (a = 0;a < k;a++) {
					for (c = 0;c < k;c++) {
						if (perm[c] == a) duar[a + b] = hehe[c + b];
						}
					}
				b += k;
				}
		/*	for (a = 0;a < zzz;a++) {
				printf("%c",duar[a]);
				}*/
			//printf("\n");
			char lastkar = '8';
			int jml = 0;
			for (b = 0;b < zzz;b++) {
				if (duar[b] == lastkar) continue;
				lastkar = duar[b];
				jml++;
				}
			answer = min(answer,jml);
			} while (next_permutation(perm,perm + k));
		printf("%d\n",answer);
		}
				
			
	
	
	return 0;
	}

