#include <stdio.h>
#include <memory.h>
#include <string.h>
#include <stdlib.h>

struct NODE
{
	bool ch[15][26];
}word[1000];

char buffer[10000];
char* buf;
char* token;
int item;
int number;

short flag[1000000];

bool isok(int num,int base) {
	memset(flag,0,sizeof(flag));
	int path_top = 0;
	int path[100];
	int fif = 0;

	while (1) {
		int m = num;
		int tt[100];
		int tt_top = 0;
		while (m) {
			tt[tt_top ++] = m % base;
			m /= base;
		}
		int mm = 0;
		for (int i = 0; i < tt_top; i ++) {
			mm += tt[i] * tt[i];
		}
		num = mm;
	/*	path[path_top ++] = mm;
		if (flag[mm] == 0) flag[mm] = 2;
		else if (flag[mm] == 2) { fif = 2; break; }
		else if (flag[mm] == 1) 
		flag[mm] = true;*/
		if (flag[mm]) return false;
		flag[mm] = true;
		if (mm == 1) return true;
	}





}

int main()
{
	freopen("A-small-attempt0.in","r",stdin);
	freopen("out.txt","w",stdout);
	int base[100];
	int base_top;
	int Case = 1;
	int i;
	int T;
	scanf("%d ",&T);
	for (Case = 1; Case <= T; Case ++) {
		gets(buffer);
		buf = buffer;
		base_top = 0;
		while ((token=strtok(buf," ")) != NULL) {
			item = atoi(token);
			base[base_top ++] = item;
			buf = NULL;
		}
		for (number = 2; ; number ++) {
			for (i = 0; i < base_top; i ++) {
				if (base[i] == 2 || base[i] == 4) continue;
				if (isok(number,base[i])) continue;
				else break;
			}
			if (i< base_top) continue;
			else break;
		//	printf("number : %d\n",number);
		}
		printf("Case #%d: %d\n",Case,number);

		
	}
	return 0;
}
