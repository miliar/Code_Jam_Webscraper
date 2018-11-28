#include <cstdio>
#include <set>
#include <map>

using namespace std;
map<char, char> mm;


int main() {
    mm['q'] = 'z';
    mm['z'] = 'q';
    mm[' '] = ' ';
    mm['a'] = 'y';
    mm['b'] = 'h';
    mm['c'] = 'e';
    mm['d'] = 's';
    mm['e'] = 'o';
    mm['f'] = 'c';
    mm['g'] = 'v';
    mm['h'] = 'x';
    mm['i'] = 'd';
    mm['j'] = 'u';
    mm['k'] = 'i';
    mm['l'] = 'g';
    mm['m'] = 'l';
    mm['n'] = 'b';
    mm['o'] = 'k';
    mm['p'] = 'r';
    mm['r'] = 't';
    mm['s'] = 'n';
    mm['t'] = 'w';
    mm['u'] = 'j';
    mm['v'] = 'p';
    mm['w'] = 'f';
    mm['x'] = 'm';
    mm['y'] = 'a';
    mm['\n'] = '\n';
    int nt;
    scanf("%d",&nt);
    char s[200];
    gets(s);
    for(int ttt=1;ttt<=nt;ttt++) {
	printf("Case #%d: ",ttt);
	gets(s);
	int l1 = strlen(s);
	for(int i=0;i<l1;i++) {
	    putchar(mm[s[i]]);
	}
	puts("");
    }
    return 0;
}
