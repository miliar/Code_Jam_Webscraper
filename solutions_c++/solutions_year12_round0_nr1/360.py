#include <cstdio>
#include <map>

std::map<char,char> m;

int main(){
m['a']='y';
m['b']='h';
m['c']='e';
m['d']='s';
m['e']='o';
m['f']='c';
m['g']='v';
m['h']='x';
m['i']='d';
m['j']='u';
m['k']='i';
m['l']='g';
m['m']='l';
m['n']='b';
m['o']='k';
m['p']='r';
m['q']='z';
m['r']='t';
m['s']='n';
m['t']='w';
m['u']='j';
m['v']='p';
m['w']='f';
m['x']='m';
m['y']='a';
m['z']='q';
m['\r']='\r';
m['\n']='\n';
m[' ']=' ';


	int n;
	scanf("%d\n", &n);
	for(int i=1;i<=n;i++){
	printf("Case #%d: ",i);
	char c=' ';
	while(c!='\n'){
		scanf("%c", &c);
		printf("%c", m[c]);
	}
	}
	return 0;
}

