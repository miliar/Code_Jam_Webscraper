/*
 * by xsy, 2011-05-07
 */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>

#define DEBUG 0

int main(int argc, char **argv)
{
    if (argc != 2) {
        printf("Usage: ./main input_file\n");
        return -1;
    }
    FILE *fp = fopen(argv[1], "r");
    if (!fp) {
        printf("Input File %s Open Error.\n", argv[1]);
        return 0;
    }

    int T, sc_cnt, ym_cnt, N;
    int i, j, j_new, k, l;
    int Y;
//    typedef char[3] sc_data;
//    typedef char[2] ym_data;
    fscanf(fp, "%d\n", &T);
    for (i = 0; i < T; i++) {
        /* 生成规则 */
        fscanf(fp, "%d ", &sc_cnt);
        char sc[sc_cnt][4];
        memset(sc, 0, sc_cnt * 4 * sizeof(char));
        for (j = 0; j < sc_cnt; j++) {
            //fscanf(fp, "%c%c%c", &sc[j][0], &sc[j][1], &sc[j][2]);
            fscanf(fp, "%s", &sc[j]);
            if (DEBUG)
                printf("sc%d: %c%c%c\n", j, sc[j][0], sc[j][1], sc[j][2]);
        }
        /* 湮灭规则 */
        fscanf(fp, "%d ", &ym_cnt);
        char ym[ym_cnt][3];
        memset(ym, 0, ym_cnt * 3 * sizeof(char));
        for (j = 0; j < ym_cnt; j++) {
            fscanf(fp, "%s", &ym[j]);
            if (DEBUG)
                printf("ym%d: %c%c\n", j, ym[j][0], ym[j][1]);
        }
        /* 输入数据 */
        fscanf(fp, "%d ", &N);
        char input[N + 1];
        memset(input, 0, (N+1) * sizeof(char));
        fscanf(fp, "%s ", input);
        if (DEBUG)
            printf("%s\n", input);

        printf("Case #%d: [", i + 1);
        int first_output = 0;
        char first, second, new_second, result = '\0';
        char output[N+1];
        memset(output, 0, (N+1) * sizeof(char));
        //first = input[0];
        //for (j = 0; j < N; j++) {       // 在输入序列中循环
        for (j = 0; j < N;) {   // 在输入序列中循环
            first = input[j];
            if (j + 1 == N) {
                result = first;
                // added
                if (strlen(output) != 0)
                    sprintf(output, "%s, %c", output, result);
                else
                    sprintf(output, "%c", result);
                // added end
                j++;
                goto yanmie;
            }
            second = input[j + 1];
            // 首先在生成规则中查找
            for (k = 0; k < sc_cnt; k++) {
                if ((sc[k][0] == first && sc[k][1] == second) || (sc[k][0] == second && sc[k][1] == first)) {
                    result = sc[k][2];
                    // added
                    if (strlen(output) != 0)
                        sprintf(output, "%s, %c", output, result);
                    else
                        sprintf(output, "%c", result);
                    // added end
                    j += 2;
                    //first = input[j];
                    goto yanmie;
                }
            }
            // 如果没有则在湮灭规则中查找
            for (j_new = j + 1; j_new < N; j_new++) {   // 要循环整个input来找湮灭规则
                second = input[j_new];  // 第一次会重复
                for (k = 0; k < ym_cnt; k++) {
                    if ((ym[k][0] == first && ym[k][1] == second) || (ym[k][0] == second && ym[k][1] == first)) {       // 有湮灭！
                        if (j + 1 == j_new) {
                            j += 2;
                            result = '\0';
                            // added
        memset(output, 0, (N+1) * sizeof(char));
                            // added end
                            goto yanmie;
                        }
                        // 还需要比较和j_new - 1是否有生成规则
                        //如果有生成规则，则继续往下比较，看能否找到一个湮灭的！
                        new_second = input[j_new - 1];  // 第一次会重复
                        for (l = 0; l < sc_cnt; l++) {
                            if ((sc[l][0] == new_second && sc[l][1] == second) || (sc[l][0] == second && sc[l][1] == new_second))
                                goto loop1;
                        }
                        // 如果没有生成规则，则是最好的，直接全部湮灭掉！！！
                        j = j_new + 1;
                        //first = input[j];
                        result = '\0';
                        // added
        memset(output, 0, (N+1) * sizeof(char));
                        // added end
                        goto yanmie;
                    }
                }       // 下一个湮灭规则
              loop1:
                int aa;
            }   // j_new 下一个输入字符
            result = first;     // 则那个就定了！
            // added
            if (strlen(output) != 0)
                sprintf(output, "%s, %c", output, result);
            else
                sprintf(output, "%c", result);
            // added end
            j++;
            //first = input[j];
          yanmie:
            int bb;
/*
            if (result != '\0') {
                if (first_output == 0) {
                    printf("%c", result);
                    first_output = 1;
                } else
                    printf(", %c", result);
            }
*/
        }       // 下一个 j 字符
        /*
           if (N == 1)
           printf("%c", input[0]);
         */
        if (strlen(output) != 0)
            printf("%s", output);
        printf("]\n");
    }
    fclose(fp);
    return 0;
}
