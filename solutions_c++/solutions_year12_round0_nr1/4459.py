#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <cctype>
#include <math.h>

#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>

#include <deque>
#include <queue>
#include <map>

using namespace std;
#define maxn  1e8
#define minn -1e9
#define eps 1e-6
const int oo=0x7f;
const int Range=1000000;
const int Nnum=510;
       
/*int cmp(const void *a, const void *b) {
    return *(double*) a - *(double*) b;
}*/

int Min( int a , int b ){
       return a > b ? b : a ;
}

int Max(double a ,double b){
    return a>b?a:b;
}


int tab[40];

void PrintTable(){
    tab['a']='y';
    tab['b']='h';
    tab['c']='e';
    tab['d']='s';
    tab['e']='o';
    tab['f']='c';
    tab['g']='v';
    tab['h']='x';
    tab['i']='d';
    tab['j']='u';
    tab['k']='i';
    tab['l']='g';
    tab['m']='l';
    tab['n']='b';
    tab['o']='k';
    tab['p']='r';
    tab['q']='z';
    tab['r']='t';
    tab['s']='n';
    tab['t']='w';
    tab['u']='j';
    tab['v']='p';
    tab['w']='f';
    tab['x']='m';
    tab['y']='a';
    tab['z']='q';
    tab[' ']=' ';
}

int main() {
    int i, j, k;
    char str[110],str1[110];
    int cas,len;
    freopen("s.txt","r",stdin);
    freopen("A-small.txt","w",stdout);
    PrintTable();
    scanf("%d",&cas);
    getchar();
    for(k=1;k<=cas;k++){
        gets(str);
        len=strlen(str);
        for(i=0;i<len;i++){
            str1[i]=tab[str[i]];
        }
        str1[len]='\0';
        printf("Case #%d: ",k);
        puts(str1);
        //cout<<endl;
 
        
    }
    //printf("%c\n%c\n",tab['a'],tab['b']);
    return 0;
}
