#include <iostream>
# include <string.h>
#include <stdio.h>
using namespace std;

int main()
{
    int N=10, L=10;
    FILE *f;
    if((f=fopen("lol.txt","r"))==NULL)
    {
        printf("er.\n");
//        exit(1);
    }

    FILE *fp;

    fp=fopen("lolo.txt","w+");

    char **c;
    int i=0, a=0;
    c=new char*[7];
    for(i=0;i<7;i++)
    c[i]=new char[5];
    char cc[100];
    int M=3;
    fgets(cc,M,f);
    for(i=0;i<M;i++)
    if(cc[i]>='0'&&cc[i]<='9')
    a=a*10+cc[i]-'0';
int k,j,x=0,y=0,v=0,h=0;
int OW=0,XW=0;
    cout<<a;
int count=0;
char ch;
//ch=getc(f);
    while(count<a)
    {
      /*  while(i==4)
        {
        while(ch!='\n')
        {
            c[i][l]=ch;
            l++;
            ch=getc(f);
        }
        i++;
        l=0;
        ch=getc(f);
        }
        //if(i==4)
        ch=getc(f);
        i=0;
        ch=getc(f);*/
        for(i=0;i<5;i++)
        {
            fgets(c[i],6,f);
           // printf("%s",c[i]);
        }
//ch=getc(f);
for(k=1;k<5;k++)
{
for(j=0;j<4;j++)
{
    if(c[k][j]=='.')
    v++;
}
}
/*
for(k=1;k<5;k++)
{
for(j=0;j<5;j++)
{
h=k-1;
    if((h==j && c[h][j]=='O') || (h==j && (c[h][j]=='T' ||c[h][j]=='O')))
    {
        x++;
    }
    if(x==4)
    {
   // cout<<"O win";
    OW=1;
    x=0;}

    if((h==j && c[h][j]=='X') || (h==j && (c[h][j]=='T' ||c[h][j]=='X')))
    {
        y++;
    }
    if(y==4)
    {
   // cout<<"X win";
    XW=1;
    y=0;}
}
}
*/
x=0;
y=0;

for(k=1;k<5;k++)
{
for(j=0;j<5;j++)
{
    if(c[k][j]=='X' || (c[k][j]=='T' ||c[k][j]=='X'))
    {
        y++;
    }
    if(y==4)
    {
    //cout<<"O win";
    XW=1;
    y=0;
    }

     if(c[k][j]=='O' || (c[k][j]=='T' ||c[k][j]=='O'))
    {
        x++;
    }
    if(x==4)
    {
   // cout<<"X win";
   OW=1;
    x=0;
    }
}
x=0;
y=0;
}
x=0;
y=0;

for(k=1;k<5;k++)
{
for(j=0;j<5;j++)
{
    if(c[j][k]=='O' || (c[j][k]=='T' ||c[j][k]=='O'))
    {
        x++;
    }
    if(x==4)
    {
    //cout<<"O win";
    OW=1;
    x=0;
    }

     if(c[j][k]=='X' || (c[j][k]=='T' ||c[j][k]=='X'))
    {
        y++;
    }
    if(y==4)
    {
  // cout<<"X win";
    XW=1;
    y=0;
    }

}
x=0;
y=0;
}
x=0;
y=0;

for(k=1;k<5;k++)
{
    if(c[k][4-k]=='O' || (c[k][4-k]=='T' ||c[k][4-k]=='O'))
{
    x++;
}
if(x==4)
OW=1;

if(c[k][4-k]=='X' || (c[k][4-k]=='T' ||c[k][4-k]=='X'))
{
    y++;
}
if(y==4)
XW=1;
}
x=0;
y=0;

for(k=1;k<5;k++)
{
    if(c[k][k-1]=='O' || (c[k][k-1]=='T' ||c[k][k-1]=='O'))
{
    x++;
}
if(x==4)
OW=1;

if(c[k][k-1]=='X' || (c[k][k-1]=='T' ||c[k][k-1]=='X'))
{
    y++;
}
if(y==4)
XW=1;
}
x=0;
y=0;



if(XW==1)
{
  //  cout<<"X win"<<count<<endl;
    fprintf(fp,"Case #%d: X won\n",count+1);
}
else if(OW==1)
{
   // cout<<"O win"<<count<<endl;
    fprintf(fp,"Case #%d: O won\n",count+1);
}
else if(XW==0 && OW==0 && v==0)
{
   // cout<<"nichia"<<count<<endl;
    fprintf(fp,"Case #%d: Draw\n",count+1);
}
else if(v>0 && XW==0 && OW==0){//cout<<"ne doigr"<<count<<endl;
fprintf(fp,"Case #%d: Game has not completed\n",count+1);
}
XW=0;
OW=0;


v=0;
//cout<<v;
      //  printf("%s",c[0]);
      cout<<endl<<count<<endl;
      for(k=1;k<5;k++)
{
for(j=0;j<5;j++)
{
    cout<<c[k][j];
}
//cout<<endl;
}
count++;
    }

    fclose(f);
fclose(fp);

//or(i=0;i<6;i++)
   // printf("%s",c[i]);
//printf("%s",c[0]);

    return 0;
}
