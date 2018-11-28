/*
 * File:   main.cpp
 * Author: eastzone
 *
 * Created on 2009年9月2日, 下午1:33
 */

#include <stdlib.h>
#include <iostream>
#include <string>
#include <string.h>
#include <list>
#include <fstream>
#include <strstream>
using namespace std;

/*
 *
 */
struct node {
    node* left;
    node* right;
    float weight;
};

int creat_tree(istringstream is){
}

int main(int argc, char** argv) {

    ifstream in_file;
    ofstream out_file;
    fstream temp_file;
    in_file.open("A-small-practice.in");
    out_file.open("A-small-practice.out");

    int N;
    in_file >> N;
    int L, n, A;
    int test_word_length;
    char test_word[500];
    char temp[500];
    char para;
    char character[500][500];
    for(int i = 0; i < N; i++){
        in_file >> L;
        in_file.getline(temp,500);
        test_word[0] = 0;

        for(int j=0; j<L;j++) {
            in_file.getline(temp,500);
            strcat(test_word, temp);
        }
        string mystring(test_word);
        istringstream is(mystring);
        creat_tree(is);

        in_file >> A;
        for(int j=0; j<A;j++) {
            in_file >> temp; //animal name;
            in_file >> n;
            for(int k=0;k<n;k++){
                in_file >> character[k];
            }
        }

        //Process Here
  
        cout << L << test_word <<"\n";
        //out_file << "Case #"<<i+1<<": "<< result <<"\n";
    }

    in_file.close();
    out_file.close();
    return (EXIT_SUCCESS);
}

