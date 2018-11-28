/* 
 * File:   main.cpp
 * Author: Administrator
 *
 * Created on 2010年5月22日, 上午9:11
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
#include <stdio.h>
#include <string.h>
using namespace std;
/*
 * 
 */
char initArray[50][50];
char rotateArray[50][50];
int mask[50][50];
//inline bool verticallyCheck(int N, int K, char ele);

int main(int argc, char** argv) {
    char* input = "A-small-attempt3.in";
    ifstream ifs(input);
    char* output = "output.out";
    ofstream ofs(output);
    int T, N, K;
    int i, j;
    char c;
    ifs >> T;
    int count = 0;
    while (T-- > 0) {
        count++;
        if (count > 1) {
            ofs << "\n";
        }
        ifs >> N;
        ifs >> K;
        int cursor = 0;
        int num = N*N;
        while (cursor < num) {
            ifs >> c;
            initArray[cursor / N][cursor % N] = c;
            cursor++;
        }
        //rotate
        for (i = 0; i < N; i++) {
            for (j = 0; j < N; j++) {
                rotateArray[i][j] = '.';
            }
        }
        for (i = N - 1; i >= 0; i--) {
            //find first index, which is not '*'
            int m = N - 1;
            for (j = N - 1; j >= 0; j--) {
                if (initArray[i][j] != '.') {
                    rotateArray[m][N - 1 - i] = initArray[i][j];
                    m--;
                }
            }
        }
        //find K pieces
        bool isRed = false, isBlue = false;
        int redNum, blueNum;
        //vertically
        for (j = 0; j < N; j++) {
            if (rotateArray[N - 1][j] == '.') {
                continue;
            }
            redNum = 0;
            blueNum = 0;
            for (i = N - 1; i >= 0; i--) {
                if (rotateArray[i][j] == '.') {
                    break;
                } else if (rotateArray[i][j] == 'R') {
                    blueNum = 0;
                    redNum++;
                    if (redNum == K) {
                        isRed = true;
                    }
                } else {
                    redNum = 0;
                    blueNum++;
                    if (blueNum == K) {
                        isBlue = true;
                    }
                }
            }
        }
        //horizontal
        if (isRed == false || isBlue == false) {
            for (i = 0; i < N; i++) {
                redNum = 0;
                blueNum = 0;
                for (j = 0; j < N; j++) {
                    if (rotateArray[i][j] == '.') {
                        redNum = 0;
                        blueNum = 0;
                    } else if (rotateArray[i][j] == 'R') {
                        blueNum = 0;
                        redNum++;
                        if (redNum == K) {
                            isRed = true;
                        }
                    } else {
                        redNum = 0;
                        blueNum++;
                        if (blueNum == K) {
                            isBlue = true;
                        }
                    }
                }
            }
        }

        //diagonally
        int m, n;
        if (isRed == false || isBlue == false) {
            for (i = 0; i < N; i++) {
                for (j = 0; j < N; j++) {
                    if (rotateArray[i][j] != '.') {
                        break;
                    }
                }
                if (j == N) {
                    continue;
                }
                while (j < N) {
                    //left down
                    m = i;
                    n = j;
                    redNum = 0;
                    blueNum = 0;
                    for (; m < N && n >= 0; m++, n--) {
                        if (rotateArray[m][n] == '.') {
                            redNum = 0;
                            blueNum = 0;
                        } else if (rotateArray[m][n] == 'R') {
                            blueNum = 0;
                            redNum++;
                            if (redNum == K) {
                                isRed = true;
                            }
                        } else {
                            redNum = 0;
                            blueNum++;
                            if (blueNum == K) {
                                isBlue = true;
                            }
                        }
                    }
                    //right down
                    m = i;
                    n = j;
                    redNum = 0;
                    blueNum = 0;
                    for (; m < N && n < N; m++, n++) {
                        if (rotateArray[m][n] == '.') {
                            redNum = 0;
                            blueNum = 0;
                        } else if (rotateArray[m][n] == 'R') {
                            blueNum = 0;
                            redNum++;
                            if (redNum == K) {
                                isRed = true;
                            }
                        } else {
                            redNum = 0;
                            blueNum++;
                            if (blueNum == K) {
                                isBlue = true;
                            }
                        }
                    }
                    j++;
                }
            }
        }

        if (isRed == false && isBlue == false) {
            ofs << "Case #" << count << ": Neither";
        } else if (isRed == true && isBlue == true) {
            ofs << "Case #" << count << ": Both";
        } else if (isRed == false && isBlue == true) {
            ofs << "Case #" << count << ": Blue";
        } else {
            ofs << "Case #" << count << ": Red";
        }
    }
    return (EXIT_SUCCESS);
}

