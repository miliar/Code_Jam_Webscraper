#include <stdio.h>
#include <string.h>
using namespace std;

/*
char sas[6][10000];
char perm[26];
int count[6];
void prepare(){
	int c;
	for (int i=0;i<6;i++) count[i] = 0;
	for (int i=0;i<6;i++) 
		while ( (c=getchar()) != '\n' ) sas[i][count[i]++] = c;
	for (int j=0;j<3;j++)
	for (int i=0;i<count[j];i++)
		if ( sas[j][i] >= 'a' && sas[j][i] <= 'z' ) {
			perm[sas[j][i] - 'a'] = sas[j+3][i];
		}
	perm['z'-'a'] = 'q';
	perm['q' - 'a'] = 'z';
}
*/
char t[10000];
void prepare(){
   t['a']='y';
   t['b']='h';
   t['c']='e';
   t['d']='s';
   t['e']='o';
   t['f']='c';
   t['g']='v';
   t['h']='x';
   t['i']='d';
   t['j']='u';
   t['k']='i';
   t['l']='g';
   t['m']='l';
   t['n']='b';
   t['o']='k';
   t['p']='r';
   t['q']='z';
   t['r']='t';
   t['s']='n';
   t['t']='w';
   t['u']='j';
   t['v']='p';
   t['w']='f';
   t['x']='m';
   t['y']='a';
   t['z']='q';
}

char ss[100000];
void solve(){
	int count=0,c;
	while ( (c=getchar()) != '\n' && c != EOF ) ss[count++] = c;
	for (int i=0;i<count;i++)
		if ( ss[i] >= 'a' && ss[i] <= 'z' ) putchar(t[ss[i]]);
	  else putchar(ss[i]);
}

int main(){
	prepare();      
	int t;
	scanf("%d\n",&t);
	for (int i=1;i<=t;i++){
		printf("Case #%d: ",i);
		solve();
		putchar('\n');
	}                 
	return 0;
}
