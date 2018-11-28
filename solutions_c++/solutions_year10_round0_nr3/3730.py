#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<iomanip.h>
#include<stdio.h>
#include<stdlib.h>
int a[1000];
//int cs=0;
void cal(int R, int K, int N)
{
	static int cs;
	long int amt=0;
	int max=N,j=0,flag;
	for(int i=1;i<=R; i++)
	{
		flag=1;
		long int t=a[j];
		j=(j+1)%max;
		flag++;
		while(1)
		{
			if(flag>max)
				break;
			if(t+a[j]>K)
				break;
			else
			{
				t+=a[j];
				j=(j+1)%max;
				flag++;
			}
		}
		amt+=t;
	}
	cs++;
	fstream f;
	f.open("out.txt",ios::app);
	f.put('C');
	f.put('a');
	f.put('s');
	f.put('e');
	f.put(' ');
	f.put('#');
	f<<cs;
	f.put(':');
	f.put(' ');
	f<<amt;
	f.put('\n');

}
void main()
{
	clrscr();
	int N=0,R,c,i,K;
	fstream f;
	f.open("C-small-attempt0",ios::in);
	f>>i;
	c=i;
	for(int x=1;x<=c;x++)
	{
		f>>i;
		R=i;
		f>>i;
		K=i;
		f>>i;
		N=i;
		for(int y=0;y<N; y++)
		{
			f>>i;
			a[y]=i;
		}
		cal(R,K,N);
	}
	f.close();
	getch();
}