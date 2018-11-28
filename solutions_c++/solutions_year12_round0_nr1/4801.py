//gcj A
#include<cstdio>
#include<iostream>
#include<cstring>

using namespace std;

int main()
{
	int cha[256];
	cha['a']='y';
	cha['b']='h';
	cha['c']='e';
	cha['d']='s';
	cha['e']='o';
	cha['f']='c';
	cha['g']='v';
	cha['h']='x';
	cha['i']='d';
	cha['j']='u';
	cha['k']='i';
	cha['l']='g';
	cha['m']='l';
	cha['n']='b';
	cha['o']='k';
	cha['p']='r';
	cha['q']='z';
	cha['r']='t';
	cha['s']='n';
	cha['t']='w';
	cha['u']='j';
	cha['v']='p';
	cha['w']='f';
	cha['x']='m';
	cha['y']='a';
	cha['z']='q';
	cha[' ']=' ';
	
	int n;
	scanf("%d%*d",&n);
	for(int p=0;p<n;p++){
		char str[256];
		fgets(str,256,stdin);
		printf("Case #%d: ",p+1);
		for(int i=0;i<strlen(str)-1;i++){
			printf("%c",cha[str[i]]);
		}
		printf("\n");
	}

	return 0;
}