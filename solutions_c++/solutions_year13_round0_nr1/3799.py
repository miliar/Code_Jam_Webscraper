#include<fstream.h>
#include<conio.h>
char a[4][4];
void status(int &res)
{
 int x=0,y=0,t=0,d=0;
 for(int i=0;i<4;i++)
 {
  for(int j=0;j<4;j++)
  {
   x=0,y=0,t=0;
   for(int k=j;k<4;k++)
   {
    if(a[i][k]=='X')
     x+=1;
    if(a[i][k]=='O')
     y+=1;
    if(a[i][k]=='T')
     t=1;
    if(a[i][k]=='.')
     d=1;
   }
   if((x==4)||(x==3 && t==1))
   { res=1;
    goto z;
   }
   else if((y==4)||(y==3 && t==1))
   { res=2;
    goto z;
   }
   if(i==0)
   {
    x=0,y=0,t=0;
    for(int k=i;k<4;k++)
    {
     if(a[k][j]=='X')
      x+=1;
     if(a[k][j]=='O')
      y+=1;
     if(a[k][j]=='T')
      t=1;
     if(a[k][j]=='.')
      d=1;
    }
    if((x==4)||(x==3 && t==1))
     {
      res=1;
      goto z;
     }
    else if((y==4)||(y==3 && t==1))
     {
      res=2;
      goto z;
     }
    x=0,y=0,t=0;
    if(j==0)
    {
     int l=j;
     for(int k=i;k<4;k++)
     {
      if(a[k][l]=='X')
       x+=1;
      if(a[k][l]=='O')
       y+=1;
      if(a[k][l]=='T')
       t=1;
      if(a[k][l]=='.')
       d=1;
      l++;
     }
     if((x==4)||(x==3 && t==1))
      {res=1;
       goto z;
       }
     else if((y==4)||(y==3 && t==1))
      {res=2;
       goto z;
      }
    }
    if(j==3)
    {
     int l=j;
     for(int k=i;k<4;k++)
     {
      if(a[k][l]=='X')
       x+=1;
      if(a[k][l]=='O')
       y+=1;
      if(a[k][l]=='T')
       t=1;
      if(a[k][l]=='.')
       d=1;
      l--;
     }
     if((x==4)||(x==3 && t==1))
     { res=1;
      goto z;
      }
     else if((y==4)||(y==3 && t==1))
     { res=2;
       goto z;
      }
    }
   }
  }
 }
 if(d==1)
  res=4;
 else
  res=3;
 z:
}
void main()
{
 clrscr();
 ifstream Ifile;
 Ifile.open("ALARGE.IN",ios::in);
 ofstream Ofile("RESULT.TXT",ios::out);
 int T;

 Ifile>>T;
 int l=0,i=0,j=0;
 char ch;
 int *result;
 result=new int[T];
 while(Ifile)
 {
  Ifile.get(ch);
  if(ch!='\n')
  {
   a[i][j]=ch;
   if(i==3 && j==3)
   {
    l+=1;
    status(result[l-1]);
    i=0;
    j=-1;
   }
   j+=1;
   if(j==4)
   {
    j=0;
    i+=1;
   }
  }
 }
 for(int y=1;y<=T;y++)
 {
  Ofile<<"\nCase #"<<y<<": ";
  cout<<"\nCase #"<<y<<": ";
  if(result[y-1]==1)
  {
   Ofile<<"X won";
   cout<<"X won";
  }
  else if(result[y-1]==2)
  {
   Ofile<<"O won";
   cout<<"O won";
  }
  if(result[y-1]==3)
  {
   Ofile<<"Draw";
   cout<<"Draw";
  }
  if(result[y-1]==4)
  {
   Ofile<<"Game has not completed";
   cout<<"Game has not completed";
  }
 }
 Ofile.close();
 delete [] result;
}