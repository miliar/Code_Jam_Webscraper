#include <cstdio>
#include <cstdlib>
#include <fstream>

FILE * fin = fopen ("B-small-attempt3.in", "r");

#include "../../my own library/big_decimal.h"
using namespace LY;

ofstream fout ("B-small.out");

template <typename _Tp>
_Tp GCD (const _Tp &a, const _Tp &b){
    _Tp s, t;
    s = a;
    t = b;
    if (s > t){
        _Tp tmp = s;
        s = t;
        t = tmp;
    }
    while (!(t == 0)){
        _Tp tmp = t;
        t = s % t;
        s = tmp;
    }
    return s;
}

void work (){
    int n;
    char str[100];
    unsign_big_int s[1000];
    unsign_big_int T = 0;
    fscanf (fin, "%d%c", &n, &s[0]);
    for (int i = 0; i < n; i ++){
        char c;
        fscanf (fin, "%c", &c);
        int j = 0;
        while (c != ' ' && c != '\n'){
            str[j] = c;
            j ++;
            fscanf (fin, "%c", &c);
        }
        str[j] = 0;
        s[i] = str;
        if (i > 0){
            unsign_big_int tmp;
            if (s[i] > s[i - 1]) tmp = s[i] - s[i - 1];
            else tmp = s[i - 1] - s[i];
            if (T == 0) T = tmp;
            T = GCD<unsign_big_int> (T, tmp);
        }
    }
    if (s[0] % T == 0){
        fout << "0\n";
        return;
    }
    unsign_big_int y = T - s[0] % T;
    fout << y << endl;
    return;
}

int main (){
    int N;
    fscanf (fin, "%d", &N);
    for (int i = 0; i < N; i ++){
        fout << "Case #" << i + 1 << ": ";
        work ();
    }
    return 0;
}
