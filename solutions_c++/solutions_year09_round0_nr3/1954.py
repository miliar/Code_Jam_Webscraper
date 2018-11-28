#include <stdlib.h>
#include <stdio.h>
#include <string.h>

#define MAX_LEN 510

int N;

char needle[]="welcome to code jam";
char hay[MAX_LEN];
int  hay_ptr[MAX_LEN][sizeof(needle)];

int i,hay_len,needle_len=sizeof(needle)-1;

long int cnt;


void search_text(int needle_pos, int hay_pos) {

	if (needle_pos == needle_len) {
		cnt++;
		return;
	}

	while (hay_pos < hay_len) {
		search_text(needle_pos+1, hay_ptr[hay_pos][needle_pos+1]);
		hay_pos=hay_ptr[hay_pos][needle_pos];
	}
}

void search_needle() {
	char* c;
	
	c=strchr(hay,needle[0]);
	if(c) search_text(0,c-hay);
}

int read_hay() {

	bool valid=false;
	int len=0;
	char c;

	while (true) {
		scanf("%c", &c);
		if ((c=='\r') || (c=='\n')) {
			if (valid) return len;
		} else {
			valid=true;
			hay[len++]=c;
		}
	}
}

void get_hay() {
	int i;
	char *c, *n;

	hay_len=read_hay();
	memset(hay_ptr, 0, sizeof(hay_ptr));
	for (i=0; i<needle_len; i++) {
		c=strchr(hay, needle[i]);
		while(c) {
			n=strchr(c+1, needle[i+1]);
			hay_ptr[c-hay][i+1]=n?n-hay:hay_len;
			n=strchr(c+1, needle[i]);
			hay_ptr[c-hay][i]=n?n-hay:hay_len;
			c=n;
		};
	}
}

int main() {
	scanf("%d", &N);


	for (i=1; i<=N; i++) {
		cnt=0;
		get_hay();
		search_needle();

		printf("Case #%d: %04ld\n", i, cnt);
	
	}

}
