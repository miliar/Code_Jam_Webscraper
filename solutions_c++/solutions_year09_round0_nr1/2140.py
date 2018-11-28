/* 
 * File:   main.cpp
 * Author: daricque
 *
 * Created on September 2, 2009, 10:10 PM
 */
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <string>
#include <vector>

/*
 * 
 */
using namespace std;
int L, D, N;
char* word, *w;

void Show(const vector<string>& v) {

    // Vectors "know" how big they are, so you don't have to
    // pass the size separately.

    for (int k = 0; k < v.size(); ++k) {
        cout << "String #" << k << ": " << v[k] << endl;
    }
}

int wordHunt(const vector<string>& word, int pos, const vector<string>& Li) {
    int i, j, k;
    vector<string> FL;
    i = word[pos].length();
    for (j = 0; j < i; j++) {
        for (k = 0; k < Li.size(); k++) {
            if (word[pos][j] == Li[k][pos]) {
                FL.push_back(Li[k]);
            }
        }
    }
    if (pos + 1 == word.size()) {
        return FL.size();
    } else {
        return wordHunt(word, pos + 1, FL);
    }
}

void Display(const vector<string>& v, const vector<string>& Li) {
    vector<string> CL;
    // Vectors "know" how big they are, so you don't have to
    // pass the size separately.
    for (int k = 0; k < v.size(); ++k) {
        int i, j, p;
        CL.clear();
        for (i = 0; i < v[k].length(); i++) {
            if (v[k][i] == '(') {
                for (j = i + 1; v[k][j] != ')'; j++) {
                }
                CL.push_back(v[k].substr(i + 1, j - i - 1));
                i = j;
            } else {
                CL.push_back(v[k].substr(i, 1));
            }
        }
        p = wordHunt(CL, 0, Li);
        cout << "Case #" << k + 1 << ": " << p << endl;
    }
}

int main(int argc, char** argv) {
    int i;
    vector<string> AL, NL;
    cin >> L;
    cin >> D;
    cin >> N;
    word = new char[2000];
    for (i = 0; i < D; i++) {
        cin >> word;
        AL.push_back(word);
    }
    for (i = 0; i < N; i++) {
        cin >> word;
        NL.push_back(word);
    }
    //Display (AL,AL);
    Display(NL, AL);
    /*
     * cout << AL[0][1] << endl;
     * cout << word << "\n" << L << D << N << "\n";
     * return (EXIT_SUCCESS);
     */
}

