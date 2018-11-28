#include <iostream.h>
#include <fstream.h>
#include <conio.h>
#include <string.h>
#include <stdio.h>
#include<stdio.h>
#include<iostream.h>
#include<conio.h>
#include<string.h>
#include<memory.h>
char s[500][500];
int main()
{
		
         FILE *fp=fopen("F:/TCWIN45/BIN/A-small-attempt1.in", "r"); 
         FILE *ofp=fopen("F:/TCWIN45/BIN/out.out", "w");
		 int T=30,i=0,j=0,k=0,l=0,n=100,count[100],words[100],temp=0;
		
		fscanf(fp, "%d", &T);
                   
                   
                   
                   
                   for(k=0;k<=T+1;k++)
                     {
                                   fgets(s[k],500,fp);
                     }
                  		
for(j=0;j<=T+1;j++)
{
for(k=0;k<n;k++)
{
if(s[j][k]=='a')
s[j][k]='y';
else if(s[j][k]=='b')
s[j][k]='h';
else if(s[j][k]=='c')
s[j][k]='e';
else if(s[j][k]=='d')
s[j][k]='s';
else if(s[j][k]=='e')
s[j][k]='o';
else if(s[j][k]=='f')
s[j][k]='c';
else if(s[j][k]=='g')
s[j][k]='v';
else if(s[j][k]=='h')
s[j][k]='x';
else if(s[j][k]=='i')
s[j][k]='d';
else if(s[j][k]=='j')
s[j][k]='u';
else if(s[j][k]=='k')
s[j][k]='i';
else if(s[j][k]=='l')
s[j][k]='g';
else if(s[j][k]=='m')
s[j][k]='l';
else if(s[j][k]=='n')
s[j][k]='b';
else if(s[j][k]=='o')
s[j][k]='k';
else if(s[j][k]=='p')
s[j][k]='r';
else if(s[j][k]=='q')
s[j][k]='z';
else if(s[j][k]=='r')
s[j][k]='t';
else if(s[j][k]=='s')
s[j][k]='n';
else if(s[j][k]=='t')
s[j][k]='w';
else if(s[j][k]=='u')
s[j][k]='j';
else if(s[j][k]=='v')
s[j][k]='p';
else if(s[j][k]=='w')
s[j][k]='f';
else if(s[j][k]=='x')
s[j][k]='m';
else if(s[j][k]=='y')
s[j][k]='a';
else if(s[j][k]=='z')
s[j][k]='q';
}
}
			      
					for(i=0;i<=T+1;i++)
					{
                    cout<<"Case #"<<i+1<<": "<<s[i]<<endl;
                    fprintf(ofp, "Case #%d: %s\n", i+1, s[i]);
                    }
getch();
return 0;
}

