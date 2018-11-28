#include<fstream.h>
#include<conio.h>
#include<math.h>
#include<string.h>
#include<stdio.h>
char ch;
int na,nb,a[200][2],b[200][2],mix[400][2],k=0;
int getno(char str[])
{
   int x=(str[0]-48)*10+(str[1]-48);
   return x;
}
void sort()
{
   for(int i=0;i<k-1;i++)
   {
      for(int j=i+1;j<k;j++)
      {
	 if(mix[i][0]>mix[j][0]||(mix[i][0]==mix[j][0] && j%2==1))
	 {
	    int t=mix[i][0];
	    mix[i][0]=mix[j][0];
	    mix[j][0]=t;
	    t=mix[i][1];
	    mix[i][1]=mix[j][1];
	    mix[j][1]=t;

	 }
      }
   }
  /* for(i=0;i<nb-1;i++)
   {
      for(int j=i+1;j<nb;j++)
      {
	 if(b[i][1]>b[j][1])
	 {
	    int t=b[i][0];
	    b[i][0]=b[j][0];
	    b[j][0]=t;
	    t=b[i][1];
	    b[i][1]=b[j][1];
	    b[j][1]=t;

	 }
      }
   }*/
}
/*void sort1()
{
   for(int i=0;i<na-1;i++)
   {
      for(int j=i+1;j<na;j++)
      {
	 if(a[i][0]>a[j][0])
	 {
	    int t=a[i][0];
	    a[i][0]=a[j][0];
	    a[j][0]=t;
	    t=a[i][1];
	    a[i][1]=a[j][1];
	    a[j][1]=t;
	 }
      }
   }
   for(i=0;i<nb-1;i++)
   {
      for(int j=i+1;j<nb;j++)
      {
	 if(b[i][0]>b[j][0])
	 {
	    int t=b[i][0];
	    b[i][0]=b[j][0];
	    b[j][0]=t;
	    t=b[i][1];
	    b[i][1]=b[j][1];
	    b[j][1]=t;

	 }
      }
   }
}

int findel(int nxt,int a[][2],int n)
{
    sort1();
    if(n==1)
      n=na;
    else
      n=nb;
    for(int pos=0;pos<n && a[pos][0]<nxt;pos++);

    if(pos==n)
    {
       sort();
       return -1;
    }
    int ret=a[pos][1];
    for(int i=pos;i<n-1;i++)
    {
       a[i][0]=a[i+1][0];
       a[i][1]=a[i+1][1];
    }
    sort();
    return ret;
} */
int findel(int mix[][2],int val)
{
      if(mix[0][0]==val)
      {
	 int code=mix[0][1];
	 for(int j=0;j<k-1;j++)
	 {
	   mix[j][0]=mix[j+1][0];
	   mix[j][1]=mix[j+1][1];
	 }
	 return code;
      }
   return -1;
}
void inc(int time[][2],int loc,int a)
{
   for(int i=loc;i<1440;i++)
   {
      time[i][a]++;
   }
}
void dec(int time[][2],int loc,int a)
{
   for(int i=loc;i<1440;i++)
   {
      if(time[i][a]>0)
	 time[i][a]--;
   }
}
void disp()
{
    cout<<endl;
    for(int i=0;i<k;i++)
       cout<<mix[i][0]<<" "<<mix[i][1]<<" ";
    cout<<"\n\n";
}
void disp(int time[][2])
{
/*   for(int i=1204;i<1287;i++)
    cout<<time[i][0]<<" "<<time[i][1]<<"  ";*/

}
int main()
{
   clrscr();
   int nc;
   ifstream fin("B-small.in");
   remove("Out.txt");
   if(!fin)
   {
      cout<<"File nahi khuli";
      getch();
      return 1;
   }
   fin>>nc;
   for(int c=0;c<nc;c++)
   {
      char str[100];
      ofstream fout("Out.txt",ios::app);
      fout<<"Case #"<<c+1<<": ";
      int t,h,m;
      fin>>t>>na>>nb;
      cout<<t<<" "<<na<<" "<<nb;
      fin.getline(str,80);
      for(int i=0;i<na;i++)
      {
	 fin.getline(str,80);
	 cout<<str<<endl;
	 h=getno(str);
	 m=getno(str+3);
	 a[i][0]=h*60+m;
	 mix[k][0]=a[i][0];
	 mix[k++][1]=0;
	 h=getno(str+6);
	 m=getno(str+9);
	 a[i][1]=h*60+m;
	 mix[k][0]=a[i][1];
	 mix[k++][1]=1;

      }
      for(i=0;i<nb;i++)
      {
	 fin.getline(str,80);
	 cout<<str<<endl;
	 h=getno(str);
	 m=getno(str+3);
	 b[i][0]=h*60+m;
	 mix[k][0]=b[i][0];
	 mix[k++][1]=2;

	 h=getno(str+6);
	 m=getno(str+9);
	 b[i][1]=h*60+m;
	 mix[k][0]=b[i][1];
	 mix[k++][1]=3;

      }

      sort();
      disp();
      int l=0,mu=0,time[2400][2]={0};

      for(i=0;i<1440;i++)
      {
	 int code=77;
	 while(code!=-1)
	 {
	    code=findel(mix,i);
	    if(code!=-1)
	    {
	       disp(time);
	       k--;
	       cout<<i<<" "<<code<<" ";
	    }
	    switch(code)
	    {
	       case 0:
	       if(time[i][0]==0)
	       {
		  l++;
	       }
	       else
		  dec(time,i,0);
	       break;

	       case 1:
	       inc(time,i+t,1);
	       break;

	       case 2:
	       if(time[i][1]==0)
	       {
		  mu++;
	       }
	       else
		  dec(time,i,1);
	       break;

	       case 3:
	       cout<<code;
	       inc(time,i+t,0);
	       break;

	       default:
	       break;
	    }
	    if(k==0)
	      break;
	 }
	 if(k==0)
	  break;
      }


      /*for(i=0;i<na;i++)
      {
	 cout<<"-------------";
	 int nxt=a[i][1]+t;
	 while(nxt!=-1)
	 {
	    disp(a,b);
	    nxt=findel(nxt,b,2);
	    if(nxt==-1)
	      break;
	    else
	    {
	      nxt+=t;
	      nb--;
	    }
	    nxt=findel(nxt,a,1);
	    if(nxt!=-1)
	    {
	      na--;
	      nxt+=t;
	    }

	 }
      }
      for(i=0;i<nb;i++)
      {
	 cout<<"----------";
	 int nxt=b[i][1]+t;
	 while(nxt!=-1)
	 {
	    disp(a,b);
	    nxt=findel(nxt,a,1);
	    if(nxt==-1)
	      break;
	    else
	    {
	       nxt+=t;
	       na--;
	    }
	    nxt=findel(nxt,b,2);
	    if(nxt!=-1)
	    {
	      nb--;
	      nxt+=t;
	    }
	 }
      } */
      fout<<l<<" "<<mu<<"\n";
      fout.close();
   }

   fin.close();
   getch();
   return 0;
}