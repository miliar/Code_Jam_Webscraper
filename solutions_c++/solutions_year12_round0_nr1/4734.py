/*
 * Google Code Jam
 *
 * Created on: 14/04/2012
 * Author: MLK
 *
 * Qualification Round 2012
 * Problem A. Speaking in Tongues
 * https://code.google.com/codejam/contest/1460488/dashboard
 *
 */

#include <cstdio>
#include <iostream>
#include <string>

using namespace std;

int main(int argc, char **argv) {

    string english("abcdefghijklmnopqrstuvwxyz");
    string googlerese("ynficwlbkuomxsevzpdrjgthaq");

    FILE * input = fopen("input.txt", "r");
    int nTestCases;
    fscanf(input, "%d\n", &nTestCases);

    for (int t = 1; t <= nTestCases; t++) {
        char text[120];
        string translatedText;

        fgets(text, 120, input);
        string strText(text);
        for (string::iterator it = strText.begin(); it < strText.end(); it++ ) {
            size_t idx = googlerese.find(*it);
            char c = *it;
            if (idx != string::npos) {
                c = english.at(idx);
            }
            translatedText.append(1,c);
        }
        cout << "Case #" << t << ": " << translatedText;
    }
    return 0;
}

