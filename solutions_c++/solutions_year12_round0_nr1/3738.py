#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char** argv){


int num;
char str[1000];
char mapping[200];

mapping['a'] = 'y';
mapping['b'] = 'h';
mapping['c'] = 'e';
mapping['d'] = 's';
mapping['e'] = 'o';
mapping['f'] = 'c';
mapping['g'] = 'v';
mapping['h'] = 'x';
mapping['i'] = 'd';
mapping['j'] = 'u';
mapping['k'] = 'i';
mapping['l'] = 'g';
mapping['m'] = 'l';
mapping['n'] = 'b';
mapping['o'] = 'k';
mapping['p'] = 'r';
mapping['q'] = 'z';
mapping['r'] = 't';
mapping['s'] = 'n';
mapping['t'] = 'w';
mapping['u'] = 'j';
mapping['v'] = 'p';
mapping['w'] = 'f';
mapping['x'] = 'm';
mapping['y'] = 'a';
mapping['z'] = 'q';


scanf("%d\n", &num);

for(int i = 0 ; i < num ; ++i){
        gets(str);
        printf("Case #%d: ", i + 1);
        for(int j = 0 ; str[j] !='\0'; ++j){
                if(str[j] >= 'a' && str[j] <= 'z'){
                          putchar(mapping[str[j]]);
                          }
                else
                          putchar(str[j]);
                
                
                }
        putchar('\n');
        
        }


return 0;
}
