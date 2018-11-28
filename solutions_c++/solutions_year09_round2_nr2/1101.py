#include<fstream>
#include<iostream>
#include<algorithm>
#include<string>
using namespace std;

int main(int argc, char *argv[]){
    string one;
    ifstream fin("input.txt");
    ofstream fout("output.txt");
    int N;
    fin >> N;
    for(int i= 1 ; i <= N; i++) {
            fin >> one;
            // Will make sting longer
            one = "0" + one;
            next_permutation(one.begin(), one.end());
            if (one[0] == '0')
               one=one.substr(1);
            fout << "Case #" << i << ": " << one << endl;
    }
    fin.close();
    fout.close();
}
