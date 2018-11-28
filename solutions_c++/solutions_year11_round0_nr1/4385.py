#include<iostream.h>
#include<conio.h>
#include<fstream.h>

void main()
{
  ifstream fin("test.txt");
  ofstream fout("alarge1.txt");
  char c[100];
  int a[100],count=0,x,y,hit,p1,p2,d1,d2,hitc,l,m,n,fg;
  long time;
  fin>>x;
  while(x>count)
  {
    fin>>y;
    hit=0;
    for(int i=0;i<y;i++)
    {
      fin>>c[i];
      fin>>a[i];
    }
    time=0;
    p1=1;p2=1;d1=0;d2=0;
    l=0;m=0;n=0;fg=0;
    while(hit<y)
    {
      time++;
      if(d1==0)
      {
	while(c[l]!='O')
	{
	  if(l<y-1)
	    l++;
	  else
	    break;
	}
	d1=a[l];
	l++;
      }
      if(d2==0)
      {
	while(c[m]!='B')
	{
	  if(m<y-1)
	    m++;
	  else
	    break;
	}
	d2=a[m];
	m++;
      }
      if(c[n]=='O' && fg==0)
      {
	hitc=0;
	n++;
	fg=1;
      }
      else if(c[n]=='B' && fg==0)
      {
	hitc=1;
	n++;
	fg=1;
      }
      if(p1==d1 && hitc==0)
      {
	hit++;
	p1=d1;
	fg=0;
	d1=0;
	if(p2<d2)
	  p2++;
	else if(p2>d2)
	  p2--;
      }
      if(p2==d2 && hitc==1)
      {
	hit++;
	p2=d2;
	fg=0;
	d2=0;
	if(p1<d1)
	  p1++;
	else if(p1>d1)
	  p1--;
      }
      if(fg==1)
      {
	if(p2<d2)
	  p2++;
	else if(p2>d2)
	  p2--;
	if(p1<d1)
	  p1++;
	else if(p1>d1)
	  p1--;
      }
    }
    fout<<"Case #"<<count+1<<": "<<time<<"\n";
    count++;
  }
}
