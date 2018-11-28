#include <iostream>
#include <fstream>
#include <stdlib.h>

using namespace std;

int ** a;

int sum_colume(int n){
    int sum = 0;
    for (int i = 0; i < 4; i++) {
        sum += a[i][n];
    }
    return sum;
}

int sum_row(int n){
    int sum = 0;
    for (int i = 0; i < 4; i++) {
        sum += a[n][i];
    }
    return sum;
}

int sum_diag(int n) {
    int sum = 0;
    for (int i  = 0; i < 4; i++) {
        if (n == 0) sum += a[i][i];
        else sum += a[i][3 - i];
    }
    return sum;
}

int check() {
    for (int i = 0; i < 4; i++) {
        if (sum_row(i) == 4 || sum_row(i) == 13) return 0;
        if (sum_row(i) == -4 || sum_row(i) == 7) return 1;
        if (sum_colume(i) == 4 || sum_row(i) == 13) return 0;
        if (sum_colume(i) == -4 || sum_row(i) == 7) return 1;
    }    
    if (sum_diag(0) == 4 || sum_diag(0) == 13) return 0;
    if (sum_diag(0) == -4 || sum_diag(0) == 7) return 1;
    if (sum_diag(1) == 4 || sum_diag(1) == 13) return 0;
    if (sum_diag(1) == -4 || sum_diag(1) == 7) return 1;
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            if (a[i][j] == 0) return 2;
        }   
    }
    return 3; 
}

int main(){
    ifstream fin;
    ofstream fout;
    fout.open("ouput.out");
    fin.open("A-small-attempt0.in");
    
    int size;
    fin >> size;
    
    a = (int **)malloc(4 * sizeof(int *));
    for (int i = 0; i < 4; i++) {
        a[i] = (int *) malloc(4 * sizeof(int));
    }
    
    
    char x;
    int result;
    int k = 0;
    while (k < size) {
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                fin >> x;
                if (x == 'X') a[i][j] = 1;
                else if (x == 'O') a[i][j] = -1;
                else if (x == 'T') a[i][j] = 10;
                else a[i][j] = 0;
            }
        }
        result = check();
        if (result == 0) fout << "Case #" << (k + 1) << ": " << "X won" << endl;
        if (result == 1) fout << "Case #" << (k + 1) << ": " << "O won" << endl;
        if (result == 2) fout << "Case #" << (k + 1) << ": " << "Game has not completed" << endl;
        if (result == 3) fout << "Case #" << (k + 1) << ": " << "Draw" << endl;        
        k++;
    }
    
    for (int i = 0; i < 4; i++) {
        free (a[i]);
    }
    free(a);
    fout.close();
    fin.close();
    
    return 0;
}
