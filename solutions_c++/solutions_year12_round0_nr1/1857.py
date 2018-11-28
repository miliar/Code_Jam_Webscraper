#include <iostream>
#include <map>
using namespace std;
char dd[1024],dd2[1024];
int n;
void learn(){
	int len,len2;
	map<char,char>mm;
	map<char,char>::iterator mit;
	for (int t = 0; t < 3; t++){
		gets(dd);
		gets(dd2);
		len = strlen(dd);
		len2 = strlen(dd2);
		for (int i = 0; i < len; i++)
		{
			mm.insert(pair<char,char>(dd[i],dd2[i]));
		}
	}
	mm.insert(pair<char,char>('a','y'));
	mm.insert(pair<char,char>('o','e'));
	mm.insert(pair<char,char>('z','q'));
	mm.insert(pair<char,char>('q','z'));
	for (mit = mm.begin(); mit != mm.end(); mit++)
	{
		printf("dd['%c'] = '%c';\n",mit->first,mit->second);
	}

}
void init(){
	memset(dd,0,sizeof(dd));
	dd[' '] = ' ';
	dd['a'] = 'y';
	dd['b'] = 'h';
	dd['c'] = 'e';
	dd['d'] = 's';
	dd['e'] = 'o';
	dd['f'] = 'c';
	dd['g'] = 'v';
	dd['h'] = 'x';
	dd['i'] = 'd';
	dd['j'] = 'u';
	dd['k'] = 'i';
	dd['l'] = 'g';
	dd['m'] = 'l';
	dd['n'] = 'b';
	dd['o'] = 'k';
	dd['p'] = 'r';
	dd['q'] = 'z';
	dd['r'] = 't';
	dd['s'] = 'n';
	dd['t'] = 'w';
	dd['u'] = 'j';
	dd['v'] = 'p';
	dd['w'] = 'f';
	dd['x'] = 'm';
	dd['y'] = 'a';
	dd['z'] = 'q';
}
int main(){
	int len;
	//learn();
//	freopen("d:/1.in","r",stdin);
//	freopen("d:/1.out","w",stdout);
	init();
	while (scanf("%d",&n) != EOF)
	{
		for (int i = 1; i <= n; i++)
		{
			gets(dd2);
			len = strlen(dd2);
			while (!len)
			{
				gets(dd2);
				len = strlen(dd2);
			}
			printf("Case #%d: ",i);
			for (int j = 0; j < len; j++){
				printf("%c",dd[dd2[j]]);
			}
			printf("\n");
		}
	}
	return 0;
}