#include<iostream.h>
#include<fstream.h>
#include<stdio.h>
#include<conio.h>
#include<string.h>

void sort( int *a,int n)
{
	for(int i=0;i<n-1;i++)
       {
		int p=i,t=a[i];
		for( int j=i+1;j<n;j++)
		{
			if(t<a[j])
			{
				t=a[j];
				p=j;
			}

		}

		int z=a[p];
			a[p]=a[i];
			a[i]=z;
       }


}

void clas(int *f,int *a,int n)
{
	for(int i=0;i<n;i++)
	{
		f[i]=a[i]%3;
	}
}
void tgen(int t[][3],int *f,int* a,int n)
{       int x,fl;
	for(int i=0;i<n;i++)
	{
	      x=a[i]/3;
	      fl=f[i];
	      switch(fl)
	      {
		case 0: t[i][0]=x;
			t[i][1]=x;
			t[i][2]=x;
			break;
		case 1: t[i][0]=x;
			t[i][1]=x;
			t[i][2]=x+1;
			break;
		case 2: t[i][0]=x+1;
			t[i][1]=x+1;
			t[i][2]=x;
			break;

	      }
	}
}

int high(int *b)
{
	if(b[0]>b[1])
	{
		if(b[0]>b[2])
			return 0;
		else
			return 2;
	}
	else
	{
		if(b[1]>b[2])
			return 1;
		else
			return 2;
	}
}
int cmp(int t[][3],int p,int n,int *loc)
{
	int c=0,flg=1,pl,i=0;
	do
	{
	      pl=high(t[i]);
	      if(t[i][pl]>=p)
		c++;
	      else
		flg=0;
	      i++;
	}while(flg && c<n);
	*loc=i-1;
	return c;
}

void surp(int t[][3],int s,int loc,int n,int *f)
{
	int left=n-loc;
       //	int fl=1;
	if(s>left)
	{
		int tmp=s-left;
		loc=loc-tmp;
	}
      //	int d=0,i=0;
	while(s>0 && loc<n)
	{
	      switch(f[loc])
	      {
		case 0: if((t[loc][0]-1)<0)
			{	s++;
				break;
			}
			t[loc][0]--;
			if((t[loc][2]+1)>10)
			{	s++;
				break;
			}
			t[loc][2]++;
			break;
		case 1: if((t[loc][0]-1)<0)
			{	s++;
				break;
			}
			t[loc][0]--;
			if((t[loc][1]+1)>10)
			{	s++;
				break;
			}
			t[loc][1]++;

			break;
		case 2: if((t[loc][0]-1)<0)
			{	s++;
				break;
			}
			t[loc][0]--;
			if((t[loc][1]+1)>10)
			{	s++;
				break;
			}
			t[loc][1]++;

			break;

	      }

	      s--;
	      loc++;
	}
	if(s>0)
	{   loc=0;
	     while(s>0 && loc<n)
	{
	      switch(f[loc])
	      {
		case 0: if((t[loc][0]-1)<0)
			{	s++;
				break;
			}
			t[loc][0]--;
			if((t[loc][2]+1)>10)
			{	s++;
				break;
			}
			t[loc][2]++;
			break;
		case 1: if((t[loc][0]-1)<0)
			{	s++;
				break;
			}
			t[loc][0]--;
			if((t[loc][1]+1)>10)
			{	s++;
				break;
			}
			t[loc][1]++;

			break;
		case 2: if((t[loc][0]-1)<0)
			{	s++;
				break;
			}
			t[loc][0]--;
			if((t[loc][1]+1)>10)
			{	s++;
				break;
			}
			t[loc][1]++;

			break;

	      }

	      s--;
	      loc++;
	}
	}
}

int solve(int *a,int n,int s,int p)
{

	int flag[100],trip[100][3],ct=0,loc=0;
	clas(flag,a,n);
	tgen(trip,flag,a,n);
	ct=cmp(trip,p,n,&loc);
	surp(trip,s,loc,n,flag);
	ct=0;
	loc=0;
	ct=cmp(trip,p,n,&loc);
	return ct;


     // getch();

      /*	for(int i=0;i<n;i++)
	{
		for(int j=0;j<3;j++)
		{

			cout<<trip[i][j]<<" ";
		}
		cout<<endl;
	}
	getch();
	cout<<endl; */
     //  fout.close();
}
void main()
{
	clrscr();
	int n,t,s,p,sum[105],ct;

       ifstream fin;
       ofstream fout;
	fout.open("out.txt");
       fin.open("input.txt");

       fin>>t;
       for(int i=0;i<t;i++)
       {
	    fin>>n>>s>>p;
	    for(int j=0;j<n;j++)
	    {
		fin>>sum[j];

	    }
	    sort(sum,n);
	   ct=solve(sum,n,s,p);
	   fout<<"Case #"<<i+1<<": "<<ct<<endl;
       }

}

