#include <cstdio>
#include <string>
using namespace std;

int get() {
    int x;
    scanf("%d",&x);
    return x;
}

string gets() {
    char aoeu[1000];
    scanf("%s",aoeu);
    return aoeu;
}

int main() {
    int n = get();
    for(int k=0;k<n;k++) {
        string board[4];
        for(int i=0;i<4;i++) {
            board[i] = gets();
        }
        int di[]={1,1,1,0};
        int dj[]={-1,0,1,1};
        bool complete = true;
        for(int i=0;i<4;i++) for(int j=0;j<4;j++) for(int kk=0;kk<4;kk++) {
            if (board[i][j]=='.')complete=false;
            char players[]="XO";
            for(int player=0;player<2;player++) {
                int amount=0;
                for(int a=0;a<4;a++) {
                    int ii=i+a*di[kk];
                    int jj=j+a*dj[kk];
                    if (ii>=0&&jj>=0&&ii<4&&jj<4) {
                        if (board[ii][jj]=='T'||board[ii][jj]==players[player]) amount++;
                    }
                }
                if(amount==4) {
                    printf("Case #%d: %c won\n",k+1,players[player]);
                    goto next_case;
                }
            }
        }
        if (complete) printf("Case #%d: Draw\n",k+1);
        else printf("Case #%d: Game has not completed\n",k+1);
next_case:
        ;
    }
    return 0;
}
