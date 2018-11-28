#include <stdio.h>
#include <map> 
using namespace std;

int main() {
	int n;
	char buffer[101];
	
	map<char,char>  dic;
	dic['y'] = 'a';
	dic['n'] = 'b';
	dic['f'] = 'c';
	dic['i'] = 'd';
	dic['c'] = 'e';
	dic['w'] = 'f';
	dic['l'] = 'g';
	dic['b'] = 'h';
	dic['k'] = 'i';
	dic['u'] = 'j';
	dic['o'] = 'k';
	dic['m'] = 'l';
	dic['x'] = 'm';
	dic['s'] = 'n';
	dic['e'] = 'o';
	dic['v'] = 'p';
	dic['z'] = 'q';
	dic['p'] = 'r';
	dic['d'] = 's';
	dic['r'] = 't';
	dic['j'] = 'u';
	dic['t'] = 'w';
	dic['g'] = 'v';
	dic['h'] = 'x';
	dic['a'] = 'y';
	dic['q'] = 'z';
	dic[' '] = ' ';

	scanf("%d",&n);

	for(int i=0; i<=n; i++) {
		gets(buffer);
		
		if (i>0) {
			printf("Case #%d: ",i);
			int j = 0;
	
			while(buffer[j] != '\0') {
		
				printf("%c",dic[buffer[j]]);
				j++;			
			}
			printf("\n");
				
		}
	}

}
