#include <cstdio>
#include <algorithm>

using namespace std;

char t[]="ynficwlbkuomxsevzpdrjgthaq",table[256];
char m[1000];

void resoud(){
	for (char c='a';c!='\n';){
		scanf("%c",&c);
		if ('a'<=c && c<='z')
			printf("%c",table[c]);
		else
			printf("%c",c);
	}
}

int main(){
	int T;
	for (int i='a';i<='z';i++)
		table[t[i-'a']]=i;
	scanf("%d\n",&T);
	for (int i=0;i<T;i++){
		printf("Case #%d: ",i+1);
		resoud();
	}
	return 0;
}
