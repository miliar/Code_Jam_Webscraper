#include<fstream.h>
#include<process.h>
#include<conio.h>
char temp[100];
char s[]="welcome to code jam";
int n,ctr=0;
void search(int t, int pos)
	{
	for(int i=pos;temp[i]!='\0';i++)
		{
		if(temp[i]==s[t])
			{
			if(t==18)
				{
				ctr++;
				}
			else
				{
				search(t+1,i+1);
				//search(t,pos+1);
				}
				
			}
		
		}
	}

			
void main()

{
clrscr();
ifstream file("C-small.in");
ofstream filo("output.out");
if(!file)
	{
	cout<<" NO FILE FOUND";
	getch();
	exit(0);
	}
file>>n;
file.getline(temp,2);
for(int i=0;i<n;i++)
	{

	ctr=0;
	file.getline(temp,100);
	search(0,0);
	cout<<temp<<" "<<ctr<<"\n";
	int a=ctr%10;
	ctr=ctr/10;
	int b=ctr%10;
	ctr=ctr/10;
	int c=ctr%10;
	ctr=ctr/10;
	int d=ctr%10;
	filo<<"Case #"<<i+1<<": "<<d<<c<<b<<a<<"\n";
	}
filo.close();
file.close();

cout<<"\ndone";
getch();
}
