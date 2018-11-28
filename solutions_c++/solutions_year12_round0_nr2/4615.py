/*
 * Google Code Jam
 *
 * Created on: 14/04/2012
 * Author: MLK
 *
 * Qualification Round 2012
 * Problem B. Dancing With the Googlers
 * https://code.google.com/codejam/contest/1460488/dashboard#s=p1
 *
 */

#include <cstdio>
#include <iostream>
#include <string>
#include <cmath>

using namespace std;

int main(int argc, char **argv) {

    FILE * input = fopen("input.txt", "r");
    int nTestCases;
    fscanf(input, "%d\n", &nTestCases);

    // For each test case
    for (int t = 1; t <= nTestCases; t++) {
        int nGooglers;
        int nSurprising;
        int targetScore;
        int answer = 0; // maximum number of Googlers that could have had a best result of at least targetScore
        int usedSurprising = 0;
        fscanf(input, "%d %d %d", &nGooglers, &nSurprising, &targetScore);

        for (int i = 0; i < nGooglers; ++i) {
            int score;
            fscanf(input, "%d", &score);

            int mean = score / 3;
            int remainder = score % 3;
            int maxScore = mean;
            if (remainder > 0) {
                maxScore = mean + 1;
            }
            if (maxScore >= targetScore) {
                answer++;
            } else if (usedSurprising < nSurprising) {
                if ((remainder == 0 && mean > 0)|| remainder == 2) {
                    if (targetScore == maxScore + 1) {
                        usedSurprising++;
                        answer++;
                    }
                }
            }
        }

        cout << "Case #" << t << ": " << answer << endl;
    }

    fclose(input);
    return 0;
}

