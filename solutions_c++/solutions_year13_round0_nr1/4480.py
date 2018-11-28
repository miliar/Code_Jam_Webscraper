#include<stdio.h>
#include<stdlib.h>

int a[4][4];

int checkwin(char ch){
    int i, j, n=4;
    for(i=0;i<n;i++){
        for(j=0;j<n;j++)
            if(a[i][j]!= ch && a[i][j]!='T') break;
        if(j==n) return 1;
    }
    
    for(i=0;i<n;i++){
        for(j=0;j<n;j++)
            if(a[j][i]!= ch && a[j][i]!='T') break;
        if(j==n) return 1;
    }
    
    for(i=0;i<n;i++) if(a[i][i]!=ch && a[i][i]!='T') break;
    if(i==n) return 1;
    
    for(i=0;i<n;i++) if(a[i][n-1-i]!=ch && a[i][n-1-i]!='T') break;
    if(i==n) return 1;
    
    return 0;
}

int main(){
    int tcases;
    FILE * pread = fopen("A-large.in", "r");
    FILE * pwrite = fopen("outA.txt", "w");
    fscanf(pread, "%d", &tcases);
    int c;
    for(c=1;c<=tcases;c++){
    
    int i, j, n=4;
    
    for(i=0;i<n;i++)
        for(j=0;j<n;j++)
            fscanf(pread, " %c", &a[i][j]);
    
    fprintf(pwrite, "Case #%d: ", c);
    if(checkwin('X')) fprintf(pwrite, "X won\n");
    else if(checkwin('O')) fprintf(pwrite, "O won\n");
    else {
    int flag=1;
    for(i=0;i<n && flag;i++) for(j=0;j<n && flag;j++)
        if(a[i][j]=='.') flag=0;
    
    if(flag) fprintf(pwrite, "Draw\n");
    else fprintf(pwrite,"Game has not completed\n");
    }
    }
    system("pause");
    return 0;
}
