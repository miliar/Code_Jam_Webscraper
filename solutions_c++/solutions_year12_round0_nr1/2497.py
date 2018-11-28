#include <stdio.h>
#include <stdlib.h>
#include <iostream>
 
using namespace std;
 
int main()
{
        char val[30];
        val['a'-'a'] = 'y';//'y';
        val['b'-'a'] = 'h';//'n';
        val['c'-'a'] = 'e';//'f';
        val['d'-'a'] = 's';//'i';
        val['e'-'a'] = 'o';//'c';
        val['f'-'a'] = 'c';//'w';
        val['g'-'a'] = 'v';//'l';
        val['h'-'a'] = 'x';//'b';
        val['i'-'a'] = 'd';//'k';
        val['j'-'a'] = 'u';//'u';
        val['k'-'a'] = 'i';//'o';
        val['l'-'a'] = 'g';//'m';
        val['m'-'a'] = 'l';//'x';
        val['n'-'a'] = 'b';//'s';
        val['o'-'a'] = 'k';//'e';
        val['p'-'a'] = 'r';//'v';
        val['q'-'a'] = 'z';//'z';
        val['r'-'a'] = 't';//'p';
        val['s'-'a'] = 'n';//'d';
        val['t'-'a'] = 'w';//'r';
        val['u'-'a'] = 'j';//'j';
        val['v'-'a'] = 'p';//'g';
        val['w'-'a'] = 'f';//'t';
        val['x'-'a'] = 'm';//'h';
        val['y'-'a'] = 'a';//'a';
        val['z'-'a'] = 'q';//'q';
 
        int n;
        scanf("%i", &n);
        //printf("%i", n);
        for(int i=1;i<=n;i++)
        {
                char texto[200];
                scanf("%*c%[^\n]", &texto);
                //cout<<texto<<endl;
                int j=0;
                while(texto[j]!='\0')
                {
                        if(texto[j]!=' ')
                                texto[j] = val[texto[j]-'a'];
                        j++;
                }
                printf("Case #%i: %s\n", i, texto);
        }
        return 0;
}