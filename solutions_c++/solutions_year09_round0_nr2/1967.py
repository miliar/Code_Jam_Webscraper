/* 
 * File:   watersheds.cpp
 * Author: hayoungpark
 *
 * Created on September 2, 2009, 9:45 PM
 */

#include <stdlib.h>
#include <iostream>
#include <fstream>
using namespace std;

ifstream fin("B-large.in");
ofstream fout("B-large.out");

struct cell{
    int nAlti;
    char basin;
    struct cell* flow;
};
char sink(struct cell* path, char* letter);
int main(int argc, char** argv) {
    int T, H, W;
    fin >> T;

    for(int i = 0; i < T; i++) {

        fin >> H;
        fin >> W;

        struct cell* map = new cell[H*W];
        struct cell* current;

        for(int m = 0; m < H; m++) {
            for(int n = 0; n < W; n++) {
                current = map + m*W + n;
                fin >> current->nAlti;
                current->basin = NULL;
                current->flow = current;
            }
        }

        struct cell *neighbor;
        int lowest;

        for(int p = 0; p < H; p++) {
            for(int q = 0; q < W; q++) {
                current = map + p*W + q; //current cell
                lowest = current->nAlti;

                if(p) {
                    neighbor = map + (p-1)*W + q;
                    if(neighbor->nAlti < lowest) { // North
                        lowest = neighbor->nAlti;
                        current->flow = neighbor;
                    }
                }
                if(q) {
                    neighbor = map + p*W + q-1;
                    if(neighbor->nAlti < lowest) { //West
                        lowest = neighbor->nAlti;
                        current->flow = neighbor;
                    }
                }
                if(q < W - 1) {
                    neighbor = map + p*W + q+1;
                    if(neighbor->nAlti < lowest) { //East
                        lowest = neighbor->nAlti;
                        current->flow = neighbor;
                    }
                }
                if(p < H - 1) {
                    neighbor = map + (p+1)*W + q;
                    if(neighbor->nAlti < lowest) { //South
                        lowest = neighbor->nAlti;
                        current->flow = neighbor;
                    }
                }
            }
        }
        char lexi= 'a' - 1;
        
        for(int j = 0; j < H; j++){
            for(int k = 0; k < W; k++) {
                current = map + j*W + k;
                current->basin = sink(current, &lexi);
            }
        }

        fout << "Case #" << i + 1 << ":" << endl;
        for(int r = 0; r < H; r++) {
            for(int s = 0; s < W; s++) {
                fout << (map + r*W + s)->basin << " ";
            }
            fout << endl;
        }
    }
    return 0;
}

char sink(struct cell* path, char* letter){
    if(path->flow != path) {
        path->basin = sink(path->flow, letter);
    }
    else {
        if(path->basin == NULL)
            path->basin = ++*letter;
    }
    return path->basin;
}