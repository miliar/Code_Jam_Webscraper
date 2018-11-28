#include<iostream.h>
#include<conio.h>
#include<fstream.h>
void main(){

clrscr();
//int* N=new int[T];

ofstream outfile;
outfile.open("output.txt");
ifstream input;
input.open("input.txt");


int T;
input>>T;


for(int i=0;i<T;i++)
{
int N;
input>>N;
int R;
input>>R;
int C;
input>>C;
char **t=new char*[R];
for(int j=0;j<R;j++)
{

t[j]=new char[C];
for(int k=0;k<C;k++)
{
input>>t[j][k];
}
}
int found=0;
for(j=0;j<R;j++)
{

//t[j]=new char[C];
for(int k=0;k<C;k++)
{
if(t[j][k]=='#')
{
  if(j+1!=R&&k+1!=C&&t[j+1][k]=='#'&&t[j][k+1]=='#'&&t[j+1][k+1]=='#')
  {
   t[j][k]='/';
   t[j+1][k]='/';
   t[j][k+1]=92;
   t[j+1][k+1]=92;

  }
  else
  {
   found=1;
   break;
  }
}
//input>>t[j][k];

}

}



outfile<<"Case #"<<i+1<<":"<<endl;

if(found==1)
outfile<<"Impossible";
else
{
 for(j=0;j<R;j++)
{

//t[j]=new char[C];
for(int k=0;k<C;k++)
{
outfile<<t[j][k];

}
outfile<<endl;
}

}
cout<<"Case #"<<i<<": "<<clock<<endl;

}
outfile.close();
getch();

}