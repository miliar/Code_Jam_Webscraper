#include <iostream>
#include <fstream>
#include <string.h>
using namespace std;

void flip (char a[]) {
    int l = strlen(a);
    for (int i=0; i<l/2; i++) {
        char tmp;
        tmp = a[i];
        a[i]=a[l-1-i];
        a[l-1-i]=tmp;
    };
};

void drop (char a[]) {
    int l = strlen(a);
    int w=0;
    for (int i=0; i<l; i++) {
        if (a[w]!='.') w++;
        else {
            if (a[i]!='.') {
                a[w]=a[i];
                a[i]='.';
                w++;
            };
        };
    };
};

int winB (char b[][51], int N, int K) {
    int counter;
    int i,j;
    for (i=0; i<N; i++) {
        counter = 0;
        for (j=0; j<N; j++) {
            if (b[i][j]=='B') {
                counter++;
                if (counter==K) return 1;
            } else {
                counter = 0;
            }
        }
    };
    for (j=0; j<N; j++) {
        counter = 0;
        for (i=0; i<N; i++) {
            if (b[i][j]=='B') {
                counter++;
                if (counter==K) return 1;
            } else {
                counter = 0;
            }
        }
    };

    for (i=0; i<2*N; i++) {
        counter = 0;
        for (j=0; j<=i; j++) {
            if (j>=N || (i-j)>=N) continue;
            if (b[j][i-j]=='B') {
                counter++;
                if (counter==K) return 1;
            } else {
                counter = 0;
            }
        }
    }

    for (i=0; i<N; i++) {
        flip(b[i]);
    }

    for (i=0; i<2*N; i++) {
        counter = 0;
        for (j=0; j<=i; j++) {
            if (j>=N || (i-j)>=N) continue;
            if (b[j][i-j]=='B') {
                counter++;
                if (counter==K) return 1;
            } else {
                counter = 0;
            }
        }
    }

    for (i=0; i<N; i++) {
        flip(b[i]);
    }

    return 0;
};

int winR (char b[][51], int N, int K) {
    int counter;
    int i,j;
    for (i=0; i<N; i++) {
        counter = 0;
        for (j=0; j<N; j++) {
            if (b[i][j]=='R') {
                counter++;
                if (counter==K) return 1;
            } else {
                counter = 0;
            }
        }
    };
    for (j=0; j<N; j++) {
        counter = 0;
        for (i=0; i<N; i++) {
            if (b[i][j]=='R') {
                counter++;
                if (counter==K) return 1;
            } else {
                counter = 0;
            }
        }
    };

    for (i=0; i<2*N; i++) {
        counter = 0;
        for (j=0; j<=i; j++) {
            if (j>=N || (i-j)>=N) continue;
            if (b[j][i-j]=='R') {
                counter++;
                if (counter==K) return 1;
            } else {
                counter = 0;
            }
        }
    }

    for (i=0; i<N; i++) {
        flip(b[i]);
    }

    for (i=0; i<2*N; i++) {
        counter = 0;
        for (j=0; j<=i; j++) {
            if (j>=N || (i-j)>=N) continue;
            if (b[j][i-j]=='R') {
                counter++;
                if (counter==K) return 1;
            } else {
                counter = 0;
            }
        }
    }

    for (i=0; i<N; i++) {
        flip(b[i]);
    }

    return 0;
};

int main () {
    int cases, N, K;
    char board[51][51];

    ifstream myfile;
    myfile.open("A-large.in", ios::in);
    myfile >> cases;
    for (int c=1; c<=cases; c++) {
        myfile >> N >> K;
        for (int i=0; i<51; i++) for (int j=0; j<51; j++) board[i][j]=0;
        for (int i=0; i<N; i++) {
            myfile >> board[i];
            flip(board[i]);
            drop(board[i]);
        };
        int b = winB (board, N, K);
        int r = winR (board, N, K);
        if (b&&r) {
            cout << "Case #" << c << ": Both\n";
        } else if (b) {
            cout << "Case #" << c << ": Blue\n";
        } else if (r) {
            cout << "Case #" << c << ": Red\n";
        } else {
            cout << "Case #" << c << ": Neither\n";
        }
    };
    myfile.close();
};
