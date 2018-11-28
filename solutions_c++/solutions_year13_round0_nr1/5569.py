#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#define f(i,a,b) for(int i=a;i<b;i++)
using namespace std;
int chk(char a,char b,char c,char d);
int main()
{
    int te;
    cin>>te;
    int cas=1;
    while(te--)
    {
               char arr[4][4];
               int x=0;
               int y=0;
               f(i,0,4)
               f(j,0,4)
               {
               cin>>arr[i][j];
               if(arr[i][j]=='.')
               {
                      y=3;           
               }
               }
               f(i,0,4)
               {
                        if((x!=1)&&(x!=2))
                        x=chk(arr[i][0],arr[i][1],arr[i][2],arr[i][3]);
                        if((x!=1)&&(x!=2))
                        x=chk(arr[0][i],arr[1][i],arr[2][i],arr[3][i]);
               }
               if((x!=1)&&(x!=2))
               x=chk(arr[0][0],arr[1][1],arr[2][2],arr[3][3]);
               if((x!=1)&&(x!=2))
               x=chk(arr[3][0],arr[2][1],arr[1][2],arr[0][3]);
               if(x==1) cout<<"Case #"<<cas<<": "<<"X won\n"; 
               else if(x==2) cout<<"Case #"<<cas<<": "<<"O won\n";
               else if(y==3)cout<<"Case #"<<cas<<": "<<"Game has not completed\n";
               else cout<<"Case #"<<cas<<": "<<"Draw\n";
               
               cas++;  
    }


 return 0;
}
int chk(char a,char b,char c,char d)
{
    char e[4];
    e[0]=a;
    e[1]=b;
    e[2]=c;
    e[3]=d;
    int k=0;
    int q=0;
    int t=0;
    f(i,0,4)
    {
            if(e[i]=='T') t++;
            else if(e[i]=='X') k++;
            else if(e[i]=='O') q++;
    }
    if(((k==3)&&(t==1))||(k==4)) return 1;
    else if(((q==3)&&(t==1))||(q==4)) return 2;  
    else return 0;    
}
