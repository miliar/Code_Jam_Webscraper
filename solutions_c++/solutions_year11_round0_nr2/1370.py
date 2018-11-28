#include <stdlib.h>
#include <stdio.h>
#include <string.h>


int solve(int ctry){
	char comp_LUT[256][256], oposed_LUT[256][256];
	memset(comp_LUT, 0, sizeof(comp_LUT));
	memset(oposed_LUT, 0, sizeof(oposed_LUT));
	int ccnt, ocnt, len;
	scanf("%d ", &ccnt);
	for (int i = 0; i < ccnt; i++){
		char c1, c2, out;
		scanf("%c%c%c ", &c1, &c2, &out);
		comp_LUT[c1][c2] = out;
		comp_LUT[c2][c1] = out;
	};
	scanf("%d ", &ocnt);
	for (int i = 0; i < ocnt; i++){
		char c1, c2;
		scanf("%c%c ", &c1, &c2);
		oposed_LUT[c1][c2] = -1;
		oposed_LUT[c2][c1] = -1;
	};
	char rez[101];
	memset(rez, 0, sizeof(rez));
	scanf("%d ", &len);
	int pos = 0;
	for (int i = 0; i < len; i++){
		scanf("%c", rez+pos);
		if (!pos){
			pos++;
			continue;
		};
		char comb = comp_LUT[rez[pos]][rez[pos-1]];
		if (comb > 0){
			rez[pos-1] = comb;
			continue;
		};
		int j;
		for (j = 0; j < pos; j++)
			if (oposed_LUT[rez[pos]][rez[j]] == -1)
				break;
		if (j == pos)
			pos++;
		else 
			pos = 0;
	};
	rez[pos] = 0;
	
	printf("Case #%d: [", ctry);	
	for (int i = 0; i < pos-1; i++)
		printf("%c, ", rez[i]);
	if (pos)
		printf("%c", rez[pos-1]);
	printf("]\n");
};


int main(){

	if (freopen("test.in", "rt", stdin)){
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("B-small-attempt0.in", "rt", stdin)){
		freopen("B-small-attempt0.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	if (freopen("B-large.in", "rt", stdin)){
		freopen("B-large.out", "wt", stdout);
		int tries = 0;
		scanf("%d", &tries);
		for (int ctry = 1; ctry <= tries; ctry++){
			solve(ctry);
		};
	};
	return 0;
};

