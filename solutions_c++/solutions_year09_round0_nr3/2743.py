#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<stdio.h>
#include<fstream.h>

char a[]="welcome to code jam";
int len=strlen(a);
char input[30000];
long count=0;
void get_count(int x,int pos,int l)
{
	if(x==len)
	{
	 count++;
	}
	else
	{
	  for(int i=pos;i<l;i++)
	  {
		if(input[i]==a[x])
		{
		      //	cout<<"."<<count<<"\n";
			get_count(x+1,i,l);

		}
	  }
	}
}
void main()
{
 clrscr();
// gets(input);
ifstream fin;
int t;
/*
fin.open("pr.txt");
fin>>t;
fin.getline(input,10000);
for(int j=0;j<t;j++)
{
fin.getline(input,10000);

int l=strlen(input);
//int length=strlen("welcome to code jam");

 get_count(0,0,l);


 cout<<"Case #"<<j+1<<": ";

 cout.fill('0');
 cout.width(4);
 cout<<count%10000;
 cout<<'\n';
 count=0;
}
*/
 getch();
}

