#include<iostream.h>
#include<fstream.h>
#include<string.h>
#include<stdio.h>
#include<stdlib.h>
int compare(char n[], char m[])
{
	for(int index=0; index<strlen(n); index++)
	{       char temp=n[0];
		for(int i=0;i<strlen(n)-1;i++)
		{
			n[i]=n[i+1];
		}
		n[strlen(n)-1]=temp;
		if(strcmp(n,m)==0)
			return 1;
	}
	return 0;
}
int main()
{
	ifstream ifile("F-small.txt");
	ofstream ofile("fsout.txt");

	char a[5], b[5],m[5],n[5];
	int te,count,c;
	int i,j,size;
	ifile>>te;
	for(int p=0;p<te;p++)
	{       count=0;
		ifile>>a;
		ifile>>b;
		i=atoi(a);
		j=atoi(b);
		while(i<j)
		{
			int k=i+1;
			while(k<=j)
			{       itoa(i,n,10);
				itoa(k,m,10);

				c=compare(n,m);
				if(c!=0)
					count++;
				k++;
			}
			i++;
		}
		ofile<<"Case #"<<p+1<<": "<<count<<"\n";
	}
	return 0;
}
