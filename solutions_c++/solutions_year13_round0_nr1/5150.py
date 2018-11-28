#include <iostream>
#include<stdio.h>
#include <cstring>

using namespace std;
char a[5][5];
string ans="";
int main()
{
   freopen("A-large.in","r",stdin);
   freopen("A-large.out","w",stdout);

  int T;int ca=1;
    scanf("%d",&T);
    while (T--){
       for (int i=0;i<4;i++){
         scanf("%s",a[i]);
       }
       ans="Draw";
       for (int i=0;i<4;i++){
         for (int j=0;j<4;j++){
           if (a[i][j]=='.') {ans="Game has not completed";break;}
         }
       }
       int x,o,t;
       x=0;o=0;t=0;
       for (int i=0;i<4;i++){
         if (a[i][i]=='.')break;
             if(a[i][i]=='X') x++;
             if(a[i][i]=='O') o++;
             if (a[i][i]=='T') t++;
       }
       if (x+t==4) {ans="X won";cout<<"Case #"<<ca++<<": "<<ans<<endl;continue;}
       if (o+t==4) {ans="O won";cout<<"Case #"<<ca++<<": "<<ans<<endl;continue;}
       x=0;o=0;t=0;
       for (int i=0;i<4;i++){
         if (a[i][3-i]=='.')break;
             if(a[i][3-i]=='X') x++;
             if(a[i][3-i]=='O') o++;
             if (a[i][3-i]=='T') t++;
       }
       if (x+t==4) {ans="X won";cout<<"Case #"<<ca++<<": "<<ans<<endl;continue;}
       if (o+t==4) {ans="O won";cout<<"Case #"<<ca++<<": "<<ans<<endl;continue;}
       for (int i=0;i<4;i++){
           x=0;o=0;t=0;
         for (int j=0;j<4;j++){
             if (a[i][j]=='.')break;
             if(a[i][j]=='X') x++;
             if(a[i][j]=='O') o++;
             if (a[i][j]=='T') t++;
         }
         if (x+t==4) {ans="X won";break;}
         if (o+t==4) {ans="O won";break;}
          x=0;o=0;t=0;
         for (int j=0;j<4;j++){
             if (a[j][i]=='.')break;
             if(a[j][i]=='X') x++;
             if(a[j][i]=='O') o++;
             if (a[j][i]=='T') t++;
         }
         if (x+t==4) {ans="X won";break;}
         if (o+t==4) {ans="O won";break;}
       }
       cout<<"Case #"<<ca++<<": "<<ans<<endl;
    }
    return 0;
}
