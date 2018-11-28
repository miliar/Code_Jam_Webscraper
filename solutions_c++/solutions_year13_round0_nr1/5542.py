#include<stdio.h>
#include<iostream>
#include<fstream>

using namespace std;
int main()
{
#ifndef ONLINE_JUDGE
 freopen("a.txt","r",stdin);
#endif

 int t,i,j,final=0;


char tic[4][4]={};

cin>>t;
while(t--)
{

int count=0;
//tic[4][4]='p';
 for(i=0;i<4;i++)
 for(j=0;j<4;j++)
  cin>>tic[i][j];
i=0;

//row wise checking

a:
int rx=0,ro=0;

for(j=0;j<4;j++)
 if(tic[i][j]=='X'|| tic[i][j]=='T')
   rx++;
for(j=0;j<4;j++)
 if(tic[i][j]=='O'|| tic[i][j]=='T')
   ro++;
if(rx==4)
{
 cout<<"Case #"<<final+1<<": "<<"X won"<<endl;
 final++; 
 continue;
}
else if(ro==4)
{
 cout<<"Case #"<<final+1<<": "<<"O won"<<endl;
  final++; 
continue;
}
else if(i<4)
 {
i++;
goto a;
}

//column wise checking
i=0;
b:
int cx=0,co=0;

for(j=0;j<4;j++)
 if(tic[j][i]=='X'||tic[j][i]=='T')
   cx++;
for(j=0;j<4;j++)
 if(tic[j][i]=='O'||tic[j][i]=='T')
   co++;
if(cx==4)
{
 cout<<"Case #"<<final+1<<": "<<"X won"<<endl;final++; 

  continue;
}
else if(co==4)
{
 cout<<"Case #"<<final+1<<": "<<"O won"<<endl;
 final++; 
  continue;
}
else if(i<4)
 {
i++;
goto b;
}

//normal diagonal
int dx=0,doo=0;

for(i=0;i<4;i++)
  if(tic[i][i]=='X' || tic[i][i]=='T')
    dx++;
for(i=0;i<4;i++)
  if(tic[i][i]=='O' || tic[i][i]=='T')
    doo++;
if(dx==4)
{
 cout<<"Case #"<<final+1<<": "<<"X won"<<endl;final++; 

  continue;
}
if(doo==4)
{
 cout<<"Case #"<<final+1<<": "<<"O won "<<endl;final++; 

  continue;
}
//reverse diagonal
 dx=0;
doo=0;

for(i=0;i<4;i++)
  if(tic[i][3-i]=='X' || tic[i][3-i]=='T')
    dx++;
for(i=0;i<4;i++)
  if(tic[i][3-i]=='O' || tic[i][3-i]=='T')
    doo++;
if(dx==4)
{
 cout<<"Case #"<<final+1<<":"<<"X won"<<endl;final++; 

  continue;
}
if(doo==4)
{
 cout<<"Case #"<<final+1<<": "<<"O won"<<endl;final++; 

  continue;
}
// game draw or not completed
for(i=0;i<4;i++)
  for(j=0;j<4;j++)
    if(tic[i][j]=='X' || tic[i][j]=='O' || tic[i][j]=='T')
      count++;
if(count==16)
  {
 cout<<"Case #"<<final+1<<": "<<"Draw"<<endl;
final++; 
continue;
}

else
{
    cout<<"Case #"<<final+1<<": "<<"Game has not completed"<<endl;

final++;
continue;
}

}
return 0;
}


