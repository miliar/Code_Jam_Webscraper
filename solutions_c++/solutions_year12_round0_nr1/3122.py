#include<iostream>
#include<stdio.h>
#include<string.h>
#include<stdlib.h>
using namespace std;

int main()
{
    freopen("example1.txt","r",(stdin));
    freopen("output.txt","w",(stdout));
	int t,no=0;
	scanf("%d ",&t);
	
	while(t--)
	{
		no++;
		char A[100000];
		
		gets(A);
		int l=strlen(A);
		
		for(int i=0;i<l;++i)
		{
			     if(A[i]=='y')A[i]='a';
			else if(A[i]=='n')A[i]='b';
			else if(A[i]=='f')A[i]='c';
			else if(A[i]=='i')A[i]='d';
			else if(A[i]=='c')A[i]='e';
			else if(A[i]=='w')A[i]='f';
			else if(A[i]=='l')A[i]='g';
			else if(A[i]=='b')A[i]='h';
			else if(A[i]=='k')A[i]='i';
			else if(A[i]=='u')A[i]='j';
			else if(A[i]=='o')A[i]='k';
			else if(A[i]=='m')A[i]='l';
			else if(A[i]=='x')A[i]='m';
			else if(A[i]=='s')A[i]='n';
			else if(A[i]=='e')A[i]='o';
			else if(A[i]=='v')A[i]='p';
			else if(A[i]=='z')A[i]='q';
			else if(A[i]=='p')A[i]='r';
			else if(A[i]=='d')A[i]='s';
			else if(A[i]=='r')A[i]='t';
			else if(A[i]=='j')A[i]='u';
			else if(A[i]=='g')A[i]='v';
			else if(A[i]=='t')A[i]='w';
			else if(A[i]=='h')A[i]='x';
			else if(A[i]=='a')A[i]='y';
			else if(A[i]=='q')A[i]='z';
			
		}
		printf("Case #%d: ",no);
		puts(A);
	
	}
return 0;
}
