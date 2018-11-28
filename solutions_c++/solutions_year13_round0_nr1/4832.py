#include<cstdio>

int noc;
int map[4][4];

int readNextChar(){
    char ch;
    while (true){
        scanf("%c",&ch);
        if (ch=='X'){
            return 1;
        } else if (ch=='O'){
            return 2;
        } else if (ch=='.'){
            return 0;
        } else if (ch=='T'){
            return 3;
        }
    }
}

inline bool check(int value,int sx,int sy,int dx,int dy){
#define CK0(x,y,v) ((map[x][y]&(v))==(v))
    return CK0(sx,sy,value) && CK0(sx+dx,sy+dy,value) && CK0(sx+dx+dx,sy+dy+dy,value) && CK0(sx+dx+dx+dx,sy+dy+dy+dy,value);
#undef CK0
}

int main(){
    scanf("%d",&noc);
    for (int tnoc=1;tnoc<=noc;++tnoc){
        bool empty = false;
        for (int i=0;i<4;++i){
            for (int j=0;j<4;++j){
                map[i][j] = readNextChar();
                empty |= (map[i][j]==0);
            }
        }
        bool res1 = check(1,0,0,1,1) || check(1,3,0,-1,1);
        bool res2 = check(2,0,0,1,1) || check(2,3,0,-1,1);
        for (int i=0;i<4;++i){
            res1 |= check(1,i,0,0,1);
            res2 |= check(2,i,0,0,1);
            res1 |= check(1,0,i,1,0);
            res2 |= check(2,0,i,1,0);
        }
        fprintf(stdout,"Case #%d: ",tnoc);
        if (res1){
            fprintf(stdout,"X won\n");
        } else if (res2){
            fprintf(stdout,"O won\n");
        } else if (empty){
            fprintf(stdout,"Game has not completed\n");
        } else {
            fprintf(stdout,"Draw\n");
        }
    }
    return 0;
}
