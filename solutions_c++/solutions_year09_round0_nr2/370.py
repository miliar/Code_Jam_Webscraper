// Watersheds.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <cstdio>
#include <cstdlib>
#include <cassert>
#include <queue>
int T,H,W;

int map[100][100];

int flow[100][100];

int color[100][100];

int dx[] = {-1, 0, 0, 1};
int dy[] = {0, -1, 1, 0};

int trans[26];
int count;
FILE *input;
FILE *output;
void init() {
    fscanf(input, "%d", &H);
    fscanf(input, "%d", &W);
    for (int i = 0; i < H; i++) 
        for (int j = 0; j < W; j++) 
           fscanf(input, "%d", &map[i][j]);
}
void calcflow() {
    for (int i = 0; i < H; i++) 
        for (int j = 0; j < W; j++) {
            int mini = 20000;
            int dir = -1;
            for (int k = 0; k < 4; k++) {
                int x = i + dx[k];
                int y = j + dy[k];
                if (x >= 0 && x < H && y >= 0 && y < W)
                    if (map[x][y] < map[i][j] && map[x][y] < mini) {
                        mini = map[x][y];
                        dir = k;
                    }
            }
            flow[i][j] = dir;
        }
}
void floodfill(int x, int y, int label) {
    std::queue<int> xqueue;
    std::queue<int> yqueue;
    xqueue.push(x);
    yqueue.push(y);
    while (!xqueue.empty()) {
        int xx = xqueue.front();
        int yy = yqueue.front();
        xqueue.pop();
        yqueue.pop();
        color[xx][yy] = label;
        for (int k = 0; k < 4; k ++) {
            int nx = xx + dx[k];
            int ny = yy + dy[k];
            if (nx >= 0 && nx < H && ny >= 0 && ny < W) {
                if (color[nx][ny] == -1 && flow[nx][ny] + k == 3) {
                    xqueue.push(nx);
                    yqueue.push(ny);
                }
            }
        }
    }
}

void flood() {
    count = 0;
    for (int i = 0; i < H; i++)
        for (int j = 0; j <  W; j++) {
            color[i][j] = -1;
        }
    for (int i = 0; i < H; i++)
        for (int j = 0; j <  W; j++)
            if (flow[i][j] == -1) {
                assert(color[i][j] == -1);
                floodfill(i,j,count);
                count ++;
            }
    assert(count <= 26);

}
void print(int ith) {
    for (int i = 0; i < count ; i++)
        trans[i] = -1;
    int ccount = 0;
    for (int i = 0; i < H; i++)
        for (int j = 0; j < W; j++) {
            int label = color[i][j];
            if (trans[label] == -1) {
                trans[label] = ccount;
                ccount ++;
            }
        }
    assert(ccount == count);


    fprintf(output, "Case #%d:\n", ith+1);
    for (int i = 0; i < H; i++) {
        for (int j = 0; j < W-1; j++) {
            fprintf(output, "%c ", (char) ('a' + trans[color[i][j]]));
        }
        fprintf(output, "%c\n", (char) ('a' + trans[color[i][W-1]]));
    }

    
}
int main(int argc, char* argv[])
{
    input = fopen("D:\\B-large.in", "r");
    output = fopen("D:\\B-large.out", "w");

    fscanf(input, "%d", &T);
    for (int i = 0; i < T; i++) {
        init();
        calcflow();
        flood();
        print(i);
    }
	return 0;
}

