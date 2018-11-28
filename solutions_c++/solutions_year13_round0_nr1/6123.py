#include<stdio.h>
#include<stdlib.h>
#include<string.h>
int tictactoe( char a[4][4] , int count1 , int count2 , int x , int y )
{
int i , j , temp1 , temp2 , temp3 ;
//travelling aal rows
for(i=0;i<4;i++)
{
if( a[i][0] == a[i][1] &&a[i][0] == a[i][2] &&a[i][0] == a[i][3] )
{
if(a[i][0] == 'X')
return 1;
if(a[i][0] == 'O')
return 2 ;
}
}

//travelling all columns
for(i=0;i<4;i++)
{
if( a[0][i] == a[1][i] &&a[0][i] == a[2][i] &&a[0][i] == a[3][i] )
{
if(a[0][i] == 'X')
return 1;
if(a[0][i] == 'O')
return 2 ;
}
}

//checking diaognals
if( a[0][0] == a[1][1] &&a[0][0] == a[2][2] &&a[0][0] == a[3][3] )
{
if(a[0][0] == 'X')
return 1;
if(a[0][0] == 'O')
return 2 ;
}

if( a[0][3] == a[1][2] &&a[0][3] == a[2][1] && a[0][3] == a[3][0] )
{
if(a[0][3] == 'X')
return 1;
if(a[0][3] == 'O')
return 2 ;
}

//checking for t 
if(count2 == 0 )
{
if(count1)
return 4 ;
else
return 3 ;
}



//if T is there


//travelling all rows
for(i=0;i<4;i++)
{
temp1 = 0 ;
temp2 = 0 ;
temp3 = 0 ;
for(j=0 ; j<4 ; j++)
{
if(a[i][j] == 'X')
temp1++;
if(a[i][j] == 'O')
temp2++ ;
if(a[i][j] == 'T')
temp3++ ;
}
if(temp1 == 3  && temp3 == 1)
return 1;
if(temp2 == 3  && temp3 == 1)
return 2 ;
}

//travelling all columns
for(j=0;j<4;j++)
{
temp1 = 0 ;
temp2 = 0 ;
temp3 = 0 ;
for(i=0 ; i<4 ; i++)
{
if(a[i][j] == 'X')
temp1++;
if(a[i][j] == 'O')
temp2++ ;
if(a[i][j] == 'T')
temp3++ ;
}
if(temp1 == 3  && temp3 == 1)
return 1;
if(temp2 == 3  && temp3 == 1)
return 2 ;
}




//checking diaognals
temp1 = 0 ;
temp2 = 0 ;
temp3 = 0 ;
for(j=0;j<4;j++)
{
if(a[j][j] == 'X')
temp1++;
if(a[j][j] == 'O')
temp2++ ;
if(a[j][j] == 'T')
temp3++ ;
}
if(temp1 == 3  && temp3 == 1)
return 1;
if(temp2 == 3  && temp3 == 1)
return 2 ;

temp1 = 0 ;
temp2 = 0 ;
temp3 = 0 ;
for(j=0;j<4;j++)
{
if(a[j][3-j] == 'X')
temp1++;
if(a[j][3-j] == 'O')
temp2++ ;
if(a[j][3-j] == 'T')
temp3++ ;
}
if(temp1 == 3  && temp3 == 1)
return 1;
if(temp2 == 3  && temp3 == 1)
return 2 ;


if(count1)
return 4;
else
return 3;


}


int main()
{
int t ,i , j=1 , k ,x,y,count1 , count2 , var = 1 ;
FILE *f1 , *f2 ;
f1 = fopen("inputques1large.txt", "r");
f2 = fopen("outputques1large.txt", "w");
fscanf(f1,"%d",&t);
char a[4][4] , z ;
while(t--)
{

count1 = 0 ;
count2 = 0;
x = -1 ; y = -1 ;
    for(i=0 ; i<4 ; i++ )
    {
    fscanf(f1,"%c",&z);
    for( j=0 ; j<4 ; j++)
    {
    fscanf(f1,"%c",&a[i][j]);
        if(a[i][j] == '.')
        count1++;
        if(a[i][j] == 'T')
        {
        count2++;
        x=i;y=j;
        }
    }
    }
    fscanf(f1,"%c",&z);

switch(tictactoe(a , count1 , count2 , x , y ))
{
case 1:fprintf(f2,"Case #%d: X won",var);
                   break ;
case 2:fprintf(f2,"Case #%d: O won",var);
                   break ;
case 3:fprintf(f2,"Case #%d: Draw",var);
                   break ;
case 4:fprintf(f2,"Case #%d: Game has not completed",var);
}
if(t>0)
fprintf(f2,"\n");
var++;
}
fclose(f1);
fclose(f2);
return 0;
}
 
