#include"cstdio"
#include"iostream"
#include"cstring"
#include"algorithm"

using namespace std;

char str[2000] , ans[2000];
int f[200] , g[200];

int main()
{
	
	/*freopen("in.txt","r",stdin);
	freopen("out.txt","w",stdout);*/
	int n;
	scanf("%d\n" , &n);
	
	f['a'] = 'y';
	f['b'] = 'n';
	f['c'] = 'f';
	f['d'] = 'i';
	f['e'] = 'c';
	f['f'] = 'w';
	f['g'] = 'l';
	f['h'] = 'b';
	f['i'] = 'k';
	f['j'] = 'u';
	f['k'] = 'o';
	f['l'] = 'm';
	f['m'] = 'x';
	f['n'] = 's';
	f['o'] = 'e';
	f['p'] = 'v';
	f['q'] = 'z';
	f['r'] = 'p';
	f['s'] = 'd';
	f['t'] = 'r';
	f['u'] = 'j';
	f['v'] = 'g';
	f['w'] = 't';
	f['x'] = 'h';
	f['y'] = 'a';
	f['z'] = 'q';
	
	for(int i = 'a' ; i <= 'z' ; i++)
		g[f[i]] = i;
	
	for(int i = 1 ; i <= n ; i++)
	{
		gets(str);
		int l = strlen(str);
		if(str[l - 1] == '\n') str[--l] = '\0';
		
		for(int i = 0 ; i < l ; i++)
			if(str[i] >= 'a' && str[i] <= 'z')
				ans[i] = g[str[i]];
			else ans[i] = str[i];
		ans[l] = '\0';
		printf("Case #%d: %s\n" , i , ans);
	}
}
