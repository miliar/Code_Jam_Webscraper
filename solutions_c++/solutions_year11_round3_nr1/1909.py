#include<iostream.h>
#include<fstream.h>
#include<conio.h>


int main()

{

fstream in, ou;
int s,t,r,c,i,j;
char rc[50][50];
clrscr();

in.open("large.in",ios::in);

if(!in)
{
cout<<"input error";
}
ou.open("A-large.out",ios::out);
if(!ou)
{
cout<<"ouput error";
}
in>>t;
for(s=0;s<t;s++)
{

int m=0;
in>>r;
in>>c;

	for(i=0;i<r;i++)
	for(j=0;j<c;j++)
	in>>rc[i][j];

	for(i=0;i<r;i++)
	{
	for(j=0;j<c;j++)
	{

	if(rc[i][j]=='#'&&m==0)
	{

	if(rc[i][j+1]=='#'&&(j+1)<c)
	rc[i][j+1]='\\';
	else m=1;

	if(rc[i+1][j]=='#'&&(i+1)<r)
	rc[i+1][j]='\\';
	else m=1;

	if(rc[i+1][j+1]=='#'&&(j+1)<c&&(i+1)<r)
	rc[i+1][j+1]='/';
	else m=1;
	rc[i][j]='/';
	}           }
	cout<<endl;
	}

	ou<<"Case #"<<s+1<<":"<<endl;
	if(m==1)
	ou<<"Impossible"<<endl;
	else
	for(i=0;i<r;i++)
	{
	for(j=0;j<c;j++)
	ou<<rc[i][j];
	ou<<endl;
	}


}

ou.close();
in.close();
return 0;




}