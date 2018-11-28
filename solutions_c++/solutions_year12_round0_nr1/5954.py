#include<stdio.h>
char x[100][1000];

char y[123];

main()

{
y['a'] = 'y';
 y['b'] = 'h';
 y['c'] = 'e';
 y['d'] = 's';
 y['e'] = 'o';
 y['f'] = 'c';
 y['g'] = 'v';
 y['h'] = 'x';
 y['i'] = 'd';
 y['j'] = 'u';
 y['k'] = 'i';
 y['l'] = 'g';
 y['m'] = 'l';
 y['n'] = 'b';
 y['o'] = 'k';
 y['p'] = 'r';
 y['q'] = 'z';
 y['r'] = 't';
 y['s'] = 'n';
 y['t'] = 'w';
 y['u'] = 'j';
 y['v'] = 'p';
 y['w'] = 'f';
 y['x'] = 'm';
 y['y'] = 'a';
 y['z'] = 'q';
 int n;
 scanf("%d ",&n);
 int i,j;
 for(j=0;j<n;j++)
 gets(x[j]);
 
 for(j=0;j<n;j++)
 for(i=0;x[j][i]!=0;i++)
 {if(x[j][i]!=' ') x[j][i]=y[x[j][i]];}
 
 for(j=0;j<n;j++)
 printf("Case #%d: %s\n",j+1,x[j]);
      
      
scanf(" ");
}
/*

 y['a'] = 'y';
 y['b'] = 'h';
 y['c'] = 'e';
 y['d'] = 's';
 y['e'] = 'o';
 y['f'] = 'c';
 y['g'] = 'v';
 y['h'] = 'x';
 y['i'] = 'd';
 y['j'] = 'u';
 y['k'] = 'i';
 y['l'] = 'g';
 y['m'] = 'l';
 y['n'] = 'b';
 y['o'] = 'k';
 y['p'] = 'r';
 y['q'] = 'z';
 y['r'] = 't';
 y['s'] = 'n';
 y['t'] = 'w';
 y['u'] = 'j';
 y['v'] = 'p';
 y['w'] = 'f';
 y['x'] = 'm';
 y['y'] = 'a';
 y['z'] = 'q';

 
*/
