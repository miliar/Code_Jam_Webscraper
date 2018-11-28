/* 
 * File:   main.cpp
 * Author: frox
 *
 * Created on April 14, 2012, 1:48 PM
 */

#include <cstdlib>
#include <string>
#include <fstream>
#include <iostream>
#include <time.h>

using namespace std;

/*
 * 
 */
char charMap[10000];

void createCharMap(string& google, string& english) {
    int i;
    int len = google.length();
    for (i = 0; i < len; i++) {
        charMap[google[i]] = english[i];
    }
}

void googleToEnglish(string google) {
    int i;
    int len = google.length();
    string english;
    for (i = 0; i < len; i++) {
        english[i] = charMap[google[i]];
        cout << english[i];
    }
    cout << endl;
}

int main(int argc, char** argv) {
    int i;
    for (i = 'a'; i <= 'z'; i++)charMap[i] = 'X';
    charMap[' '] = ' ';
    charMap['\n'] = '\n';
    charMap['q']='z';
    charMap['z']='q';
    ifstream inFile("/home/frox/Dropbox/Dropbox/private/Codejam/CODEJAM_1A/sample", ios::in);
    string google;
    string english;
    getline(inFile, google);
    getline(inFile, english);
    createCharMap(google, english);
    getline(inFile, google);
    getline(inFile, english);
    createCharMap(google, english);
    getline(inFile, google);
    getline(inFile, english);
    createCharMap(google, english);

    //for (i = 'a'; i <= 'z'; i++)cout << charMap[i];
    inFile.close();
    inFile.open("/home/frox/Dropbox/Dropbox/private/Codejam/CODEJAM_1A/real_test", ios::in);
    getline(inFile, google);
    int cases;
    cases = atoi(google.c_str());
    for (i = 1; i <= cases; i++) {
        getline(inFile, google);
        cout << "Case #" << i << ": ";
        googleToEnglish(google);
    }

    //cout << line << endl;
    return 0;
}

