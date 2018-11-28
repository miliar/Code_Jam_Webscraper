




#include <stdio.h>
int main () {
	int t;
	int j=1;
		int i;
		int b[400]={0};
			for ( i = 0; i<400;i++){
			b[i]=i;
		}
		b['a']='y';
		b['b']='h';
		b['c']='e';
		b['d']='s';
		b['e']='o';
		b['f']='c';
		b['g']='v';
		b['h']='x';
		b['i']='d';
		b['j']='u';
		b['k']='i';
		b['l']='g';
		b['m']='l';
		b['n']='b';
		b['o']='k';
		b['p']='r';
		b['q']='z';
		b['r']='t';
		b['s']='n';
		b['t']='w';
		b['u']='j';
		b['v']='p';
		b['w']='f';
		b['x']='m';
		b['y']='a';
		b['z']='q';
	scanf("%d",&t);
	getchar();
	while(t--){
		char a[101];
		gets(a);
		printf("Case #%d: ",j);
		for(i=0;a[i]!='\0';i++)
		printf("%c",b[a[i]]);
		printf("\n");
		j++;
}
return 0;
}
