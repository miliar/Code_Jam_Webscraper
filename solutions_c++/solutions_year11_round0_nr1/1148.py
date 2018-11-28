#include <stdio.h>
#include <math.h>
#define MAXN 200

int oper_B[MAXN], oper_O[MAXN];
int now_B, now_O, sum_B, sum_O, step, ans, done_B, done_O;
char oper[MAXN][2];
int n;

int main(){
	FILE *fp1, *fp2;
	int t, CASE, i, data;
	fp1 = fopen("A-large.in", "r");
	fp2 = fopen("output.out", "a");
	fscanf(fp1, "%d", &CASE);
	for(t = 1; t <= CASE; t ++){
		fscanf(fp1, "%d\n", &n);
		sum_B = sum_O = 0;
		for(i = 0; i < n; i ++){
			fscanf(fp1, "%1s %d", oper[i], &data);
			if(oper[i][0] == 'B') oper_B[sum_B ++] = data;
			else oper_O[sum_O ++] = data;
		}
		now_B = now_O = 1;
		done_B = done_O = 0;
		ans = 0;
		for(i = 0; i < n; i ++){
			if(oper[i][0] == 'B'){
				step = abs(now_B - oper_B[done_B]);
				now_B = oper_B[done_B ++];
				ans += step + 1;
				if(abs(now_O - oper_O[done_O]) <= step + 1) now_O = oper_O[done_O];
				else now_O = now_O < oper_O[done_O] ? (now_O + step + 1) : (now_O - step - 1);
			}
			else{
				step = abs(now_O - oper_O[done_O]);
				now_O = oper_O[done_O ++];
				ans += step + 1;
				if(abs(now_B - oper_B[done_B]) <= step + 1) now_B = oper_B[done_B];
				else now_B = now_B < oper_B[done_B] ? (now_B + step + 1) : (now_B - step - 1);
			}
		}
		fprintf(fp2, "Case #%d: %d\n",t, ans);
	}
	fclose(fp1);
	fclose(fp2);
	return 0;
}