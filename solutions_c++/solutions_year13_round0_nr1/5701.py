#include<iostream>
#include<cstdio>
#include<cstring>
#include<string>
using namespace std;
int main()
{
    freopen( "A-small-attempt1.in", "r", stdin );
	freopen( "output.txt", "w", stdout );
    int n,cases=0;
    cin>>n;
    getchar();
    int x,o,id,t,d;
    while(n--)
    {
        char s[5];
        id=t=x=d=o=0;
        char s1[5][5];
        int h=4,ind=-1,i,j;
        while(gets(s))
        {
            if(strlen(s)==0) break; ind++;
            s1[ind][0]=s[0];s1[ind][1]=s[1];s1[ind][2]=s[2];s1[ind][3]=s[3];
        }
       printf("Case #%d: ",++cases);
       for(i=0;i<=3;i++)
       {
           for(j=0;j<=3;j++)
           {
               if(s1[i][j]=='X') ++x;
               else if(s1[i][j]=='O') ++o;
               else if(s1[i][j]=='T') ++t;
               else if(s1[i][j]=='.') ++d;
           }
           if(x==4 || (x==3 && t==1))
           {
               id=1;break;
           }
           else if(o==4 || (o==3 && t==1))
           {
               id=2;break;
           }
           x=t=d=o=0;
       }
       x=t=d=o=0;
       if(id==0){
       for(i=0;i<=3;i++)
       {
           for(j=0;j<=3;j++)
           {
               if(s1[j][i]=='X') ++x;
               else if(s1[j][i]=='O') ++o;
               else if(s1[j][i]=='T') ++t;
               else if(s1[j][i]=='.') ++d;
           }
           if(x==4 || (x==3 && t==1))
           {
               id=1;break;
           }
           else if(o==4 || (o==3 && t==1))
           {
               id=2;break;
           }
           x=t=d=o=0;
       }
       }
       x=t=d=o=0;
       if(id==0)
       {
           if(s1[0][0]=='X') x++;if(s1[1][1]=='X') x++;if(s1[2][2]=='X') x++;if(s1[3][3]=='X') x++;
             if(s1[0][0]=='O') o++;if(s1[1][1]=='O') o++;if(s1[2][2]=='O') o++;if(s1[3][3]=='O') o++;
             if(s1[0][0]=='T') t++;if(s1[1][1]=='T') t++;if(s1[2][2]=='T') t++;if(s1[3][3]=='T') t++;
             if(s1[0][0]=='.') d++;if(s1[1][1]=='.') d++;if(s1[2][2]=='.') d++;if(s1[3][3]=='.') d++;
            if(x==4 || (x==3 && t==1))
           {
               id=1;
           }
           else if(o==4 || (o==3 && t==1))
           {
               id=2;
           }
           x=o=t=d=0;
            if(id==0)
           {
              if(s1[0][3]=='X') x++;if(s1[1][2]=='X') x++;if(s1[2][1]=='X') x++;if(s1[3][0]=='X') x++;
             if(s1[0][3]=='O') o++;if(s1[1][2]=='O') o++;if(s1[2][1]=='O') o++;if(s1[3][0]=='O') o++;
             if(s1[0][3]=='T') t++;if(s1[1][2]=='T') t++;if(s1[2][1]=='T') t++;if(s1[3][0]=='T') t++;
             if(s1[0][3]=='.') d++;if(s1[1][2]=='.') d++;if(s1[2][1]=='.') d++;if(s1[3][0]=='.') d++;
             if(x==4 || (x==3 && t==1))
           {
               id=1;
           }
           else if(o==4 || (o==3 && t==1))
           {
               id=2;
           }
           }
       }
       if(id==1) {printf("X won\n");}
       else if(id==2) {printf("O won\n");}
       else
       {
           if(d==0) {printf("Draw\n");}
           else if(d>0) {printf("Game has not completed\n");}
       }
    }

    return 0;
}

