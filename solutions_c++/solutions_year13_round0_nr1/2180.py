#include<cstdio>
int T, vb[4][4];
char gb[4][4];
int res;

bool init(){
     bool f = 1;
     for (int i = 0; i < 4; i++)
        for (int j = 0; j < 4; j++){
            switch (gb[i][j]){
                   case ('X'): vb[i][j] = 1; break;
                   case ('O'): vb[i][j] = 10; break;
                   case ('T'): vb[i][j] = 100; break;
                   case ('.'): vb[i][j] = 0; f = 0; break;
            }
        }
     return f;
}

int Check(){
    bool f = init();
    int res = -1;
    
    for (int i = 0; i < 4; i++){
        int r = 0, c = 0;
        for (int j = 0; j < 4; j++){
            r += vb[i][j];
            c += vb[j][i];
        }
        if ((r == 4)||(c == 4)||(r==103)||(c == 103)) res = 0;
        if ((r ==40)||(c ==40)||(r==130)||(c == 130)) res = 1;
    }
    
    if (res == -1){
       int d1 = 0, d2 = 0;
       for (int i = 0; i < 4; i++){
           d1 += vb[i][i];
           d2 += vb[i][3-i];
       }
       if ((d1 == 4)||(d2 == 4)||(d1 == 103)||(d2 == 103)) res = 0;
       if ((d1 ==40)||(d2 ==40)||(d1 == 130)||(d2 == 130)) res = 1;
    }
    
    if (res == -1){
        if (f) res = 2; else res = 3;
    }
    
    return res;
}

int main(){

//    freopen("GCJ13_QR_Alarge.in","r",stdin);
//    freopen("GCJ13_QR_Alarge.out","w",stdout);
    scanf("%d", &T);
    for (int i = 0; i < T; i++){
        for (int j = 0; j < 4; j++)scanf("%s",gb[j]);
        res = Check();
        switch (res){
           case 0: printf("Case #%d: X won\n", i+1); break;
           case 1: printf("Case #%d: O won\n", i+1); break;
           case 2: printf("Case #%d: Draw\n", i+1); break;
           case 3: printf("Case #%d: Game has not completed\n", i+1); break;
        }
    }
    return 0;
}
