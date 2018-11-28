#include<iostream>
#include<fstream>
#include<conio>
#include<string>
#include<stdio>
#include<stdlib>
#include<ctype>
using namespace std;
int GetIntVal(string strConvert)
{
	int intReturn;
   intReturn = atoi(strConvert.c_str());
   return(intReturn);
}



void main()
{
	ifstream myfile("gcj1.txt");
   ofstream outputfile("gcj2.txt");
	string line;
   char words[500][500],tests[500][500],letters[500][500];
   int L,D,N,len,j,c1=0,count=0,c2=0,c=0,mul=1,flag,factor,m,co=0;
   getline(myfile,line,' ');
   L=GetIntVal(line);
   getline(myfile,line,' ');
   D=GetIntVal(line);
   getline(myfile,line,'\n');
   N=GetIntVal(line);
   for(int i=0;i<D;i++)
   {
   	getline(myfile,line,'\n');
      for(j=0;j<L;j++)
      {
      	words[i][j]=line[j];
      }
      words[i][j]='\0';
   }
   for(int r=0;r<N;r++)
   {
   	getline(myfile,line,'\n');
      len=line.size();
      for(j=0;j<len;j++)
      {
      	tests[r][j]=line[j];
      }
      tests[r][j]='\0';
   }
   for(int r=0;r<N;r++)
   {
   	len=strlen(tests[r]);

      count=0;
      while(count<len)
      {
         if(tests[r][count]=='(')
         {
         	while(tests[r][count]!=')')
            {

         	count++;
         	if(tests[r][count]!=')')
            {

         		letters[c1][c2]=tests[r][count];
               c2++;
            }
			}
           letters[c1][c2]='\0';
           count++;
           c1++;
           c2=0;
         }
         else
         {
         	letters[c1][c2++]=tests[r][count];
            letters[c1][c2]='\0';
            c1++;
            c2=0;
            count++;
			}
   	}
      c1=0;

   for(int j=0;j<D;j++)
   {
   	flag=0;
		for(int i=0;i<L;i++)
	   {
      	//cout<<letters[i]<<"\n";
         for(int a=0;a<strlen(letters[i]);a++)
         {
   			if(words[j][i]==letters[i][a])
            {
            	flag++;
               break;
            }
         }
      }

      if(flag==L)
      {
   	  co++;
      }

   }
   outputfile<<"Case #"<<r+1<<": "<<co<<"\n";
   co=0;
}


   getch();


}
