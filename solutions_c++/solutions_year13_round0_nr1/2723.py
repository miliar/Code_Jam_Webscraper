using namespace std;
#include<iostream>
#define Max 1000 + 5
 
char matrix[Max][Max];
bool check;
int i,j;
 
int row() 
{
bool XWin = false;
bool OWin = false;
int count = 0;
for(i=0;i<4;i++) 
{
for(j=0;j<4;j++)
{
if(matrix[i][j] == 'X' || matrix[i][j] == 'T') 
count++;
}
if(count == 4) 
XWin = true;
count = 0;
}
count = 0;
for(i=0;i<4;i++) 
{
for(j=0;j<4;j++)  
{
if(matrix[i][j] == 'O' || matrix[i][j] == 'T')  
count++;
}
if(count == 4) 
OWin = true;
count = 0;
}
if(XWin && OWin)                 
return 3;
else if(!XWin && OWin)           
return 2;
else if(XWin && !OWin)           
return 1;
else                             
return 0;
}
 
int column() 
{
bool XWin = false;
bool OWin = false;
int count = 0;
for(i=0;i<4;i++) 
{
for(j=0;j<4;j++) 
{
if(matrix[j][i] == 'X' || matrix[j][i] == 'T') 
count++;
}
if(count == 4) 
XWin = true;
count = 0;
}
count = 0;
for(i=0;i<4;i++) 
{
for(j=0;j<4;j++)
{
if(matrix[j][i] == 'O' || matrix[j][i] == 'T')  
count++;
}
if(count == 4) 
OWin = true;
count = 0;
}
if(XWin && OWin)                 
return 3;
else if(!XWin && OWin)           
return 2;
else if(XWin && !OWin)           
return 1;
else                             
return 0;
}
 
int diagonal() 
{
bool XWin = false;
bool OWin = false;
if((matrix[0][0] == 'X' || matrix[0][0] == 'T') && (matrix[1][1] == 'X' || matrix[1][1] == 'T') && (matrix[2][2] == 'X' || matrix[2][2] == 'T') && (matrix[3][3] == 'X' || matrix[3][3] == 'T'))
XWin = true;
if((matrix[0][0] == 'O' || matrix[0][0] == 'T') && (matrix[1][1] == 'O' || matrix[1][1] == 'T') && (matrix[2][2] == 'O' || matrix[2][2] == 'T') && (matrix[3][3] == 'O' || matrix[3][3] == 'T'))
OWin = true;
if((matrix[0][3] == 'X' || matrix[0][3] == 'T') && (matrix[1][2] == 'X' || matrix[1][2] == 'T') && (matrix[2][1] == 'X' || matrix[2][1] == 'T') && (matrix[3][0] == 'X' || matrix[3][0] == 'T'))
XWin = true;
if((matrix[0][3] == 'O' || matrix[0][3] == 'T') && (matrix[1][2] == 'O' || matrix[1][2] == 'T') && (matrix[2][1] == 'O' || matrix[2][1] == 'T') && (matrix[3][0] == 'O' || matrix[3][0] == 'T'))
OWin = true;
if(XWin && OWin)                 
return 3;
else if(!XWin && OWin)           
return 2;
else if(XWin && !OWin)           
return 1;
else                             
return 0;
}
 
int main() 
{
freopen("A-large.in", "r", stdin);
freopen("output1.txt", "w", stdout);
int test,k;
scanf("%d",&test);
k=1;
cin.ignore();
while(test--) 
{
check = true;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++) 
{
cin>>matrix[i][j];
if(matrix[i][j] == '.') 
check = false;
}
}
int c_row = row();
int c_col = column();
int c_diagonal = diagonal();
printf("Case #%d: ",k++);
if(c_row == 1) 
{
printf("X won\n");
continue;
}
if(c_row == 2) 
{
printf("O won\n");
continue;
}
if(c_col == 1) 
{
printf("X won\n");
continue;
}
if(c_col == 2) 
{
printf("O won\n");
continue;
}
if(c_diagonal == 1) 
{
printf("X won\n");
continue;
}
if(c_diagonal == 2) 
{
printf("O won\n");
continue;
}
if(!check) 
{
printf("Game has not completed\n");
continue;
}
printf("Draw\n");
}     
return 0;
}
