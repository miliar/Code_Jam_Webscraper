#include <iostream>
#include <string>
#include <vector>
//#include<conio.h>
using namespace std;
int main()
{
int tests;
FILE *file, *out;
    file=fopen("inputashu.txt", "r");
    out=fopen("outputashu.txt", "w");
    fscanf(file,"%d", &tests);
//printf("enter the no of test cases:-");
char a[5][5];
for(int t=1;t<=tests; t++)
{
bool flag=0;
//printf("enter the %d tic-tac-toe:-\n", t);

for(int i=1; i<5; i++)
{
for(int j=1; j<5; j++)
{
//printf("a[%d][%d]= ", i, j);
//fflush(stdin);
fscanf(file,"%c", &a[i][j]);
if(a[i][j]=='\n')
j--;
}
}

// X wins row wise

for(int r=1; r<5; r++)
{
for(int c=1; c<5; c++)
{
if(a[r][c]=='O' || a[r][c]=='.' )
break;
if(c==4)
{
flag=1;
fprintf(out,"Case #%d: X won\n", t);
}

}
if(flag==1)
break;
}
if(flag==1)
continue;

// X wins column wise
for(int c=1; c<5; c++)
{
for(int r=1; r<5; r++)
{
if(a[r][c]=='O' || a[r][c]=='.')
break;
if(r==4)
{
flag=1;
fprintf(out,"Case #%d: X won\n", t);
}

}
if(flag==1)
break;
}
if(flag==1)
continue;


//X wins diagonal 1
for(int r=1, c=1; r<5, c<5; r++, c++)
{

{
if(a[r][c]=='O' || a[r][c]=='.')
break;
if(c==4 && r==4)
{
flag=1;
fprintf(out, "Case #%d: X won\n", t);
}

}
if(flag==1)
break;
}
if(flag==1)
continue;

//X wins diagonal 2
for(int r=1, c=4; r<5, c>0; r++, c--)
{

{
if(a[r][c]=='O' || a[r][c]=='.')
break;
if(r==4 && c==1)
{
flag=1;
fprintf(out,"Case #%d: X won\n", t);
}

}
if(flag==1)
break;
}
if(flag==1)
continue;


//O wins row wise

for(int r=1; r<5; r++)
{
for(int c=1; c<5; c++)
{
if(a[r][c]=='X' || a[r][c]=='.')
break;
if(c==4)
{
flag=1;
fprintf(out,"Case #%d: O won\n", t);
}

}
if(flag==1)
break;
}
if(flag==1)
continue;


//O wins column wise

for(int c=1; c<5; c++)
{
for(int r=1; r<5; r++)
{
if(a[r][c]=='X' || a[r][c]=='.')
break;
if(r==4)
{
flag=1;
fprintf(out,"Case #%d: O won\n", t);
}

}
if(flag==1)
break;
}
if(flag==1)
continue;


//O wins diagonal 1
for(int r=1, c=1; r<5, c<5; r++, c++)
{

{
if(a[r][c]=='X' || a[r][c]=='.')
break;
if(c==4 && r==4)
{
flag=1;
fprintf(out,"Case #%d: O won\n", t);
}

}
if(flag==1)
break;
}
if(flag==1)
continue;

//O wins diagonal 2
for(int r=1, c=4; r<5, c>0; r++, c--)
{

{
if(a[r][c]=='X' || a[r][c]=='.')
break;
if(r==4 && c==1)
{
flag=1;
fprintf(out,"Case #%d: O won\n", t);
}

}
if(flag==1)
break;
}
if(flag==1)
continue;



//draw

for(int r=1; r<5; r++)
{
for(int c=1; c<5; c++)
{
if(a[r][c]=='.' )
{
fprintf(out,"Case #%d: Game has not completed\n", t);
flag=1;
break;
}
}
if(flag==1)
break;
}
if(flag==1)
continue;

//match not completed
fprintf(out,"Case #%d: Draw\n", t);
}
//getch();
}
