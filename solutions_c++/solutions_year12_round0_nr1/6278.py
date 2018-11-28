#include <cstdlib>
#include <iostream>
#include <fstream>
#include <cmath>
#include <stdio.h>
#include <sstream>
#include <stack>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, char *argv[])
{
    ifstream fin("A-small-attempt2.in"); 
    ofstream fout("temp.txt"); 
    string root="yhesocvxduiglbkrztnwjpfmaq";
         
    int n;
    fin >> n;
    string input;
    getline(fin,input);
    int count=1;
    while(n--){
        getline(fin,input);
        for(int i=0;i<input.length();i++){
            if(isalpha(input[i])){
                input[i]=root[input[i]-97];
            }
        }
        fout << "Case #" << count << ": ";
        fout << input << endl;
        count++;
    }
    fin.close();
    fout.close();
    return EXIT_SUCCESS;
}
