#include<iostream.h>
#include<conio.h>
#include<fstream.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
void main()
{
clrscr();
int a,i,j,T,flag;
char translate[]={'y','n','f','i','c','w','l','b','k','u','o','m','x','s','e','v','z','p','d','r','j','g','t','h','a','q'};

char t[10];
char buffer[200];
ifstream ifile("input.txt");
ofstream ofile("output.txt",ios::out);
ifile.getline(t,'\n');
T=atoi(t);
cout<<"\nt:";
cout<<T;
a=0;
if(T<=30)
{
	while(!ifile.eof()&&a<T)
	{

		ifile.getline(buffer,101,'\n');
		cout<<"Buffer:";
		puts(buffer);
		cout<<"\n";
		for(int i=0;i<strlen(buffer);i++)
		{
			flag=0;
			for(int j=0;j<26;j++)
			{
				if(buffer[i]==translate[j])
				{
					flag=1;
					break;
				}
			}
			if(flag==1)
			{
				buffer[i]=96+j+1;
			}
		}
		ofile<<"Case #"<<++a;
		ofile<<": "<<buffer<<"\n";
		cout<<"buffer:"<<buffer<<"\n";
		buffer[0]='\0';
	}
}
ofile.close();
ifile.close();


}