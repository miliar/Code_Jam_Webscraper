#include <cstdio>
#include <cstdlib>
#include <string>
#include <iostream>
using namespace std;

int T, H, W;
int **alts;
char **flows;
int **labels;
char mark[27];
bool used[27];

int which_way(int a, int b, int c, int d, int self) {
    int min = a;
    if (b < min) min = b;
    if (c < min) min = c;
    if (d < min) min = d;
    if (min >= self) return 0;
    if (a == min) return 1;
    if (b == min) return 2;
    if (c == min) return 3;
    if (d == min) return 4;
}

void fill(int i, int j, int counter) {
     labels[i][j] = counter;
     if ((i>0) && (flows[i-1][j] == 's')) fill(i-1,j,counter);
     if ((i<H-1) && (flows[i+1][j] == 'n')) fill(i+1,j,counter);
     if ((j>0) && (flows[i][j-1] == 'e')) fill (i,j-1,counter);
     if ((j<W-1) && (flows[i][j+1] == 'w')) fill (i,j+1,counter);
}

int main() {
    scanf("%d\n", &T);
    for (int z=1; z<=T; z++) {
        scanf("%d %d\n", &H, &W);
        alts = new int*[H];
        flows = new char*[H];
        labels = new int*[H];
        for (int i=0; i<H; i++) {
            alts[i] = new int[W];
            flows[i] = new char[W];
            labels[i] = new int[W];
        }
        for (int i=0; i<H; i++)
            for (int j=0; j<W; j++)
                scanf("%d", &alts[i][j]);
        
        printf("Case #%d:\n", z);
        
        for (int i=0; i<H; i++)
            for (int j=0; j<W; j++) {
                int a,b,c,d;
                if (i == 0) a = 20000; else a = alts[i-1][j];
                if (j == 0) b = 20000; else b = alts[i][j-1];
                if (j == W-1) c = 20000; else c = alts[i][j+1];
                if (i == H-1) d = 20000; else d = alts[i+1][j];
                int result = which_way(a,b,c,d,alts[i][j]);
                if (result == 0) flows[i][j] = 'c';
                else if (result == 1) flows[i][j] = 'n';
                else if (result == 2) flows[i][j] = 'w';
                else if (result == 3) flows[i][j] = 'e';
                else flows[i][j] = 's';
            }
        
        int counter = 0;
        for (int i=0; i<H; i++)
            for (int j=0; j<W; j++) {
                if (flows[i][j] == 'c') {
                   counter++;
                   fill(i,j,counter);
                }
            }
        
        char* letters = " abcdefghijklmnopqrstuvwxyz";
        for (int i=1; i<27; i++) used[i] = false;
        
        int next = 1;
        for (int i=0; i<H; i++)
            for (int j=0; j<W; j++) {
                int x = labels[i][j];
                if (used[x] == false) {
                   used[x] = true;
                   mark[x] = next;
                   next++;
                }
            }
        
        for (int i=0; i<H; i++) {
            for (int j=0; j<W; j++) printf("%c ", letters[mark[labels[i][j]]]);
            printf("\n");
        }
        delete alts;
        delete flows;
        delete labels;   
    }
}
