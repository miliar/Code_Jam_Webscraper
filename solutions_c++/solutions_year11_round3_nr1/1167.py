#include<iostream.h>
#include<conio.h>
#include<fstream.h>

void main()
{
  clrscr();
  char a[55][55];
  int t,r,c,i,j,k,flag;
  ifstream fin("tile1.txt");
  ofstream fout("output1.txt");
  fin>>t;
  for(i=0;i<t;i++)
  {
     flag=0;
     fin>>r;
     fin>>c;
     for(j=0;j<r;j++)
       for(k=0;k<c;k++)
	  fin>>a[j][k];
    for(j=0;j<r-1;j++)
    {
       for(k=0;k<c-1;k++)
       {
	  if(a[j][k]=='.')
	    continue;
	  else if(a[j][k]=='#')
	  {
	    if(a[j][k]=='#' && a[j][k+1]=='#' && a[j+1][k]=='#' && a[j+1][k+1]=='#')
	    {
	       a[j][k]='/';
	       a[j][k+1]='\\';
	       a[j+1][k]='\\';
	       a[j+1][k+1]='/';
	    }
	  }
       }
    }
    for(j=0;j<r;j++)
      for(k=0;k<c;k++)
	if(a[j][k]=='#')
	{
	  flag=1;
	  break;
	}
    if(flag==1)
      fout<<"Case #"<<i+1<<": \n"<<"Impossible\n";
    else
    {
      fout<<"Case #"<<i+1<<": \n";
      for(j=0;j<r;j++)
      {	for(k=0;k<c;k++)
	  fout<<a[j][k];
	fout<<"\n";
      }
    }
  }
}