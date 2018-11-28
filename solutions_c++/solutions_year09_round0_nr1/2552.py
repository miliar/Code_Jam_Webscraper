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
char words[5000][15];
char temp_word[1000];
int process(int D, int L){
    char reorg_word[15][100];
    int result=0;
    int i = 0, j=0, k= 0;
    while(temp_word[i]){
        if(temp_word[i] == '('){
            i++;
            while(temp_word[i] != ')'){
                reorg_word[j][k] = temp_word[i];
                k++;
                i++;
            }
            i++;
            reorg_word[j][k] = 0;
            cout << reorg_word[j] <<'\n';
            k = 0;
        }
        else{
            reorg_word[j][0] = temp_word[i];
            reorg_word[j][1] = 0;
            cout << reorg_word[j] <<'\n';
            i++;
        }
        j++;
    }
    for (i=0; i<D; i++){
        for (j=0; j<L; j++){
            for (k=0; reorg_word[j][k]!=0; k++){
                if(reorg_word[j][k]==words[i][j]){
                    break;
                }
            }
            if(reorg_word[j][k]==0) break;
        }
        if(j==L) result ++;
    }
    return result;
}

int main(int argc, char** argv) {

    ifstream in_file;
    ofstream out_file;
    in_file.open("A-small-practice.in");
    out_file.open("A-small-practice.out");
    int L, D, N;
    in_file >> L;
    in_file >> D;
    in_file >> N;
    int number = 0;
    
    for(int i=0; i< D; i++){
        in_file >> words[i];
        cout << words[i] <<"\n";
    }

    for(int i = 0; i < N; i++){
        in_file >> temp_word;
        //Process Here
        number = process(D, L);
        cout << temp_word << ":"<< number <<"\n";
        out_file << "Case #"<<i+1<<": "<<number<<"\n";
    }

    in_file.close();
    out_file.close();
    return (EXIT_SUCCESS);
}

