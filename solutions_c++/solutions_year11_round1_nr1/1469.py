#include<iostream.h>
#include<conio.h>
#include<fstream.h>

void main()
{
  clrscr();
  ifstream fin("asmall.txt");
  ofstream fout("output.txt");
  double n;
  int pd,pg,t,d,g,wd,wg;
  int flag=0;
  fin>>t;
  for(int i=0;i<t;i++)
  {
    flag=0;
    fin>>n;
    fin>>pd;
    fin>>pg;
    cout<<i+1<<") "<<n<<" "<<pd<<" "<<pg<<"\n";
    for(int j=1;j<=n;j++)
    {
      wd = (pd * j);
      if(wd%100 !=0)
	continue;
      wd = wd / 100;
      if(wd==0 && pg<100)
      {
	flag=1;
	break;
      }
      else if(wd>0 && pg>0 && pg<100)
      {
	flag=1;
	break;
      }
      else if(wd>0 && pg==100)
      {
	if(wd==j)
	{
	  flag=1;
	  break;
	}
      }
    }
    if(flag==0)
     fout<<"Case #"<<i+1<<": Broken\n";
    else
     fout<<"Case #"<<i+1<<": Possible\n";




  }
  getch();
}