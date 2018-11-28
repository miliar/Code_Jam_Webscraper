#include<iostream>
#include<Vector>
using namespace std;
char a[10][10];
int f(char d)
{
    int i,j;
    for(i=0;i<4;i++)    
    {
                    for(j=0;j<4;j++)
                    {
                                    if(a[i][j]==d||a[i][j]=='.') {break;}
                    }
                    if(j==4) return 1;
    }
    for(i=0;i<4;i++)    
    {
                    for(j=0;j<4;j++)
                    {
                                    if(a[j][i]==d||a[j][i]=='.') break;
                    }
                    if(j==4) return 1;
    }
    for(i=0;i<4;i++)
    if(a[i][i]==d||a[i][i]=='.') break;
    if(i==4) return 1;
    for(i=0;i<4;i++)
    if(a[i][3-i]==d||a[i][3-i]=='.') break;
    if(i==4) return 1;
    return 0;
}
int main()
{
    freopen("in.txt","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    scanf("%d",&t);
    int i,j,k,sign;
    for(i=1;i<=t;i++)
    {
             for(j=0;j<4;j++)
             scanf("%s",a[j]);
             sign=0;
             if(f('O'))  sign=1;
             else if(f('X')) sign=-1;
             else
             for(j=0;j<4;j++)
             for(k=0;k<4;k++)
             if(a[j][k]=='.') sign=2;
             printf("Case #%d: ",i);
             if(sign==1) printf("X won\n");
             else if(sign==-1) printf("O won\n");
             else if(sign==2)  printf("Game has not completed\n");
             else printf("Draw\n");
    }
    return 0;
}
