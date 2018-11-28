#include <cstdio>
#include <cstring>
using namespace std;

char ans[][50] = {"X won","O won", "Draw", "Game has not completed"};
char a[4][4];

inline char getNext(){
    char ch;
    do{
        ch = getchar();
    } while(ch!='.' && ch!='X' && ch!='T' && ch!='O');
    return ch;
}

int totd, totx, toto, tott;
inline void GG(char ch){
    if(ch=='X') totx++;
    if(ch=='O') toto++;
    if(ch=='.') totd++;
    if(ch=='T') tott++;
}

int check(){
    int i, j;
    for(totd=0,i=0;i<4;i++){
        for(totx=0,toto=0,tott=0,j=0;j<4;j++)
            GG(a[i][j]);
        if(totx==4 || totx==3&&tott==1) return 0;
        if(toto==4 || toto==3&&tott==1) return 1;
    }
    int ff = totd;
    for(totd=0,i=0;i<4;i++){
        for(totx=0,toto=0,tott=0,j=0;j<4;j++)
            GG(a[j][i]);
        if(totx==4 || totx==3&&tott==1) return 0;
        if(toto==4 || toto==3&&tott==1) return 1;
    }
    totx=toto=tott=0;GG(a[0][0]),GG(a[1][1]),GG(a[2][2]),GG(a[3][3]);
    if(totx==4 || totx==3&&tott==1) return 0;
    if(toto==4 || toto==3&&tott==1) return 1;
    totx=toto=tott=0;GG(a[0][3]),GG(a[1][2]),GG(a[2][1]),GG(a[3][0]);
    if(totx==4 || totx==3&&tott==1) return 0;
    if(toto==4 || toto==3&&tott==1) return 1;
    return ff>0?3:2;
}

int main(){
    freopen("1.in","r",stdin);
    freopen("1.txt","w",stdout);
    int tt, i, j, cal=0;
    scanf("%d",&tt);
    while(tt--){
        for(i=0;i<4;i++) for(j=0;j<4;j++)
            a[i][j] = getNext();
        printf("Case #%d: %s\n",++cal,ans[check()]);
    }
    return 0;
}
