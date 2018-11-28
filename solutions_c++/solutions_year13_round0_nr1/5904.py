#include<iostream>
#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    int N;
    cin>>N;
    for (int z=1;z<=N;z++)
    {
       char a[4][4];
       for (int i=0;i<4;i++)
       for (int j=0;j<4;j++)
       cin>>a[i][j];

       int dot=0,t=0,x=0,o=0,win=0;
       for (int i=0;i<4;i++)
       {
           t=0;x=0;o=0;
           for (int j=0;j<4;j++)
           {if (a[i][j]=='.'){dot=1;break;}
           if (a[i][j]=='T'){t++;}
           if (a[i][j]=='X'){x++;}
           if (a[i][j]=='O'){o++;}}
           if ((x==4)||((x==3)&&(t==1)))
           {
        win=1;break;
           }

           if ((o==4)||((o==3)&&(t==1)))
           {
        win=2;break;
           }
       }

    if (win==0)
    {

        for (int j=0;j<4;j++)
       {
           t=0;x=0;o=0;
           for (int i=0;i<4;i++)
           {if (a[i][j]=='.'){dot=1;break;}
           if (a[i][j]=='T'){t++;}
           if (a[i][j]=='X'){x++;}
           if (a[i][j]=='O'){o++;}}
           if ((x==4)||((x==3)&&(t==1)))
           {
        win=1;break;
           }

           if ((o==4)||((o==3)&&(t==1)))
           {
        win=2;break;
           }
       }
    }

    if (win==0)
    {
        t=0;x=0;o=0;
       for (int i=0;i<4;i++)
           {if (a[i][i]=='.'){dot=1;break;}
           if (a[i][i]=='T'){t++;}
           if (a[i][i]=='X'){x++;}
           if (a[i][i]=='O'){o++;}}
           if ((x==4)||((x==3)&&(t==1)))
           {
        win=1;
           }

           if ((o==4)||((o==3)&&(t==1)))
           {
        win=2;
           }
    }

    if (win==0)
    {
        t=0;x=0;o=0;
       for (int i=0;i<4;i++)
           {if (a[i][3-i]=='.'){dot=1;break;}
           if (a[i][3-i]=='T'){t++;}
           if (a[i][3-i]=='X'){x++;}
           if (a[i][3-i]=='O'){o++;}}
           if ((x==4)||((x==3)&&(t==1)))
           {
        win=1;
           }

           if ((o==4)||((o==3)&&(t==1)))
           {
        win=2;
           }
    }


       cout<<"Case #"<<z<<": ";
       if(win==2)
       cout<<"O won\n";
       else if(win==1)
       cout<<"X won\n";
       else
       {
           if (dot==1)
           cout<<"Game has not completed\n";
           else
           cout<<"Draw\n";
       }
    }
}
