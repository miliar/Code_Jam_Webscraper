#include <cstdio>
#include <iostream>
#include <cctype>

using namespace std;

int main () {

		freopen ("input.in","r",stdin);
		freopen ("output.out","w",stdout);
		
		int TC;
		char input[200];
		char cmap[200];
		cmap['y']='a';
		cmap['n']='b';
		cmap['f']='c';
		cmap['i']='d';
		cmap['c']='e';
		cmap['w']='f';
		cmap['l']='g';
		cmap['b']='h';
		cmap['k']='i';
		cmap['u']='j';
		cmap['o']='k';
		cmap['m']='l';
		cmap['x']='m';
		cmap['s']='n';
		cmap['e']='o';
		cmap['v']='p';
		cmap['z']='q';
		cmap['p']='r';
		cmap['d']='s';
		cmap['r']='t';
		cmap['j']='u';
		cmap['g']='v';
		cmap['t']='w';
		cmap['h']='x';
		cmap['a']='y';
		cmap['q']='z';

		scanf ("%d",&TC);
		getchar();
		for (int j=0;j<TC;j++) {
				fgets (input,200,stdin);
				for (int i=0;input[i]!='\n';i++) {
						if (isalpha(input[i]))
						input[i]=cmap[input[i]];
				}
				printf ("Case #%d: %s",j+1,input);
		}
}











