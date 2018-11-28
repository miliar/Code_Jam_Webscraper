/***************************************************************************
 * 
 * Copyright (c) 2012, Inc. All Rights Reserved
 * 
 **************************************************************************/
 
 
 
/**
 * @file a.cpp
 * @author work
 * @date 2012/04/28 09:34:48
 * @brief 
 *  
 **/

#include <stdio.h>
#include <stdlib.h>

int main() {
    int T, A, B, case_num = 1;
    scanf("%d", &T);
    while (case_num <= T) {
        scanf("%d%d", &A, &B);
        float prob[A], tmp_key_num;
        float tmp_prob1 = 1.0;
        for (int i = 0; i < A; i++) {
            scanf("%f", &prob[i]);
            tmp_prob1 *= prob[i];
        } 

        float min_key_num = B + 2.0;

        tmp_key_num = (B - A + 1) * tmp_prob1 + (2 * B - A + 2) * (1 - tmp_prob1);
        if (tmp_key_num < min_key_num) {
            min_key_num = tmp_key_num;
        }

        float tmp_prob2 = 1.0;
        for (int i = 0; i < A - 1; i ++) {
            tmp_prob2 *= prob[i];
        }

        tmp_key_num = (B - A + 3) * tmp_prob2 + (2 * B - A + 4) * (1 - tmp_prob2);
        if (tmp_key_num < min_key_num) {
            min_key_num = tmp_key_num;
        }

        printf("Case #%d: %.6f\n", case_num, min_key_num);
        case_num ++;
    }

    return 0;
}




















/* vim: set expandtab ts=4 sw=4 sts=4 tw=100: */
