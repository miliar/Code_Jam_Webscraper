/* 
 * File:   main.cpp
 * Author: daricque
 *
 * Created on September 3, 2009, 5:12 AM
 */
#include <stdio.h>
#include <stdlib.h>
#include <iostream>
#include <vector>
#define WIDTH 105
#define HEIGHT 105

/*
 * 
 */
using namespace std;

int LETTER = 96;

void fill (int T[][WIDTH]) {
    for (int k = 0; k < HEIGHT; ++k) {
        for (int j = 0; j < WIDTH; j++) {
            T[k][j] = -1;
        }
    }
}

void fill (char T[][WIDTH]) {
    for (int k = 0; k < HEIGHT; ++k) {
        for (int j = 0; j < WIDTH; j++) {
            T[k][j] = 96;
        }
    }
}

void Show(int T[][WIDTH]) {
    for (int k = 0; k < HEIGHT; ++k) {
        cout << "Line #" << k << ": ";
        for (int j = 0; j < WIDTH; j++) {
            cout << T[k][j] << " ";
        }
        cout << endl;
    }
}

void Show(char T[][WIDTH],int H, int W) {
    for (int k = 0; k < H; ++k) {
        //cout << "Line #" << k << ": ";
        for (int j = 0; j < W; j++) {
            cout << T[k][j] << " ";
        }
        cout << endl;
    }
}

int is_basins(int T[][WIDTH], int k, int m, char B[][WIDTH], int H, int W) {
    //cout << "ENTRANDO: k,m,h,w e B[k][m] " << k << "," << m << "," << H << "," << W << " e " << B[k][m] << endl;
    if (B[k][m] != 96) return B[k][m];
    int n,s,we,e,low=10001,q,p,r;
    //Show (B,H,W);
    //cout << "LOW " << low << endl;
    if (k>0) {
        n = T[k-1][m];
        low = n;
        q=0;
    }
    if (m>0) {
        we = T[k][m-1];
        if (we<low) {
            low = we;
            q=1;
        }
    }
    if (m<W-1) {
        e = T[k][m+1];
        if (e<low) {
            low = e;
            q=2;
        }
    }
    if (k<H-1) {
        s = T[k+1][m];
        if (s<low) {
            low = s;
            q=3;
        }
    }
    //cout << "LOW " << low << endl;
    //cout << T[k][m] << " <= " << low << " Q " << q<<endl;
    if (T[k][m]<=low) {
        if (B[k][m] == 96) {
            LETTER++;
            B[k][m] = LETTER;
        }
        //cout << B[k][m] << " <= " << LETTER << " K e M " << k << " " << m <<endl;
    } else { 
        p = k;
        r = m;
        switch (q) {
            case 0: p = k-1; break;
            case 1: r = m-1; break;
            case 2: r = m+1; break;
            case 3: p = k+1; break;
        }
        //cout << B[k][m] << " <= " << LETTER << " P e R " << p << " " << r <<endl;
        B[k][m] = is_basins(T,p,r,B,H,W);
        //cout << "VOLTOU " << is_basins(T,p,r,B,H,W) << endl;
        //Show (B,H,W);
    }
    //Show (B,H,W);
    return (B[k][m]);
}

int main(int argc, char** argv) {
    int T[HEIGHT][WIDTH];
    char B[HEIGHT][WIDTH];
    int i,j,H,W,k,m,*n;
    //B[0][0] = 97;
    //cout << B[0][0] << endl;
    cin >> i;
    for (j=0;j<i;j++) {
        fill(T);
        fill(B);
        LETTER = 96;
        cin >> H;
        cin >> W;
        //Show (B,H,W);
        for (k=0; k<H; k++) {
            for (m=0;m<W;m++) {
                cin >> T[k][m];
                //if (m==0)
            }
            //T.push_back(n);
        }
        //cout << "SAIU DO FORNO ASSIM:\n";
        //Show(T);
        for (k=0;k<H;k++) {
            for (m=0;m<W;m++) {
                if (B[k][m] == 96) B[k][m] = is_basins(T,k,m,B,H,W);
            }
        }
        cout << "Case #" << j+1 << ":" << endl;
        Show (B,H,W);
        //T.clear();
    }
    return (EXIT_SUCCESS);
}

