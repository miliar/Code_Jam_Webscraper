#include <cstdio>
#include <iostream>
#include <string>
#include <fstream>

using namespace std;

#define DEBUGFILE "debug.txt"

#define INFILE "A-small-attempt0.in"
#define OUTFILE "out.txt"

#define DATA 10000

void sortSmall(float data[DATA], int num) {
    for (int i = 0; i < num-1; i++) {
        for (int j = i; j < num; j++) {
            if (data[i] > data[j]) {
                float temp = data[i];
                data[i] = data[j];
                data[j] = temp;
            }
        }
    }
}

void sortLarge(float data[DATA], int num) {
    for (int i = 0; i < num-1; i++) {
        for (int j = i; j < num; j++) {
            if (data[i] < data[j]) {
                float temp = data[i];
                data[i] = data[j];
                data[j] = temp;
            }
        }
    }
}

int main () {
    ofstream debug(DEBUGFILE);

    freopen(INFILE, "rt", stdin);
    freopen(OUTFILE, "wt", stdout);

    int T = 0;
    int count = 1;
    float result = 0;
    int num = 0;

    float data1[DATA];
    float data2[DATA];

    scanf("%i", &T);

    while (T) {
        float temp;
        scanf("%i", &num);
        for (int i = 0; i < num; i++) {
            scanf("%f", &temp);
            data1[i] = temp;
        }
        for (int i = 0; i< num; i++) {
            scanf("%f", &temp);
            data2[i] = temp;
        }
        sortSmall(data1, num);
        sortLarge(data2, num);
        float temp2 = 0;
        for (int i = 0; i< num; i++) {
            temp2 = data1[i]*data2[i] + temp2;
        }
        result = temp2;
        printf("Case #%i: %.0f\n", count, result);
        count++;
        T--;
    }

    fclose(stdin);
    fclose(stdout);
    debug.close();
    return 0;
}
