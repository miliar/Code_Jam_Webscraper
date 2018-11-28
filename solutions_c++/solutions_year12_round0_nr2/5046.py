/***************************************************************************
 * 
 * Copyright (c) 2012, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 
 
/**
 * @file b.cpp
 * @author work
 * @date 2012/04/14 10:28:30
 * @brief 
 *  
 **/


#include<stdio.h>
#include<stdlib.h>

int main() {
    int i, T, N, S, p, t[100], case_count = 1;
    scanf("%d", &T);
    while(case_count <= T) {
        scanf("%d%d%d", &N, &S, &p);
        for (i  = 0; i < N; i++) {
            scanf("%d", &t[i]);
        }
        int result_count = 0;
        for (i = 0; i < N; i++) {
            int max_num = t[i] / 3;
            if (t[i] % 3 != 0) {
                max_num += 1;
            }

            if (max_num >= p) {
                result_count ++;
            }
            else {
                if (S > 0) {
                    if (t[i] % 3 == 0) {
                        if (t[i] - 3 < 0) {
                            max_num = 0;
                        }
                        else {
                            max_num = (t[i] - 3) / 3 + 2;
                        }
                    }
                    else if(t[i] % 3 == 1) {
                        max_num = t[i] / 3 + 1;
                    }
                    else {
                        max_num = t[i] / 3 + 2;
                    }

                    if (max_num >= p) {
                        result_count ++;
                        S --;
                    }
                }
            }
        }
        printf("Case #%d: %d\n", case_count, result_count);
        case_count ++;
    }
}


















/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
