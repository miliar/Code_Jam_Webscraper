#include <stdio.h>
#include <string.h>

#define		MAXL	17
#define		MAXD	5005

char dict[MAXD][MAXL+1];
char word[MAXL][26+1];

int main()
{
	FILE *fo;
	
	int L, D, N;
	scanf("%d %d %d", &L, &D, &N);
	int i = 0;
	while(i < D) {		
		scanf("%s", dict[i]);
		++i;
	}
	i = 1;
	char temp[MAXL*28+1];
	fo = fopen("output","w");
	while(i <= N) {
		scanf("%s", temp);
		memset(word, 0, MAXL*(26+1));
		void prev_proc(char *);
		prev_proc(temp);
		int cal(int , int );

		int res = cal(L, D);
		fprintf(fo,"Case #%d: %d\n", i,res);
		++i;
	}
	return 0;
}

void prev_proc(char *str) 
{
	static int i = 0;
	if (*str == 0) {
		i = 0;
		return;
	}
	
	if (*str != '(')
		word[i][0]=*str;
	else { // (
		int j = 0;
		str++;
		while(*str!=')') 
			word[i][j++] = *str++;
	}
	str++;
	i++;
	prev_proc(str);
}
int cal(int L, int D) {
	int res = 0;
	int i, j;
	for (i=0;i<D;++i) {
		bool f = true;
		for (j=0;j<L;++j) {
			if (strchr(word[j], dict[i][j])==0) {
				f = false;
				break;
			}
		}
		if (f)
			++res;
	}
	return res;
}