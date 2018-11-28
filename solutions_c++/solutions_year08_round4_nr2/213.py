#include <cstdio>
#include <cstdlib>
#include <algorithm>

using namespace std;


int n,m,a;
int jmlcase;
int koorx[3],koory[3];
bool selesai;

void rekursif(int jml) {
	if (jml == 2) {
		
		int aa,bb;
		int itung = 0;
		for (aa = 0;aa <= n;aa++) {
		if (selesai) return;
			koorx[2] = aa;
			int itung = (koorx[0] * koory[1]) + (koorx[2] * koory[0]) - (koorx[1] * koory[0]) - (koorx[2] * koory[1]);
			int super = a - itung;
			if (super < 0) continue;
		//	if (koorx[0] - koorx[1] == 0) break;
			if (koorx[1] <= koorx[0]) continue;
			int hehe = koorx[1] - koorx[0];
			if (super % hehe > 0) continue;
			int der = super / hehe;
			if (der > m) continue;
			koory[2] = der;
			
			
		
			for (aa = 0;aa < 3;aa++) {
				printf(" %d %d",koorx[aa],koory[aa]);
				}
			printf("\n");
			selesai = 1;
			}
		return;
		}
	int aa,bb;
	for (aa = 0;aa <= n;aa++) {
		for (bb = 0;bb <= m;bb++) {
			if (selesai) return;
			koorx[jml] = aa;if (selesai) continue;
			koory[jml] = bb;
			rekursif(jml + 1);
			}
		}
	}
	
	

int main() {
	
	int e;
	scanf("%d",&jmlcase);
	for (e = 0;e < jmlcase;e++) {
		scanf("%d%d%d",&n,&m,&a);
		printf("Case #%d:",e + 1);
		selesai = 0;
		rekursif(0);
		if (!selesai) printf(" IMPOSSIBLE\n");
		}
	
		
	
	return 0;
	}

