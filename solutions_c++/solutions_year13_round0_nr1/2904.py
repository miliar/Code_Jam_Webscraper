#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <string>
#include <cstring>
#define MID(x,y) ((x+y)>>1)
#define mem(a,b) memset(a,b,sizeof(a))
using namespace std;

typedef long long LL;
const int sup = 0x7fffffff;
const int inf = -0x7fffffff;

char ch[4][4];

bool judge(char c){
    for (int i = 0; i < 4; i ++){
        bool res = true;
        for (int j = 0; j < 4; j ++)
            if (ch[i][j] == (c == 'X'?'O':'X') || ch[i][j] == '.'){
                res = false;
                break;
            }
        if (res)
            return true;
    }
    for (int j = 0; j < 4; j ++){
        bool res = true;
        for (int i = 0; i < 4; i ++)
            if (ch[i][j] == (c == 'X'?'O':'X') || ch[i][j] == '.'){
                res = false;
                break;
            }
        if (res)
            return true;
    }
    bool res = true;
    for (int i = 0; i < 4; i ++){
        if (ch[i][i] == (c == 'X'?'O':'X') || ch[i][i] == '.'){
            res = false;
            break;
        }
    }
    if (res)
        return true;
    res = true;
    for (int i = 0; i < 4; i ++){
        if (ch[i][3-i] == (c == 'X'?'O':'X') || ch[i][3-i] == '.'){
            res = false;
            break;
        }
    }
    if (res)
        return true;
    return false;
}

bool ch_empty(){
    for (int i = 0; i < 4; i ++)
        for (int j = 0; j < 4; j ++)
            if (ch[i][j] == '.')
                return true;
    return false;
}

int main(){
    int t;
    FILE *fi = fopen("input.txt", "r+");
    FILE *fp = fopen("output.txt", "w+");
    fscanf(fi, "%d", &t);
    for (int cases = 1; cases <= t; cases ++){
        for (int i = 0; i < 4; i ++)
            for (int j = 0; j < 4; j ++)
                fscanf(fi, "%1s", &ch[i][j]);

        if (judge('X')){
            fprintf(fp, "Case #%d: X won\n", cases);
        }
        else if (judge('O')){
            fprintf(fp, "Case #%d: O won\n", cases);
        }
        else if (!ch_empty()){
            fprintf(fp, "Case #%d: Draw\n", cases);
        }
        else{
            fprintf(fp, "Case #%d: Game has not completed\n", cases);
        }
    }
	return 0;
}
