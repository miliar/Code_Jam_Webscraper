#include <fstream>
#include <string>

using namespace std;

ifstream fin("input.txt");
ofstream fout("output.txt");

const int n= 4;

string s[n];

void check(){
    for (int i= 0; i<n; ++i){
        int o= 0, x= 0;
        for (int j= 0; j<n; ++j){
            if (s[i][j]=='O'){
                ++o;
            }else if (s[i][j]=='X'){
                ++x;
            }else if (s[i][j]=='T'){
                ++o;
                ++x;
            }
        }
        if (o==n){
            fout<<"O won\n";
            return;
        }else if (x==n){
            fout<<"X won\n";
            return;
        }
        o= 0; x= 0;
        for (int j= 0; j<n; ++j){
            if (s[j][i]=='O'){
                ++o;
            }else if (s[j][i]=='X'){
                ++x;
            }else if (s[j][i]=='T'){
                ++o;
                ++x;
            }
        }
        if (o==n){
            fout<<"O won\n";
            return;
        }else if (x==n){
            fout<<"X won\n";
            return;
        }
    }
    int o= 0, x= 0;
    for (int i= 0; i<n; ++i){
        if (s[i][i]=='O'){
            ++o;
        }else if (s[i][i]=='X'){
            ++x;
        }else if (s[i][i]=='T'){
            ++o;
            ++x;
        }
    }
    if (o==n){
        fout<<"O won\n";
        return;
    }else if (x==n){
        fout<<"X won\n";
        return;
    }

    o= 0; x= 0;
    for (int i= 0; i<n; ++i){
        if (s[i][n-i-1]=='O'){
            ++o;
        }else if (s[i][n-i-1]=='X'){
            ++x;
        }else if (s[i][n-i-1]=='T'){
            ++o;
            ++x;
        }
    }
    if (o==n){
        fout<<"O won\n";
        return;
    }else if (x==n){
        fout<<"X won\n";
        return;
    }
    for (int i= 0; i<n; ++i){
        for (int j= 0; j<n; ++j){
            if (s[i][j]=='.'){
                fout<<"Game has not completed\n";
                return;
            }
        }
    }
    fout<<"Draw\n";
}

int main(){
    int nt;
    fin>>nt;
    for (int ct= 1; ct<=nt; ++ct){
        for (int i= 0; i<n; ++i){
            fin>>s[i];
        }
        fout<<"Case #"<<ct<<": ";
        check();    
    }
    return 0;
}
