#include <stdio.h>
#include <string.h>
using namespace std;

int n,s,q,res;

char aaa[100][110], qs[110];
bool bbb[100];
int current;

void init() {
	for (int i=0;i<s;i++) {
		bbb[i] = false;
	}
}

int find(char* w) {
	for (int i=0;i<s;i++) {
		int r = strcmp(aaa[i],w);
		//printf("Compare '%s' and '%s': %d\n",aaa[i],w,r);
		if (r == 0) {
			return i+1;
		}
	}
	return 0;
}

int count() {
	int r = 0;
	for (int i=0;i<s;i++) {
		r += (int)(bbb[i]);
	}
	return r;
}

int main() {
	scanf("%d\n",&n);
	for (int i=0;i<n;i++) {
		scanf("%d\n",&s);
		res = 0;
		init();
		for (int j=0;j<s;j++) {
			gets(aaa[j]);
		}
		scanf("%d\n",&q);
		for (int j=0;j<q;j++) {
			gets(qs);
			int f = find(qs);
			//printf("Find: %d\n",f);
			if (f > 0) {
				bbb[f-1] = true;
			}
			int current = count();
			//printf("Count: %d\n",current);
			if (current > s-1) {
				res++;
				init();
				bbb[f-1] = true;
			}
		}
		printf("Case #%d: %d\n",i+1,res);
	}
}
