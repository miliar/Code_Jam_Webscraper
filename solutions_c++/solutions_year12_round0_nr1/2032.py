/* 
 * File:   main.cpp
 * Author: liuyubo
 *
 * Created on April 14, 2012, 7:29 PM
 */

#include <cstdlib>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cctype>

#include <utility>
#include <iostream>
#include <string>
#include <algorithm>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <queue>
#include <map>

using namespace std;

void loadData( void );
void proc( void );
void printRes( int );

char mapletter[26]={
    'y', //a
    'n', //b
    'f', //c
    'i', //d
    'c', //e
    'w', //f
    'l', //g
    'b', //h
    'k', //i
    'u', //j
    'o', //k
    'm', //l
    'x', //m
    's', //n
    'e', //o
    'v', //p
    'z', //q
    'p', //r
    'd', //s
    'r', //t
    'j', //u
    'g', //v
    't', //w
    'h', //x
    'a', //y
    'q'  //z
};

char input[105];

int main(int argc, char** argv) {

    freopen("A-small-attempt0.in","r",stdin);
    freopen("A.out","w",stdout);
    loadData();
    
    return 0;
}

void proc( void ){
    
    int len = strlen(input);
    for( int i = 0 ; i < len ; i ++ ){
        if( input[i] != ' '){
            for( int j = 0 ; j < 26 ; j ++ )
                if( input[i] == mapletter[j] )
                    printf("%c",'a'+j);
        }
        else
            printf(" ");
    }
    return ;
}

void loadData( void ){

    int T;
    char enter;
    scanf("%d%c",&T,&enter);
    for( int cases = 1 ; cases <= T ; cases ++ ){
        gets(input);
        printRes( cases );
    }
    return;
}

void printRes( int index ){

    printf("Case #%d: ",index);
    proc();
    printf("\n");
    return;
}

