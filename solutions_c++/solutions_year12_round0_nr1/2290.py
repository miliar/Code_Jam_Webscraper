#include <cstdlib>
#include <iostream>
#include <string.h>
#include <stdio.h>

using namespace std;

char character_map[256];
char result[256];

void proc(char *in)
{
     int i = 0;
     while(*in)
        result[i++] = character_map[*in++];
     result[i] = 0;
 }

int main(int argc, char *argv[])
{
    character_map[' '] = ' ';
    /*character_map['a'] = 'y';
    character_map['o'] = 'e';
    character_map['z'] = 'q';
    

character_map['a'] = 'y';
character_map['c'] = 'e';
character_map['d'] = 's';
character_map['e'] = 'o';
character_map['i'] = 'd';
character_map['j'] = 'u';
character_map['k'] = 'i';
character_map['l'] = 'g';
character_map['m'] = 'l';
character_map['n'] = 'b';
character_map['o'] = 'e';
character_map['p'] = 'r';
character_map['r'] = 't';
character_map['s'] = 'n';
character_map['v'] = 'p';
character_map['x'] = 'm';
character_map['y'] = 'a';
character_map['z'] = 'q';
    

character_map['a'] = 'y';
character_map['b'] = 'h';
character_map['c'] = 'e';
character_map['d'] = 's';
character_map['e'] = 'o';
character_map['f'] = 'c';
character_map['h'] = 'x';
character_map['i'] = 'd';
character_map['j'] = 'u';
character_map['k'] = 'i';
character_map['l'] = 'g';
character_map['m'] = 'l';
character_map['n'] = 'b';
character_map['o'] = 'e';
character_map['p'] = 'r';
character_map['r'] = 't';
character_map['s'] = 'n';
character_map['t'] = 'w';
character_map['v'] = 'p';
character_map['w'] = 'f';
character_map['x'] = 'm';
character_map['y'] = 'a';
character_map['z'] = 'q';*/
    
character_map['a'] = 'y';
character_map['b'] = 'h';
character_map['c'] = 'e';
character_map['d'] = 's';
character_map['e'] = 'o';
character_map['f'] = 'c';
character_map['g'] = 'v';
character_map['h'] = 'x';
character_map['i'] = 'd';
character_map['j'] = 'u';
character_map['k'] = 'i';
character_map['l'] = 'g';
character_map['m'] = 'l';
character_map['n'] = 'b';
character_map['o'] = 'k';
character_map['p'] = 'r';
character_map['q'] = 'z';
character_map['r'] = 't';
character_map['s'] = 'n';
character_map['t'] = 'w';
character_map['u'] = 'j';
character_map['v'] = 'p';
character_map['w'] = 'f';
character_map['x'] = 'm';
character_map['y'] = 'a';
character_map['z'] = 'q';
    
    
    char buf[256] = {};
    //char buf2[256] = {};
    //gets(buf);
    /*gets(buf2);
    for (int i = 0; buf[i] != '\n' && buf[i]; ++i)
    {
        character_map[buf[i]] = buf2[i];
    }*/
        
    //for (char a  = 'a'; a <= 'z'; ++a)
        //printf("character_map['%c'] = '%c';\n", a, character_map[a]);
      //  ar[character_map[a] - 'a'] = 1;
        
    //for (char a  = 'a'; a <= 'z'; ++a)
      //  printf("%c %d\n", a, ar[a - 'a']);

     FILE* fp = fopen("D:\\Dev-Cpp\\Projects\\Code Jam\\A2.in", "r");
     FILE *o_fp = fopen("D:\\Dev-Cpp\\Projects\\Code Jam\\A2_out.txt", "w");
    int n;
    fscanf(fp, "%d", &n);
    printf("%d\n", n);
    //system("PAUSE");
    fgets(buf, 256, fp);
    for (int i = 1; i <=n; ++i)
    {
        fgets(buf, 256, fp);
         //printf("%s\n", buf);
        proc(buf);
        fprintf(o_fp, "Case #%d: %s\n", i, result);
        //system("PAUSE");
    }
    fclose(o_fp);
    scanf("%d", &n);
    
    system("PAUSE");
    return 0;
}
