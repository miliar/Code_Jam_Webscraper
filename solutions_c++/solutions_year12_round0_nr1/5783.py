#include<stdio.h>
#include<iostream>
using namespace std;
int main()
{
char str[10500];
char arr[26][1];
arr[0][0]='y';
arr[1][0]='h';
arr[2][0]='e';
arr[3][0]='s';
arr[4][0]='o';
arr[5][0]='c';
arr[6][0]='v';
arr[7][0]='x';
arr[8][0]='d';
arr[9][0]='u';
arr[10][0]='i';
arr[11][0]='g';
arr[12][0]='l';
arr[13][0]='b';
arr[14][0]='k';
arr[15][0]='r';
arr[16][0]='z';
arr[17][0]='t';
arr[18][0]='n';
arr[19][0]='w';
arr[20][0]='j';
arr[21][0]='p';
arr[22][0]='f';
arr[23][0]='m';
arr[24][0]='a';
arr[25][0]='q';
int t;
scanf("%d",&t);
getchar();
int y=0;
while(t--)
{
y++;
int i=0;
//char c;

gets(str);
//printf("%s\n",str);
while(str[i]!='\0')
{
   if(str[i]!=' ')
str[i]=arr[str[i]-'a'][0];
i++;
//printf("%c",str[i-1]);
}
printf("Case #%d: %s",y,str);
printf("\n");
}
return 0;
}
