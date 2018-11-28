#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <iomanip>
#include <math.h>
#include <fstream>
using namespace std;
int main() {
    int tc,tci,i,j,k,output,O_no,X_no,dot;
    char str[6][6],ch;
    FILE *fp = fopen("C:/ikj/input.txt","r");
    FILE *fp2 = fopen("C:/ikj/output.txt","w");
    fscanf(fp,"%d",&tc);
    fgetc(fp);
    for(tci=0;tci<tc;tci++) {
        for(i=0;i<4;i++) {
            fscanf(fp,"%s",str[i]);
        }
        output=0;dot=0;
        for(i=0;i<4;i++) {
            O_no=0; X_no=0;
            for(j=0;j<4;j++) {
                if(str[i][j]=='.') {
                    O_no=X_no=dot=1;
                    break;
                }
                if(str[i][j]=='X') O_no=1;
                if(str[i][j]=='O') X_no=1;
            }
            if(X_no==0) {fprintf(fp2,"Case #%d: X won\n",tci+1);output=1;break;}
            else if(O_no==0) {fprintf(fp2,"Case #%d: O won\n",tci+1);output=1;break;}
        }
        for(i=0;(i<4)&&(output==0);i++) {
            O_no=0; X_no=0;
            for(j=0;j<4;j++) {
                if(str[j][i]=='.') {
                    O_no=X_no=dot=1;
                    break;
                }
                if(str[j][i]=='X')  O_no=1;
                if(str[j][i]=='O')  X_no=1;
            }
            if(X_no==0) {fprintf(fp2,"Case #%d: X won\n",tci+1);output=1;break;}
            else if(O_no==0) {fprintf(fp2,"Case #%d: O won\n",tci+1);output=1;break;}
        }
        if(output==0) {
        O_no=0; X_no=0;
        for(i=0;i<4;i++) {
            if(str[i][i]=='.') {
                O_no=X_no=dot=1;
                break;
            }
            if(str[i][i]=='X') O_no=1;
            if(str[i][i]=='O') X_no=1;
        }
        if(X_no==0) {fprintf(fp2,"Case #%d: X won\n",tci+1);output=1;}
        else if(O_no==0) {fprintf(fp2,"Case #%d: O won\n",tci+1);output=1;}
        }
        if(output==0) {
            O_no=0; X_no=0;
            for(i=0;i<4;i++) {
                if(str[i][3-i]=='.') {
                    O_no=X_no=dot=1;
                    break;
                }
                if(str[i][3-i]=='X') O_no=1;
                if(str[i][3-i]=='O') X_no=1;
            }
            if(X_no==0) {fprintf(fp2,"Case #%d: X won\n",tci+1);output=1;}
            else if(O_no==0) {fprintf(fp2,"Case #%d: O won\n",tci+1);output=1;}
        }
        if((dot==1)&&(output==0)) {fprintf(fp2,"Case #%d: Game has not completed\n",tci+1);output=1;}
        if(output==0) fprintf(fp2,"Case #%d: Draw\n",tci+1);
    }
}
