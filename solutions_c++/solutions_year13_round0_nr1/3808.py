#include<stdio.h>
#include<math.h>
#include<stdlib.h>
#include<string.h>
#define fori(a) for(i=0;i<a;i++)
#define forj(a) for(j=0;j<a;j++)
#define fork(a,b) for(k=a;k<b;k++)
char arr[6][6],arr2[6][6];
int readint()
{
    int t=0;
    char c;
    c=getchar();
    while(c<'0' || c>'9')
        c=getchar();
    while(c>='0' && c<='9')
    {
        t=(t<<3)+(t<<1)+c-'0';
        c=getchar();
    }
    return t;
}
int main()
{
    int i,j,k,t;
    FILE *fp;
    freopen("A-large.in","r",stdin);
    FILE *fout ;
    freopen ("OUTPUT2.txt","w",stdout);
    t=readint();
    fori(t)
    {
        if (i!=0) getchar();
        forj(4) {gets(arr[j]);strcpy(arr2[j],arr[j]);}
        //forj(4) {puts(arr2[j]);}
        int flaga=0,flagb=0,flag=0;
        char c;
        forj(4) fork(0,4) if (arr[j][k]=='.') {flag=1;break;}
        c='X';
        forj(4)
        {
            k=0;
            if (arr[j][k]=='T') arr[j][k]='X';
            if (arr[j][k+1]=='T') arr[j][k+1]='X';
            if (arr[j][k+2]=='T') arr[j][k+2]='X';
            if (arr[j][k+3]=='T') {arr[j][k+3]='X';}
            //printf("%c %c %c %c\n",arr[j][k],arr[j][k+1],arr[j][k+2],arr[j][k+3]);
            if (arr[j][k]==c&&arr[j][k+1]==c&&arr[j][k+2]==c&&arr[j][k+3]==c) {flaga=1;break;}
        }
        //printf("flag=%d\n",flaga);
        fork(0,4)
        {
            j=0;
            if (arr[j][k]=='T') arr[j][k]='X';
            if (arr[j+1][k]=='T') arr[j+1][k]='X';
            if (arr[j+2][k]=='T') arr[j+2][k]='X';
            if (arr[j+3][k]=='T') arr[j+3][k]='X';
            //printf("%c %c %c %c\n",arr[j][k],arr[j][k+1],arr[j][k+2],arr[j][k+3]);
            if (arr[j][k]==c&&arr[j+1][k]==c&&arr[j+2][k]==c&&arr[j+3][k]==c) {flaga=1;break;}
        }
        if (arr[0][0]==c&&arr[1][1]==c&&arr[2][2]==c&&arr[3][3]==c) flaga=1;
        else if (arr[0][3]==c&&arr[1][2]==c&&arr[2][1]==c&&arr[3][0]==c) flaga=1;
        c='O';
        forj(4)
        {
            k=0;
            if (arr2[j][k]=='T') arr2[j][k]='O';
            if (arr2[j][k+1]=='T') arr2[j][k+1]='O';
            if (arr2[j][k+2]=='T') arr2[j][k+2]='O';
            if (arr2[j][k+3]=='T') arr2[j][k+3]='O';
            //printf("%c %c %c %c\n",arr2[j][k],arr2[j][k+1],arr2[j][k+2],arr2[j][k+3]);
            if (arr2[j][k]==c&&arr2[j][k+1]==c&&arr2[j][k+2]==c&&arr2[j][k+3]==c) {flagb=1;break;}
        }
        fork(0,4)
        {
            j=0;
            if (arr2[j][k]=='T') arr2[j][k]='O';
            if (arr2[j+1][k]=='T') arr2[j+1][k]='O';
            if (arr2[j+2][k]=='T') arr2[j+2][k]='O';
            if (arr2[j+3][k]=='T') arr2[j+3][k]='O';
            if (arr2[j][k]==c&&arr2[j+1][k]==c&&arr2[j+2][k]==c&&arr2[j+3][k]==c) {flagb=1;break;}
        }
        if (arr2[0][0]==c&&arr2[1][1]==c&&arr2[2][2]==c&&arr2[3][3]==c) flagb=1;
        else if (arr2[0][3]==c&&arr2[1][2]==c&&arr2[2][1]==c&&arr2[3][0]==c) flagb=1;
        //printf("flaga=%d flagb=%d flag=%d\n",flaga,flagb,flag);
        if (flaga==1&&flagb==0) printf("Case #%d: X won\n",i+1);
        else if (flagb==1&&flaga==0) printf("Case #%d: O won\n",i+1);
        else if (flaga==flagb&&flag==0) printf("Case #%d: Draw\n",i+1);
        else if (flaga==0&&flagb==0&&flag==1) printf("Case #%d: Game has not completed\n",i+1);
    }
    return 0;
}
