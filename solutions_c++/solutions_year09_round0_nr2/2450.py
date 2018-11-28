#include <iostream>
#include <fstream>

using namespace std;

ifstream in("B-large.in");
ofstream out("B-large.out");

int H, W;
int *map;
char *drain;

char solver(int x, int y) {
    //out << drain[y*W+x] << " " << x << " " << y << endl;
    if(drain[y*W+x]=='0') {
        int min, min_x, min_y;
        min_x = x;
        min_y = y;
        min = map[y*W+x];
        if(y>0 && min > map[(y-1)*W+x]) {
            min = map[(y-1)*W+x];
            min_x = x;
            min_y = y-1;
        }
        if(x>0 && min > map[y*W+x-1]) {
            min = map[y*W+x-1];
            min_x = x-1;
            min_y = y;
        }
        if(x<W-1 && min > map[y*W+x+1]) {
            min = map[y*W+x+1];
            min_x = x+1;
            min_y = y;
        }
        if(y<H-1 && min > map[(y+1)*W+x]) {
            min = map[(y+1)*W+x];
            min_x = x;
            min_y = y+1;
        }
        drain[y*W+x] = solver(min_x, min_y);
    }
    return drain[y*W+x];
}

void replace(char a, char b) {
    int i, j;
    for(i=0; i<H; i++)
        for(j=0; j<W; j++)
            if(drain[i*W+j]==a)
                drain[i*W+j] = b;
}

int main() {
    int T, i, j, k;
    char label, l, t;
    in >> T;
    int* maps[T];
    int dim[T][2];
    for(i=0; i<T; i++) {
        in >> H >> W;
        dim[i][0] = H; dim[i][1] = W;
        maps[i] = new int[H*W];
        for(j=0; j<H; j++)
            for(k=0; k<W; k++)
                in >> maps[i][j*W+k];
    }
    for(i=0; i<T; i++) {
        label = '1';
        H = dim[i][0];
        W = dim[i][1];
        map = new int[H*W];
        drain = new char[H*W];
        for(j=0; j<H; j++) {
            for(k=0; k<W; k++) {
                map[j*W+k] = maps[i][j*W+k];
                drain[j*W+k] = '0';
            }
        }
        for(k=0; k<W; k++) {
            for(j=0; j<H; j++) {
                if(j>0 && map[j*W+k] > map[(j-1)*W+k])
                    continue;
                if(j<H-1 && map[j*W+k] > map[(j+1)*W+k])
                    continue;
                if(k>0 && map[j*W+k] > map[j*W+k-1])
                    continue;
                if(k<W-1 && map[j*W+k] > map[j*W+k+1])
                    continue;
                drain[j*W+k] = label;
                label++;
            }
        }
        for(j=0; j<H; j++)
            for(k=0; k<W; k++)
                if(drain[j*W+k]=='0')
                    drain[j*W+k] = solver(k,j);

        label = 'a';
        l = '0';

        for(j=0; j<H; j++) {
            for(k=0; k<W; k++) {
               if(drain[j*W+k] != l && (drain[j*W+k] < 'a' || drain[j*W+k] > 'z')) {
                    l = drain[j*W+k];
                    replace(l, label);
                    label++;
               }
            }
        }
        out << "Case #" << i+1 << ":" << endl;
        for(j=0; j<H; j++) {
            for(k=0; k<W; k++)
                out << drain[j*W+k] << " ";
            out << endl;
        }
        delete[] map;
        delete[] drain;
    }
    in.close();
    out.close();
    return 0;
}
