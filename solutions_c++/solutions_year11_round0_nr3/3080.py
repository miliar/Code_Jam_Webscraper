#include <stdio.h>
#include <string.h>
#include <math.h>

#define MAX_BUFF_SIZE 1000

int brother(int *buff, int maxnum)
{
    int sum = 0;
    int i = 1;
    int tmp = 0;
    int n = 0;

    if (maxnum <= 1) {
        return -1;
    }

    tmp = buff[0];

    for (i = 1; i < maxnum; i++) {
        if (tmp < buff[i]) {
            tmp = buff[i];
        }
    }

    n = (int) sqrt(tmp);
    for (int k = n - 1; k >= 0; k--) {
        sum = 0;

        for (i = 0; i < maxnum; i++) {
            sum += (buff[i] >> k);
        }

        if (sum & 1) {
            return -1;
        }

    }

    tmp = buff[0];
    for (i = 1; i < maxnum; i++) {
        if (tmp > buff[i]) {
            tmp = buff[i];
        }
    }

    sum = 0;
    for (i = 0; i < maxnum; i++) {
        sum += buff[i];
    }

    return sum - tmp;
}

int main(int argc, char *argv[])
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

    int tmpbuff[MAX_BUFF_SIZE];
    int T, N;
    int sum = 0;

    fscanf(fp, "%d\n", &T);
    for (int i = 0; i < T; i++) {
        fscanf(fp, "%d", &N);

        for (int j = 0, k = 0; j < N; k = j, j++) {
            fscanf(fp, " %d", &tmpbuff[j]);
        }
        if ((sum = brother(tmpbuff, N)) < 0) {
            printf("Case #%d: NO\n", i + 1);
        } else {
            printf("Case #%d: %d\n", i + 1, sum);
        }
    }
    fclose(fp);
    return 0;
}
