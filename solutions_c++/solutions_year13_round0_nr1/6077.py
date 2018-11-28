# include<iostream>
using namespace std;
int main()
{
int i,j,k,t,o=0,x=0,y=0;
char a[5][5];
cin>>t;
for(k=1;k<=t;k++)
{
y=0;
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
cin>>a[i][j];
}
}
for(i=0;i<4;i++)
{
o=0;
x=0;
for(j=0;j<4;j++)
{
if(a[i][j]=='T')
{
o++;
x++;
}
else if(a[i][j]=='O')
o++;
else if(a[i][j]=='X')
x++;
if(o==4)
y=1;
if(x==4)
y=2;
}
}
if(y==0)
{
for(i=0;i<4;i++)
{
o=0;
x=0;
for(j=0;j<4;j++)
{
if(a[j][i]=='T')
{
o++;
x++;
}
else if(a[j][i]=='O')
o++;
else if(a[j][i]=='X')
x++;
if(o==4)
y=1;
if(x==4)
y=2;
}
}
}
o=0;
x=0;
if(y==0)
{
for(i=0;i<4;i++)
{
if(a[i][i]=='T')
{
o++;
x++;
}
else if(a[i][i]=='O')
o++;
else if(a[i][i]=='X')
x++;
if(o==4)
y=1;
if(x==4)
y=2;
}
}
o=0;
x=0;
if(y==0)
{
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if((i+j)==3)
{
if(a[i][j]=='T')
{
o++;
x++;
}
else if(a[i][j]=='O')
o++;
else if(a[i][j]=='X')
x++;
if(o==4)
y=1;
if(x==4)
y=2;
}
}
}
}
if(y==1)
{
cout<<"Case #"<<k<<": "<<"O won"<<"\n";

}
else if(y==2)
{
cout<<"Case #"<<k<<": "<<"X won"<<"\n";

}
else
{
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(a[i][j]=='.')
y=3;
}
}

if(y==3)
cout<<"Case #"<<k<<": "<<"Game has not completed"<<"\n";
else
cout<<"Case #"<<k<<": "<<"Draw"<<"\n";
}
}
return 0;
}
