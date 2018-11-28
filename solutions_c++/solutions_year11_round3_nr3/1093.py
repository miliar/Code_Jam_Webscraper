#include<iostream.h>
#include<conio.h>
#include<fstream.h>

void main()
{
  int t,n,l,h,f[120],j,k,fg;
  ifstream fin("input.txt");
  ofstream fout("output.txt");
  fin>>t;
  for(int i=0;i<t;i++)
  {
    fg=0;
    fin>>n;
    fin>>l;
    fin>>h;
    for(j=0;j<n;j++)
      fin>>f[j];
    for(j=l;j<=h;j++)
    {
      fg=0;
      for(k=0;k<n;k++)
      {
	 if(j>f[k])
	 {
	   if(j%f[k]!=0)
	   {  fg=1;
	      break;
	   }

	 }
	 else
	 {
	   if(f[k]%j!=0)
	   {
	     fg=1;
	     break;
	   }
	 }
      }
      if(fg==0)
	break;
    }
    if(fg==0)
    fout<<"Case #"<<i+1<<": "<<j<<"\n";
    else
    fout<<"Case #"<<i+1<<": "<<"NO\n";
} }