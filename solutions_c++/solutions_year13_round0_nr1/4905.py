#include<stdio.h>
#include<string.h>
#include<stdlib.h>
#include<time.h>
char a[16][16];
int n = 4;
bool checkrow(char c, int i){
    bool res=1;
    for(int j=0;j<n && res;j++)
        res&=(a[i][j]==c || a[i][j]=='T');
    return res;
}
bool checkcol(char c, int i){
    bool res=1;
    for(int j=0;j<n && res;j++)
        res&=(a[j][i]==c || a[j][i]=='T');
    return res;
}
bool checkd1(char c){
    bool res=1;
    for(int j=0;j<n && res;j++)
        res&=(a[j][j]==c || a[j][j]=='T');
    return res;
}
bool checkd2(char c){
    bool res=1;
    for(int j=0;j<n && res;j++)
        res&=(a[j][n-j-1]==c || a[j][n-j-1]=='T');
    return res;
}
int main(){
#ifdef _DEBUG
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#else
    freopen("tetrahedron.in", "r", stdin);
    freopen("tetrahedron.out", "w", stdout);
#endif
    int i, j;
    int T, Tests;
    scanf("%d",&Tests);
    for(T=1;T<=Tests;T++){
        gets(a[0]);
        for(i=0;i<n;i++)
            gets(a[i]);
        int dot=0;
        for(i=0;i<n;i++)
            for(j=0;j<n;j++)
                dot+=(a[i][j]=='.');
        bool  wx=0, wo=0;
        for(i=0;i<n;i++){
            wx|=checkrow('X', i)|checkcol('X', i);
            wo|=checkrow('O', i)|checkcol('O', i);
        }
        wx|=checkd1('X')|checkd2('X');
        wo|=checkd1('O')|checkd2('O');
        if(wx && wo)
            printf("Case #%d: Draw\n", T);
        else if(wx && !wo)
            printf("Case #%d: X won\n", T);
        else if(!wx && wo)
            printf("Case #%d: O won\n", T);
        else if(!wx && !wo && dot==0)
            printf("Case #%d: Draw\n", T);
        else
            printf("Case #%d: Game has not completed\n", T);
     }


    return 0;
}
