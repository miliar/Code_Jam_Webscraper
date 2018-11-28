#include <iostream>
#include <fstream>

using namespace std;

#define MAX 101

int MAP[MAX][MAX];
char B[MAX][MAX];

int lblMax;

int getMin(int x, int y, int &tx, int &ty, int H, int W){
    int min = -1;
    if(x-1 >= 0 && MAP[x-1][y] < MAP[x][y]){
        min = MAP[x-1][y];
        tx = x-1, ty = y;
    }
    if(y-1 >=0 && MAP[x][y-1] < MAP[x][y]){
        if((min < 0) || (min >= 0 && MAP[x][y-1] < min)){
            min = MAP[x][y-1];
            tx = x, ty = y-1;
        }
    }
    if(y+1 < W && MAP[x][y+1] < MAP[x][y]){
        if((min < 0) || (min >= 0 && MAP[x][y+1] < min)){
            min = MAP[x][y+1];
            tx = x, ty = y+1;
        }
    }
    if(x+1 < H && MAP[x+1][y] < MAP[x][y]){
        if((min < 0) || (min >= 0 && MAP[x+1][y] < min)){
            min = MAP[x+1][y];
            tx = x+1, ty = y;
        }
    }
    
    return min;
}

char backTrack(int x, int y, int H, int W){
    char label;
    if(B[x][y] >= 'a' && B[x][y] <= 'z'){
        return B[x][y];
    }
    int tx, ty;
    if(getMin(x, y, tx, ty, H, W) < 0){
        // set a new character and return
        lblMax;
        B[x][y] = 'a'+lblMax;
        return 'a'+lblMax++;

    }
    else {
        label = backTrack(tx, ty, H, W);
        B[x][y] = label;
        return label;
    }
}

int main(){
    ifstream fin("B-large.in");
    ofstream fout("B-large-out.out");

    int T, H, W;
    
    fin >> T;

    for(int i=1; i <= T; i++){
        fin >> H >> W;
        lblMax =0;

        for(int j=0; j < H; j++)
            for(int k=0; k < W; k++) {
                fin >> MAP[j][k];
                B[j][k] = '-';
            }

        for(int j=0; j < H; j++)
            for(int k=0; k < W; k++){
                if(B[j][k]=='-') backTrack(j, k, H, W);       
            }

        fout << "Case #" << i << ":" << endl;

        for(int j=0; j < H; j++){
            for(int k=0; k < W; k++){
                fout << B[j][k];
                if(k == W-1) fout << endl;
                else fout << " ";
            }
        }
    }
    
    return 0;
}