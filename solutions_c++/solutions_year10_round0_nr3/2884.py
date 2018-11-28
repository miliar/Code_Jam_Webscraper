# include<fstream.h>
# include <conio.h>
# include <string.h>
# include <stdio.h>
int num[10000], w;
void sort(int l)
{ int b[1000],k=0;
for(int i=1;i<=l;i++)
b[i]=num[i];
for( i=1;i<=w;i++)
 if(i+l<=w)
  num[i]=num[i+l];
 else
   num[i]=b[k++];
}
void main()
{
  clrscr();
  ifstream infile("in3.in",ios::in);
  ofstream outfile("zli.out",ios::out);
  int k,r,n;
  infile >> n;
  int sum=0;
  for(int i=1;i<=n;i++)
  {
    infile >>r;
    infile >>k;
    infile >>w;
    for(int j=1;j<=w;j++)
    {
     infile >>num[j];
    }
    int rider =0;
    for( j=1;j<=w;j++)
    {
     rider+=num[j];
     if(rider < k && rider+num[j+i] >k)
       {
	sum +=rider;
	}
	sort(j);
    cout <<"value of rider"<<rider<<endl;
    }
     outfile<<"Case #"<<i<<" "<<rider<<"\n";
  }
  getch();
  }