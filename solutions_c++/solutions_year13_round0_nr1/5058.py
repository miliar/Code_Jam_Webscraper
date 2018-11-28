#include<iostream>
#include<cstring>
#include<cstdio>

using namespace std;

char peta[5][5];
int kasus;

int main() {
    scanf("%d",&kasus);
    for (int l=1;l<=kasus;++l) {
        bool kosong = false;
        int x,y;
        
        for (int j=0;j<4;++j) {
            scanf("%s",peta[j]);
            for (int k=0;k<4;++k) {
                if (peta[j][k] == 'T') {
                    x = k;
                    y = j;
                } else if (peta[j][k] == '.') {
                    kosong = true;
                }
            }
        }
        
        peta[y][x] = 'X';
        //cout<<y<<" "<<x<<endl;
        bool f1 = false,f2=false,flag;
        
        for (int j=0;j<4;++j) {
            //cout<<peta[j]<<endl;
            flag = true;
            for (int k=0;k<4 && flag;++k) {
                flag = (peta[j][k] == 'X');
                //cout<<k<<endl;
            }
            
            if (flag) {
                f1 = true;
                break;
            }
            
            flag = true;
            for (int k=0;k<4 && flag;++k) {
                flag = (peta[k][j] == 'X');
            }

            if (flag == true) {
                f1 = true;
                break;
            }
        }
        
        flag = true;
        for (int i=0;i<4 && flag;++i) {
            flag = (peta[i][i] == 'X');
        }
        f1 = f1 || flag;
        
        flag = true;
        for (int i=0;i<4 && flag;++i) {
            flag = (peta[i][3-i] == 'X');
        }
        f1 = f1 || flag;
        
        peta[y][x] = 'O';
        for (int j=0;j<4;++j) {
            flag = true;
            for (int k=0;k<4 && flag;++k) {
                flag = (peta[j][k] == 'O');
            }
            
            if (flag) {
                f2 = true;
                break;
            }
            
            flag = true;
            for (int k=0;k<4 && flag;++k) {
                flag = (peta[k][j] == 'O');
            }

            if (flag == true) {
                f2 = true;
                break;
            }
        }
        
        flag = true;
        for (int i=0;i<4 && flag;++i) {
            flag = (peta[i][i] == 'O');
        }
        f2 = f2 || flag;
        
        flag = true;
        for (int i=0;i<4 && flag;++i) {
            flag = (peta[i][3-i] == 'O');
        }
        f2 = f2 || flag;
        
        printf("Case #%d: ",l);
        if (f1) printf("X won\n");
        else if (f2) printf("O won\n");
        else if (kosong) printf("Game has not completed\n");
        else printf("Draw\n");
    }
    return 0;
}
