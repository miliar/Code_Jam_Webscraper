#include <stdio.h>

FILE *fin, *fout;
int who(char d)
{
    if (d == 'X') return 1;
    else return 2;
}
int process(void)
{
    char board[5][5]={0};
    int i, j;
    const int N = 4;
    char d;
    for (i=0;i<N;++i){
        fscanf(fin, "%s", board[i]);
    }

    //determine win
    for (i=0;i<N;++i){
        //row
        d = board[i][0];
        if (d == 'T') d = board[i][1];
        if (d != '.'){
            for (j=0;j<N;++j){
                if (d != board[i][j] && 'T' != board[i][j]) break;
            }
            if (j==N){
                return who(d);
            }
        }

        d = board[0][i];
        if (d == 'T') d = board[i][1];
        if (d != '.'){
            for (j=0;j<N;++j){
                if (d != board[j][i] && 'T' != board[j][i]) break;
            }
            if (j==N){
                return who(d);
            }
        }
    }
    d=board[0][0];
    if (d == 'T') d = board[1][1];
    if (d != '.'){
        for (i=0;i<N;++i){
            if (d != board[i][i] && 'T' != board[i][i]) break;
        }
        if (i==N){
            return who(d);
        }
    }

    d=board[0][N-1];
    if (d=='T') d=board[1][N-2];
    if (d != '.'){
        for (i=0;i<N;++i){
            if (d!=board[i][N-i-1] && 'T'!= board[i][N-i-1]) break;
        }
        if (i==N){
            return who(d);
        }
    }

    // no one wins
    for (i=0;i<N;++i){
        for (j=0;j<N;++j){
            if (board[i][j]=='.') return 4;
        }
    }

    return 3;
}
int main(void)
{
    int T, t;
    fin = fopen("input.txt", "r");
    fout = fopen("output.txt", "w");
    fscanf(fin, "%d", &T);
    for (t=1;t<=T;++t){
        int res=process();
        fprintf(fout, "Case #%d: ", t);
        switch(res){
        case 1:
            fprintf(fout, "X won");
            break;
        case 2:
            fprintf(fout, "O won");
            break;
        case 3:
            fprintf(fout, "Draw");
            break;
        case 4:
            fprintf(fout, "Game has not completed");
            break;
        }
        fprintf(fout, "\n");
    }
    fclose(fin);
    fclose(fout);
}
