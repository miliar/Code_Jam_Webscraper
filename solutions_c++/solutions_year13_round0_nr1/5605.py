#include<fstream.h>
#include<conio.h>
#include<stdio.h>
void main()
{
clrscr();
int T,i,j,filled,x;
char board[6][6],ch;
ifstream fin;
ofstream fout;
fin.open("tictac.in");
fout.open("tictac.txt");
fin>>T;
fin.get(ch);
for(x=1;x<=T;x++)
{
filled=1;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
fin>>board[i][j];
if(board[i][j]=='.')
filled=0;
}
fin.get(ch);
}

/*for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
cout<<board[i][j]<<" ";
}
cout<<"\n";
}
cout<<"\n\n"<<m<<"  "<<n<<"\n\n"<<filled<<"\n\n"<<ondiag;*/


for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if((board[i][j]!='X')&&(board[i][j]!='T'))
break;
else if(j==3)
{
fout<<"Case #"<<x<<": "<<"X won\n";
goto end;
}
}
}
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if((board[i][j]!='O')&&(board[i][j]!='T'))
break;
else if(j==3)
{
fout<<"Case #"<<x<<": "<<"O won\n";
goto end;
}
}
}
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if((board[j][i]!='O')&&(board[j][i]!='T'))
break;
else if(j==3)
{
fout<<"Case #"<<x<<": "<<"O won\n";
goto end;
}
}
}
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if((board[j][i]!='X')&&(board[j][i]!='X'))
break;
else if(j==3)
{
fout<<"Case #"<<x<<": "<<"X won\n";
goto end;
}
}
}

for(i=0,j=0;i<4;i++,j++)
{
if((board[i][j]!='O')&&(board[i][j]!='T'))
break;
else if(i==3)
{
fout<<"Case #"<<x<<": "<<"O won\n";
goto end;
}
}
for(i=0,j=0;i<4;i++,j++)
{
if((board[i][j]!='X')&&(board[i][j]!='T'))
break;
else if(i==3)
{
fout<<"Case #"<<x<<": "<<"X won\n";
goto end;
}
}
for(i=0,j=3;i<4;i++,j--)
{
if((board[i][j]!='O')&&(board[i][j]!='T'))
break;
else if(i==3)
{
fout<<"Case #"<<x<<": "<<"O won\n";
goto end;
}
}
for(i=0,j=3;i<4;i++,j--)
{
if((board[i][j]!='X')&&(board[i][j]!='T'))
break;
else if(i==3)
{
fout<<"Case #"<<x<<": "<<"X won\n";
goto end;
}
}







/*for(i=0;i<4;i++)
{
if((board[m][i]!='O')&&(board[m][i]!='T'))
break;
else if(i==3)
{
cout<<"\n\nO won";
goto end;
}
}
for(i=0;i<4;i++)
{
if((board[i][n]!='X')&&(board[i][n]!='T'))
break;
else if(i==3)
{
cout<<"\n\nX won";
goto end;
}
}
for(i=0;i<4;i++)
{
if((board[i][n]!='O')&&(board[i][n]!='T'))
break;
else if(i==3)
{
cout<<"\n\nO won";
goto end;
}
}
if(ondiag==0)
goto skip;
if(ondiag==1)
{
for(i=0,j=0;i<4;i++,j++)
{
if((board[i][j]!='O')&&(board[i][j]!='T'))
break;
else if(i==3)
{
cout<<"\n\nO won";
goto end;
}
}
for(i=0,j=0;i<4;i++,j++)
{
if((board[i][j]!='X')&&(board[i][j]!='T'))
break;
else if(i==3)
{
cout<<"\n\nX won";
goto end;
}
}
}
if(ondiag==-1)
{
for(i=0,j=3;i<4;i++,j--)
{
if((board[i][j]!='O')&&(board[i][j]!='T'))
break;
else if(i==3)
{
cout<<"\n\nO won";
goto end;
}
}
for(i=0,j=3;i<4;i++,j--)
{
if((board[i][j]!='X')&&(board[i][j]!='T'))
break;
else if(i==3)
{
cout<<"\n\nX won";
goto end;
}
}
}
skip:*/
if(filled==0)
fout<<"Case #"<<x<<": "<<"Game has not completed\n";
else
fout<<"Case #"<<x<<": "<<"Draw\n";
end:
fin.get(ch);
}
getch();
}