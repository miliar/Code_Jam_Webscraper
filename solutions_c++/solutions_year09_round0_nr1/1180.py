#include <iostream>
#include <fstream>
#include <string>
using namespace std;

string dictionary[5000];
int L, D, N, letters[15][300];

int get(string s)
{
    memset(letters, 0, sizeof(letters));
    int ind = 0;
    for(int i = 0; i < s.size(); i++){
        if(s[i] == '('){
            while(s[++i] != ')'){
                letters[ind][(int)s[i]]++;
            }
        }
        else{
            letters[ind][(int)s[i]]++;
        }
        ind++;
    }

    int res = 0;
    for(int i = 0; i < D; i++){
        int ok = 1;
        for(int j = 0; j < L; j++){
            ok &= letters[j][(int)dictionary[i][j]];
        }
        res += ok;
    }
    return res;
}

int main()
{
    ifstream fin("A-large.in");
    ofstream fout("A-large.out");
    fin >> L >> D >> N;
    for(int i = 0; i < D; i++){
        fin >> dictionary[i];
    }
    for(int test = 1; test <= N; test++){
        string pattern;
        fin >> pattern;
        fout << "Case #" << test << ": " << get(pattern) << endl;
    }
}
