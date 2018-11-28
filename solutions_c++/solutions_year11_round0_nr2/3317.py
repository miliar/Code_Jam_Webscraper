//
//  main.cpp
//  B
//
//  Created by MMX on 11/05/07.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#include <cstdio>
#include <vector>

using namespace std;

class crule {
public:
    char from[2];
    char to;
    crule (char *str) {
        from[0] = str[0];
        from[1] = str[1];
        to = str[2];
    }
    bool isFit(char str1, char str2) {
        if ((str1 == from[0] and str2 == from[1]) or (str1 == from[1] and str2 == from[0])) {
            return true;
        } else {
            return false;
        }
    }
};

class drule {
public:
    char from[2];
    drule (char *str) {
        from[0] = str[0];
        from[1] = str[1];
    }
    bool isFit(char str1, char str2) {
        if ((str1 == from[0] and str2 == from[1]) or (str1 == from[1] and str2 == from[0])) {
            return true;
        } else {
            return false;
        }
    }
};

int main (int argc, const char * argv[])
{
    int T;
    scanf("%d", &T);
    for (int t = 0; t < T; t++) {
        vector<crule> crules;
        vector<drule> drules;
        int C, D, N;
        int output_len = 0;
        char str[150] = {0}, output[150] = {0};
        scanf("%d", &C);
        for (int c = 0; c < C; c++) {
            scanf("%s", str);
            crule *r = new crule(str);
            crules.push_back(*r);
        }
        scanf("%d", &D);
        for (int d = 0; d < D; d++) {
            scanf("%s", str);
            drule *r = new drule(str);
            drules.push_back(*r);
        }
        scanf("%d", &N);
        scanf("%s", str);
        bool c_flag = true;
        bool d_flag = true;
        output[output_len++] = str[0];
        for (int i = 1; i < N; i++) {
            c_flag = false;
            d_flag = false;
            for (int c = 0; c < C; c++) {
                if (crules[c].isFit(output[output_len-1], str[i])) {
                    output[output_len - 1] = crules[c].to;
                    c_flag = true;
                    break;
                }
            }
            if (c_flag == false) {
                for (int d = 0; d < D; d++) {
                    for (int e = 0; e < output_len; e++) {
                        if (drules[d].isFit(output[e], str[i])) {
                            output_len = 0;
                            d_flag = true;
                            break;
                        }
                    }
                    if (d_flag == true)
                        break;
                }
            }
            if (c_flag == false && d_flag == false) {
                output[output_len++] = str[i];
            }
            output[output_len] = 0;
        }
        printf("Case #%d: [", t + 1);
        for (int i = 0; i < output_len; i++) {
            printf("%c", output[i]);
            if (i < output_len - 1)
                printf(", ");
        }
        printf("]\n");
    }
    
    return 0;
}

