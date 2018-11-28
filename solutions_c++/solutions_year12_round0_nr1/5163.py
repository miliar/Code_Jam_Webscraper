/***************************************************************************
 * 
 * Copyright (c) 2012, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 
 
/**
 * @file a.cpp
 * @author work
 * @date 2012/04/14 09:17:32
 * @brief 
 *  
 **/
#include<stdio.h>
#include<stdlib.h>

int main() {
    int map[26];
    map['e' - 'a'] = 'o' - 'a';
    map['j' - 'a'] = 'u' - 'a';
    map['p' - 'a'] = 'r' - 'a';
    map['m' - 'a'] = 'l' - 'a';
    map['y' - 'a'] = 'a' - 'a';
    map['s' - 'a'] = 'n' - 'a';
    map['l' - 'a'] = 'g' - 'a';
    map['c' - 'a'] = 'e' - 'a';
    map['k' - 'a'] = 'i' - 'a';
    map['d' - 'a'] = 's' - 'a';
    map['x' - 'a'] = 'm' - 'a';
    map['v' - 'a'] = 'p' - 'a';
    map['n' - 'a'] = 'b' - 'a';
    map['r' - 'a'] = 't' - 'a';
    map['i' - 'a'] = 'd' - 'a';
    map['a' - 'a'] = 'y' - 'a';
    map['b' - 'a'] = 'h' - 'a';
    map['f' - 'a'] = 'c' - 'a';
    map['g' - 'a'] = 'v' - 'a';
    map['h' - 'a'] = 'x' - 'a';
    map['o' - 'a'] = 'k' - 'a';
    map['t' - 'a'] = 'w' - 'a';
    map['u' - 'a'] = 'j' - 'a';
    map['w' - 'a'] = 'f' - 'a';
    map['q' - 'a'] = 'z' - 'a';
    map['z' - 'a'] = 'q' - 'a';
    int T, len, i, tmp, case_count = 1;
    char googlerese[100];
    scanf("%d", &T);
    tmp = getchar();
    while(case_count <= T) {
        tmp  = getchar();
        len = 0;
        while (tmp != '\n') {
            googlerese[len ++] = tmp;
            tmp = getchar();
        }
        printf("Case #%d: ", case_count);
        for (i = 0; i < len; i ++) {
            if (googlerese[i] < 'a' || googlerese[i] > 'z') {
                printf(" ");
            }
            else {
                printf("%c", map[googlerese[i] - 'a'] + 'a');
            }
        }
        printf("\n");
        case_count ++;
    } 
}



















/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
