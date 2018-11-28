/*
 * File:   qual2008.cpp
 * Author: eastzone
 *
 * Created on 2009年9月2日, 下午1:33
 */

#include <stdlib.h>
#include <iostream>
#include <string>
#include <list>
#include <fstream>
using namespace std;

/*
 *
 */
char search_word[20]="welcome to code jam";
char test_word[500];

int process(int search_start_pos, int test_start_pos){
    int i = search_start_pos;
    int j = test_start_pos;

    if(search_word[i] == 0) return 1;
    while(test_word[j]!=search_word[i]){
        j++;
        if(test_word[j]==0) return 0;
    }
    return process(i, j+1) + process(i+1,j+1);
}

int main(int argc, char** argv) {

    ifstream in_file;
    ofstream out_file;
    in_file.open("A-small-practice.in");
    out_file.open("A-small-practice.out");
    int N;
    char result[5];
    in_file >> N;
    int number = 0;
    in_file.getline(test_word,500);
    for(int i = 0; i < N; i++){
        for(int j=0; j<500;j++) test_word[j]= 0;
        in_file.getline(test_word,500);
        //Process Here
        number = process(0,0);
        sprintf(result, "%04d", number);
        cout << test_word << ":"<< result <<"\n";
        out_file << "Case #"<<i+1<<": "<< result <<"\n";
    }

    in_file.close();
    out_file.close();
    return (EXIT_SUCCESS);
}

