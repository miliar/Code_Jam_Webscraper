/* 
 * File:   main.cpp
 * Author: joker
 *
 * Created on 14 Апрель 2012 г., 14:11
 */

#include <cstdlib>
#include <map>
#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;


map<char, char> mapper;
int main(int argc, char** argv) {
    freopen("A-small-attempt0.in","r",stdin);
    freopen("A-small-attempt0.out","w",stdout);
    mapper['a']='y';
    mapper['b']='h';
    mapper['c']='e';
    mapper['d']='s';
    mapper['e']='o';
    mapper['f']='c';
    mapper['g']='v';
    mapper['h']='x';
    mapper['i']='d';
    mapper['j']='u';
    mapper['k']='i';
    mapper['l']='g';
    mapper['m']='l';
    mapper['n']='b';
    mapper['o']='k';
    mapper['p']='r';
    mapper['q']='z';
    mapper['r']='t';
    mapper['s']='n';
    mapper['t']='w';
    mapper['u']='j';
    mapper['v']='p';
    mapper['w']='f';
    mapper['x']='m';
    mapper['y']='a';
    mapper['z']='q';
    mapper[' ']=' ';
    int T;
    cin >> T;
    char str[1024]={0};
    cin.getline(str,1024,'\n');
    for(int i = 0; i<T; i++)
    {
        cin.getline(str,1024,'\n');
        cout << "Case #" << (i+1) <<": ";
        int len = strlen(str);
        for(int i = 0; i<len; i++)
            printf("%c",mapper[str[i]]);
        printf("\n");
    }
    return 0;
}

