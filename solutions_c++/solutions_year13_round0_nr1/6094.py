#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<fstream.h>
unsigned char t[4][4]; //array in which X,O and T pattern in a game is stored//
unsigned char ch;  //variable to read a character from input stream//
int i = 0 , j = 0 , f = 0 , r = 0 , s = 0 , d = 0;
int no_of_cases(); //to count number of test cases//
void row_check();  //to check row wise if any of the players won//
void col_check();  //to check column wise if any of the players won//
void dia_check();  //to check diagonally if any of the players won//
void incomplete(); //to check if the game actually completed //
void array_init(); //to initialize the various elements of character array//
void disp();       //to display the result//
ifstream in("rojo.txt");        //in handles input stream//
ofstream out("patrick.txt");    //out handles output stream//
void main()
{int a;
clrscr();
a = no_of_cases();
cout<<a;
for(int h=1;h<=(5*a);h++)
{array_init();
f=0;
if(h%5==0)
 {disp();
  i=0;
  j=0;
  out<<"Case #"<<h/5<<": ";
 row_check();
 if(f!=1)
 {col_check();
  if(f!=1)
  {dia_check();}
  if(f!=1)
  {incomplete();}
 }
 if(f==0)
 {cout<<"\nDRAW";
 out<<"Draw\n";}
 }


 }

in.close();
out.close();
getch();
}
void row_check()
{for(r=0;r<4;r++)
 {if( (t[r][0]=='T') && (t[r][1]=='T') && (t[r][2]=='T') && (t[r][3]=='T'))
   {continue;}
  else if( (t[r][0]=='T'||t[r][0]=='X') && (t[r][1]=='T'||t[r][1]=='X') && (t[r][2]=='T'||t[r][2]=='X') && (t[r][3]=='T'||t[r][3]=='X'))
   {cout<<"\nX won!!";
    out<<"X won\n";
    f =	1;
    break;}
  else if( (t[r][0]=='T'||t[r][0]=='O') && (t[r][1]=='T'||t[r][1]=='O') && (t[r][2]=='T'||t[r][2]=='O') && (t[r][3]=='T'||t[r][3]=='O'))
   {cout<<"\nO won!!";
    out<<"O won\n";
    f = 1;
    break;}
  }
}
void col_check()
{for(r=0;r<4;r++)
 {if( (t[0][r]=='T') && (t[1][r]=='T') && (t[2][r]=='T') && (t[3][r]=='T'))
   {continue;}
  else if( (t[0][r]=='T'||t[0][r]=='X') && (t[1][r]=='T'||t[1][r]=='X') && (t[2][r]=='T'||t[2][r]=='X') && (t[3][r]=='T'||t[3][r]=='X'))
   {cout<<"\nX won!!";
    out<<"X won\n";
    f = 1;
    break;}
  else if( (t[0][r]=='T'||t[0][r]=='O') && (t[1][r]=='T'||t[1][r]=='O') && (t[2][r]=='T'||t[2][r]=='O') && (t[3][r]=='T'||t[3][r]=='O'))
   {cout<<"\nO won";
    out<<"O won\n";
    f = 1;
    break;}
  }
}

void dia_check()
{if( (t[0][0]=='T' || t[0][0]=='X') &&  (t[1][1]=='T' || t[1][1]=='X') && (t[2][2]=='T' || t[2][2]=='X') && (t[3][3]=='T' || t[3][3]=='X') )
  {cout<<"\nX won!!";
   out<<"X won\n";
   f=1;}
 else if( (t[0][0]=='T' || t[0][0]=='O') &&  (t[1][1]=='T' || t[1][1]=='O') && (t[2][2]=='T' || t[2][2]=='O') && (t[3][3]=='T' || t[3][3]=='O') )
  {cout<<"\nO won!!";
   out<<"O won\n";
   f=1;}
 else if( (t[0][3]=='T' || t[0][3]=='O') &&  (t[1][2]=='T' || t[1][2]=='O') && (t[2][1]=='T' || t[2][1]=='O') && (t[3][0]=='T' || t[3][0]=='O') )
  {cout<<"\nO won!!";
   out<<"O won\n";
   f=1;}
 else if( (t[0][3]=='T' || t[0][3]=='X') &&  (t[1][2]=='T' || t[1][2]=='X') && (t[2][1]=='T' || t[2][1]=='X') && (t[3][0]=='T' || t[3][0]=='X') )
  {cout<<"\nX won!!";
   out<<"X won\n";
   f=1;}
}
void array_init()
{ f = 0;
  in.get(ch);
if( (i<4) & (j<4))
{ while( (ch!='\n') && ((int)ch!=255))
  {t[i][j++]=ch;
   in.get(ch);
    if(j==4)
     {j=0;
      i=i++;
     }
  }
}
else{
  while((ch!='\n') && ((int)ch!=255))
     { in.get(ch);
     }
    }
}
void disp()
{for(i=0;i<4;i++)
 { cout<<"\n";
   for(j=0;j<4;j++)
    {cout<<t[i][j];}
  }
}
int no_of_cases()
{int a=0;
in.seekg(0);
in.get(ch);
a = (int)ch -48;
in.get(ch);
while(ch!='\n')
{a = (a*10) + ((int)ch - 48);
in.get(ch);
}
return a;
}

void incomplete()
{for(r=0;r<4;r++)
{ for(s=0;s<4;s++)
   { if(t[r][s]!='X' && t[r][s] !='O' && t[r][s] != 'T')
    {cout<<"\nMATCH NOT COMPLETED";
     out<<"Game has not completed\n";
     f=1;
     break;}

   }
   if(f==1)
   {break;}
}
	}


