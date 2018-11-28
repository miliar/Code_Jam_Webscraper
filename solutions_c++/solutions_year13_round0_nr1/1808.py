//
//  main.cpp
//  A
//
//  Created by IwfWcf on 13-4-13.
//  Copyright (c) 2013年 IwfWcf. All rights reserved.
//

#include <iostream>
#include <stdio.h>

using namespace std;

string r[4];
bool mark[256];

inline int judge()
{
    int count;
    for (int i = 0; i < 4; i++) {
        mark['X'] = mark['O'] = mark['T'] = mark['.'] = false;
        for (int j = 0; j < 4; j++)
            mark[r[i][j]] = true;
        count = mark['X'] + mark['O'] + mark['T'] + mark['.'];
        if (count > 2 || mark['.'] || mark['X'] && mark['O']) continue;
        if (mark['X']) return 1;
        else return 2;
    }
    for (int j = 0; j < 4; j++) {
        mark['X'] = mark['O'] = mark['T'] = mark['.'] = false;
        for (int i = 0; i < 4; i++)
            mark[r[i][j]] = true;
        count = mark['X'] + mark['O'] + mark['T'] + mark['.'];
        if (count > 2 || mark['.'] || mark['X'] && mark['O']) continue;
        if (mark['X']) return 1;
        else return 2;
    }
    mark['X'] = mark['O'] = mark['T'] = mark['.'] = false;
    mark[r[0][0]] = mark[r[1][1]] = mark[r[2][2]] = mark[r[3][3]] = true;
    count = mark['X'] + mark['O'] + mark['T'] + mark['.'];
    if (count <= 2 && !mark['.'] && !(mark['X'] && mark['O']))
        if (mark['X']) return 1;
        else return 2;
    mark['X'] = mark['O'] = mark['T'] = mark['.'] = false;
    mark[r[0][3]] = mark[r[1][2]] = mark[r[2][1]] = mark[r[3][0]] = true;
    count = mark['X'] + mark['O'] + mark['T'] + mark['.'];
    if (count <= 2 && !mark['.'] && !(mark['X'] && mark['O']))
        if (mark['X']) return 1;
        else return 2;
    return 0;
}

int main(int argc, const char * argv[])
{
    freopen("/Users/IwfWcf/Desktop/A/in.txt", "r", stdin);
    freopen("/Users/IwfWcf/Desktop/A/out.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int cases = 1; cases <= t; cases++) {
        for (int i = 0; i < 4; i++)
            cin >> r[i];
        int ret = judge();
        printf("Case #%d: ", cases);
        if (ret) {
            if (ret == 1) printf("X won\n");
            else printf("O won\n");
        } else {
            bool flag = false;
            for (int i = 0; i < 4; i++)
                for (int j = 0; j < 4; j++)
                    if (r[i][j] == '.') flag = true;
            if (flag) printf("Game has not completed\n");
            else printf("Draw\n");
        }
    }
    return 0;
}

