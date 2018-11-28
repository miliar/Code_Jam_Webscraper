#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int main(){
	int n,a[300],i,len,j;
	char s[1000];
	for(i=1;i<=300;i++){a[i]=i;}
	a['a']='y';
    a['b']='h';
    a['c']='e';
    a['d']='s';
    a['e']='o';
    a['f']='c';
    a['g']='v';
    a['h']='x';
    a['i']='d';
    a['j']='u';
    a['k']='i';
    a['l']='g';
    a['m']='l';
    a['n']='b';
    a['o']='k';
    a['p']='r';
    a['q']='z';
    a['r']='t';
    a['s']='n';
    a['t']='w';
    a['u']='j';
    a['v']='p';
    a['w']='f';
    a['x']='m';
    a['y']='a';
    a['z']='q';
    a[' ']=' ';

	scanf("%d",&n);
	for(i=1;i<=n;i++){
		scanf("\n");
		cin.getline(s,1000);
		len=strlen(s);
		printf("Case #%d: ",i);
		for(j=0;j<len;j++){
			printf("%c",a[s[j]]);
		}
		printf("\n");
	}
	return 0;
}
	
