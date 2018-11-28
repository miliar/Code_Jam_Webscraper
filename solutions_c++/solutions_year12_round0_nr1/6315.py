#include <cstdio>
#include <map>
using namespace std;
map<char,char> r;
int main(){
	int n,k,j;
	char x[123];
	freopen("input.txt","r",stdin);
	FILE* file;
	file=fopen("C:\\output.txt","wt");
	r['e']='o';
	r['j']='u';
	r['m']='l';
	r['y']='a';
	r['s']='n';
	r['l']='g';
	r['k']='i';
	r['x']='m';
	r['v']='p';
	r['d']='s';
	r['n']='b';
	r['c']='e';
	r['r']='t';
	r['e']='o';
	r['i']='d';
	r['p']='r';
	r['b']='h';
	r['a']='y';
	r['f']='c';
	r['g']='v';
	r['h']='x';
	r['o']='k';
	r['t']='w';
	r['u']='j';
	r['w']='f';
	r['q']='z';
	r['z']='q';
	r[' ']=' ';
	scanf("%d",&n);
	for(k=1;k<=n;k++){
		scanf("\n%[ a-z]",x);
		for(j=0;j<strlen(x);j++)
			x[j]=r[x[j]];
		fprintf(file,"Case #%d: %s\n",k,x);
	}
	fclose(file);
	return 0;
}