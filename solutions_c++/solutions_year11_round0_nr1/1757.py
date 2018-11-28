#include<iostream>
#include<cstring>
#include<stdlib.h>
#include<algorithm>

using namespace std;

#define MAX 105

int abs(int a){
	if (a < 0)	return -a;
	else	return a;
}
int main(void){
	int cas, n, goal, oc, bc, occ, bcc, onext, bnext;
	int pos, ori[MAX], blu[MAX];
	char temp[15];
	bool kind[MAX];
	freopen("A.in", "r", stdin);
	freopen("test.out", "w", stdout);
	scanf("%d", &cas);
	for (int t = 1; t <= cas; t++){
		goal = 0;
		scanf("%d", &n);
		ori[0] = 1, blu[0] = 1;
		oc = 0, bc = 0;
		for (int i = 0; i < n; i++){
			scanf("%s%d", &temp, &pos);
			if (temp[0] == 'O')	kind[i] = false, ori[++oc] = pos;
			else	kind[i] = true, blu[++bc] = pos;
		}
		ori[++oc] = ori[oc-1];
		blu[++bc] = blu[bc-1];
		occ = 0, bcc = 0;
		onext = ori[occ+1] - ori[occ];
		bnext = blu[bcc+1] - blu[bcc];
		for (int i = 0; i < n; i++){
			if (kind[i] == 0){
				goal += onext;
				bnext = max(bnext-onext-1, 0);
				occ++;
				onext = abs(ori[occ+1] - ori[occ]);
			}
			else{
				goal += bnext;
				onext = max(onext-bnext-1, 0);
				bcc++;
				bnext = abs(blu[bcc+1] - blu[bcc]);
			}
			goal++;
		}
		printf("Case #%d: %d\n", t, goal);
	}
	return 0;
}