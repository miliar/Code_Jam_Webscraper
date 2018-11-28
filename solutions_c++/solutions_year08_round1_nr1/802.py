#include<fstream.h>
#include<iostream.h>
#include<conio.h>
#include<ctype.h>
#include<math.h>
#include<string.h>
#include<stdio.h>
void sort(long ar[],int n)
{
   for(int i=0;i<n-1;i++)
   {
     for(int j=i+1;j<n;j++)
       if(ar[i]>ar[j])
       {
	  int temp=ar[i];
	  ar[i]=ar[j];
	  ar[j]=temp;
       }
   }
}
void revsort(long ar[],int n)
{
   for(int i=0;i<n-1;i++)
   {
     for(int j=i+1;j<n;j++)
       if(ar[i]<ar[j])
       {
	  int temp=ar[i];
	  ar[i]=ar[j];
	  ar[j]=temp;
       }
   }
}

int main()
{
   int nc;
   ifstream fin("A-large.in");
   remove("Out.txt");

   ofstream fout("Out.txt");
   if(!fin)
   {
      cout<<"File nahi khuli";
      getch();
      return 1;
   }
   fin>>nc;
   for(int c=0;c<nc;c++)
   {
      fout<<"Case #"<<c+1<<": ";
      int n,i;
      long a[1000],b[1000],sol=0;
      fin>>n;
      for(i=0;i<n;i++)
	 fin>>a[i];
      for(i=0;i<n;i++)
	 fin>>b[i];
      sort(a,n);
      revsort(b,n);
      for(i=0;i<n;i++)
	 sol+=a[i]*b[i];
      fout<<sol<<"\n";

   }
   fin.close();
   fout.close();
   getchar();
   return 0;
}
