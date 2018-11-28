#include <cstdio>
#include <map>

using namespace std;

int main()
{
	freopen("ololo.txt","r",stdin);
	freopen("out.txt","w",stdout);
	map<char,char> dict;

	dict['\n']='\n';
	dict[' ']=' ';
	dict['q']='z';
	dict['w']='f';
	dict['e']='o';
	dict['r']='t';
	dict['t']='w';
	dict['y']='a';
	dict['u']='j';
	dict['i']='d';
	dict['o']='k';
	dict['p']='r';
	dict['a']='y';
	dict['s']='n';
	dict['d']='s';
	dict['f']='c';
	dict['g']='v';
	dict['h']='x';
	dict['j']='u';
	dict['k']='i';
	dict['l']='g';
	dict['z']='q';
	dict['x']='m';
	dict['c']='e';
	dict['v']='p';
	dict['b']='h';
	dict['n']='b';
	dict['m']='l';

	int n;
	scanf("%d",&n);
	getc(stdin);
	for (int i=0; i<n; i++) {
		printf("Case #%d: ",i+1);
		char p=' ';
		while (p!='\n') {
			scanf("%c",&p);
			printf("%c",dict[p]);
		}
	}


	return 0;
}