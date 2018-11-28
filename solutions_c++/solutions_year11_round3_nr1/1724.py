#include<iostream.h>
#include<fstream.h>
#include<conio.h>
#include<stdio.h>
#include<math.h>
#include<iomanip.h>


#define rep(i,n) for(i=0;i<n;i++)
#define rep1(i,n) for(i=1;i<=n;i++)
#define res(i,a,b) for(i=a;i<b;i++)
#define rev(i,k) for(i=k;i>=0;i--)


typedef long long ll;
typedef long double ld;

ll tn,tr;
int r,c;
char bs[100][100];
int i,j;




void main(void)
{


	ifstream in("i.txt");
	freopen("o.txt", "w", stdout);
	clrscr();
	cout.setf(ios::fixed);
	cout.unsetf(ios::showpoint);

	int flag;
	in>>tr;
	rep(tn,tr)
	{
		in>>r>>c;
		flag=0;
		rep(i,r)
		{
			in>>bs[i];
		}
		rep(i,r-1)
		{
			rep(j,c-1)
			{
				if(bs[i][j]=='#'&&bs[i][j+1]=='#'&&bs[i+1][j]=='#'&&bs[i+1][j+1]=='#')
				{
				      bs[i][j]='/';
				      bs[i][j+1]='\\';
				      bs[i+1][j]='\\' ;
				      bs[i+1][j+1]='/';
				}
			}
		}

		rep(i,r)
		{
			rep(j,c)
			{	if(bs[i][j]=='#')
				{flag=1;}
			}
		}
		if(flag==1)
		{       cout<<"Case #"<<tn+1<<":"<<endl<<"Impossible"<<endl; continue; }

		cout<<"Case #"<<tn+1<<":"<<endl;
		rep(i,r)
		{	rep(j,c)
			{
				cout<<bs[i][j];
			}
			cout<<endl;
		}


	 }
	// getch();



}







