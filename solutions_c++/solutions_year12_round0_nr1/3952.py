#include <cstdio>
#include <cstring>

char table[127] = {0};
void working(int round){
	int i,n;
	char input[1000];
	gets(input);
	int len = strlen(input);
	printf("Case #%d: ",round);
	for(i=0;i<len;i++){
		printf("%c",table[input[i]]);
	}
	printf("\n");
}
int main(){
	int T;
	int i;
	char tmp[100];
	
	table[' '] = ' ';
	table['a'] = 'y';
	table['b'] = 'h';
	table['c'] = 'e';
	table['d'] = 's';
	table['e'] = 'o';
	table['f'] = 'c';
	table['g'] = 'v';
	table['h'] = 'x';
	table['i'] = 'd';
	table['j'] = 'u';
	table['k'] = 'i';
	table['l'] = 'g';
	table['m'] = 'l';
	table['n'] = 'b';
	table['o'] = 'k';
	table['p'] = 'r';
	table['q'] = 'z';
	table['r'] = 't';
	table['s'] = 'n';
	table['t'] = 'w';
	table['u'] = 'j';
	table['v'] = 'p';
	table['w'] = 'f';
	table['x'] = 'm';
	table['y'] = 'a';
	table['z'] = 'q';
	
	scanf("%d",&T);
	gets(tmp);
	for(i=1;i<=T;i++){
		working(i);
	}
	return 0;
}