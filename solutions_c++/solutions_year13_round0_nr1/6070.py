#include<fstream.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<iomanip.h>
#include<ctype.h>
#include<process.h>
#include<stdio.h>
#include<stdlib.h>
#include<iostream.h>
int hmm()
{
char a[4][4];
for(int i=0;i<4;i++)
for(int j=0;j<4;j++)
cin>>a[i][j];

int x=5,y=5;
for(i=0;i<4;i++)
for(int j=0;j<4;j++)
if(a[i][j]=='T')
{x=i;
y=j;
}

if(x<5)
a[x][y]='X';


if(a[0][0]=='X' && a[0][1]=='X' && a[0][2]=='X'&& a[0][3]=='X' )
return 10;
else if(a[1][0]=='X' && a[1][1]=='X' && a[1][2]=='X'&& a[1][3]=='X' )
return 10;
else if(a[2][0]=='X' && a[2][1]=='X' && a[2][2]=='X'&& a[2][3]=='X' )
return 10;
else if(a[3][0]=='X' && a[3][1]=='X' && a[3][2]=='X'&& a[3][3]=='X' )
return 10;
else if(a[0][0]=='X' && a[1][0]=='X' && a[2][0]=='X'&& a[3][0]=='X' )
return 10;
else if(a[0][1]=='X' && a[1][1]=='X' && a[2][1]=='X'&& a[3][1]=='X' )
return 10;
else if(a[0][2]=='X' && a[1][2]=='X' && a[2][2]=='X'&& a[3][2]=='X' )
return 10;
else if(a[0][3]=='X' && a[1][3]=='X' && a[2][3]=='X'&& a[3][3]=='X' )
return 10;
else if(a[0][0]=='X' && a[1][1]=='X' && a[2][2]=='X'&& a[3][3]=='X' )
return 10;
else if(a[0][3]=='X' && a[1][2]=='X' && a[2][1]=='X'&& a[3][0]=='X' )
return 10;


if(x<5)
a[x][y]='O';

if(a[0][0]=='O' && a[0][1]=='O' && a[0][2]=='O'&& a[0][3]=='O' )
return 20;
else if(a[1][0]=='O' && a[1][1]=='O' && a[1][2]=='O'&& a[1][3]=='O' )
return 20;
else if(a[2][0]=='O' && a[2][1]=='O' && a[2][2]=='O'&& a[2][3]=='O' )
return 20;
else if(a[3][0]=='O' && a[3][1]=='O' && a[3][2]=='O'&& a[3][3]=='O' )
return 20;
else if(a[0][0]=='O' && a[1][0]=='O' && a[2][0]=='O'&& a[3][0]=='O' )
return 20;
else if(a[0][1]=='O' && a[1][1]=='O' && a[2][1]=='O'&& a[3][1]=='O' )
return 20;
else if(a[0][2]=='O' && a[1][2]=='O' && a[2][2]=='O'&& a[3][2]=='O' )
return 20;
else if(a[0][3]=='O' && a[1][3]=='O' && a[2][3]=='O'&& a[3][3]=='O' )
return 20;
else if(a[0][0]=='O' && a[1][1]=='O' && a[2][2]=='O'&& a[3][3]=='O' )
return 20;
else if(a[0][3]=='O' && a[1][2]=='O' && a[2][1]=='O'&& a[3][0]=='O' )
return 20;

else
{       int f=0;
 for(i=0;i<4;i++)
 {
 for(int j=0;j<5;j++)
  if(a[i][j]=='.')
  {
  return 30;
  f=1;
  break;
  }
 if(f==1)
 break;
 }


if(f!=1)
return 40;


}
}
//*******************************************************************//


//*******************************************************************//
void main()
{
clrscr();
int n,b[1000]={0,0,0},k=0;
cin>>n;

for(int i=0;i<n;i++)
b[k++]=hmm();
for(int l=0;l<1;l++)
for(int j=0;j<n;j++)
{
cout<<"Case #"<<j+1<<": ";
if(b[j]==10)
{cout<<"X won"<<endl;
continue;
}
else if(b[j]==20)
{cout<<"O won"<<endl;
continue;
}
else if(b[j]==30)
{cout<<"Game has not completed"<<endl;
continue;
}
else if(b[j]==40)
{cout<<"Draw"<<endl;
continue;
}

}
getch();
}