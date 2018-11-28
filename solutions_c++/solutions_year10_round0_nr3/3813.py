#include<iostream.h>
#include<conio.h>
#include<stdio.h>
#include<fstream.h>

double fare(double r, double k, double n[10],int li);
void main()
{ clrscr();
 int t,size;
 double r,k,n[10],res;
 fstream fin,fout;
 fin.open("input.txt",ios::in);
 fout.open("output.txt",ios::out);
 fin>>t;
for(int times=0;times<t;times++)
{
   fin>>r;
   fin>>k;
   fin>>size;
  for(int i=0;i<size;i++)
  fin>>n[i];//={2,4,2,3,4,2,1,2,1,3};
   res=fare(r,k,n,size);
   fout<<"Case#:"<<(times+1)<<": "<<res<<endl;
 //cout<<t<<" "<<r<<" "<<k<<" "<<size;
}

 fin.close();
 fout.close();
 getch();
}

double fare(double r,double k, double n[10],int li)
{ double temp=0,total=0;
  int pos=0;

  for(int i=0;i<li;i++)
   temp+=n[i];

  if(temp<=k)   // if grp size <=k
   return (r*temp);

  temp=0;

  for(i=1;i<=r;i++)
  {   temp=0;
     while(temp<=k)
     { temp+=n[pos];
	 if(temp>k)
	   break;
       if(pos==li-1)
	 pos=0;
       else
	 pos++;
     }//end of while

       total+=temp-n[pos];

  }//end of for

     return total;

  }    //end of function
