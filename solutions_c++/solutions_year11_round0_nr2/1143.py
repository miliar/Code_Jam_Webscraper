#include <stdio.h>
#include <string.h>

#define MAXN 200

int combine[250][250];
int opposed[250][250];
char oper[MAXN];
char ans[MAXN];
int ans_len;
char str[10];
int n, m;

int main(){
	FILE *fpin, *fpout;
	int CASE, t, i, j, falg;
	char ch;
	fpin = fopen("B.in", "r");
	fpout = fopen("B.out", "a");
	fscanf(fpin, "%d", &CASE);
	for(t = 1; t <= CASE; t ++){
		memset(combine, -1, sizeof(combine));
		memset(opposed, 0, sizeof(opposed));
		fscanf(fpin, "%d", &m);
		for(i = 0; i < m; i ++){
			fscanf(fpin, "%s", str);
			combine[str[0]][str[1]] = str[2];
			combine[str[1]][str[0]] = str[2];
		}
		fscanf(fpin, "%d", &m);
		for(i = 0; i < m; i ++){
			fscanf(fpin, "%s", str);
			opposed[str[0]][str[1]] = 1;
			opposed[str[1]][str[0]] = 1;
		}
		fscanf(fpin, "%d", &n);
		fscanf(fpin, "%s", oper);
		ans_len = 1;
		ans[1] = 0;
		for(i = 0; i < n; i ++){
			if(combine[ans[ans_len - 1]][oper[i]] != -1){
				ch = combine[ans[ans_len - 1]][oper[i]];
				ans_len -= 1;
			}
			else ch = oper[i];
			falg = 0;
			for(j = 1; j < ans_len; j ++)
				if(opposed[ch][ans[j]]){
					falg = 1;
					break;
				}
			if(falg) ans_len = 1;
			else ans[ans_len ++] = ch;
		}
		fprintf(fpout, "Case #%d: [", t);
		for(i = 1; i < ans_len - 1; i ++)
			fprintf(fpout, "%c, ", ans[i]);
		if(ans_len > 1)
			fprintf(fpout, "%c]\n", ans[ans_len-1]);
		else fprintf(fpout, "]\n");
	}
	fclose(fpin);
	fclose(fpout);
	return 0;
}


