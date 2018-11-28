#include <cstdio>
using namespace std;

const int MAX = 100;
const char _t[26] = {'y','h','e','s','o','c','v','x','d','u','i','g',
	'l','b','k','r','z','t','n','w','j','p','f','m','a','q'}, *const t = _t-'a';

int n;
char s[MAX+1];


int main()
{
	scanf("%d\n", &n);
	for (int i=1; i<=n; ++i) {
		gets(s);
		
		printf("Case #%d: ", i);
		for (int j=0; s[j]; ++j) putchar(s[j]==' ' ? ' ' : t[int(s[j])]);
		putchar('\n');
	}
	
	return 0;
}
