/* 
 * File:   speak.cc
 * Author: vivek
 *
 * Created on April 14, 2012, 11:48 PM
 */

#include <cstdlib>
#include<map>
#include<cstring>
#include<cstdio>
using namespace std;

/*
 * 
 */
int main(int argc, char** argv) {
    int t, i;
    char c = 'a';
    map<char, char> dict;
    dict['a'] = 'y';
    dict['b'] = 'h';
    dict['c'] = 'e';
    dict['d'] = 's';
    dict['e'] = 'o';
    dict['f'] = 'c';
    dict['g'] = 'v';
    dict['h'] = 'x';
    dict['i'] = 'd';
    dict['j'] = 'u';
    dict['k'] = 'i';
    dict['l'] = 'g';
    dict['m'] = 'l';
    dict['n'] = 'b';
    dict['o'] = 'k';
    dict['p'] = 'r';
    dict['q'] = 'z';
    dict['r'] = 't';
    dict['s'] = 'n';
    dict['t'] = 'w';
    dict['u'] = 'j';
    dict['v'] = 'p';
    dict['w'] = 'f';
    dict['x'] = 'm';
    dict['y'] = 'a';
    dict['z'] = 'q';
    i = 0;
    scanf("%d", &t);
    getchar();
    while (t--) {
        i++;
        printf("Case #%d: ", i);        
        while((c = getchar()) != '\n' && c != EOF)        
         {            
            if (c >= 'a' && c <= 'z') {
                printf("%c", dict[c]);
            } else {
                printf("%c", c);
            }
        }while((c!=EOF)&& (c!= '\n') && (c!= '\r'));
        printf("\n");
    }
    return 0;
}

