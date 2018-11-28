#include<iostream>
#include<fstream>
#include<conio>
#include<string>
#include<stdio>
#include<stdlib>
using namespace std;
int change(string strConvert)
{
	int intReturn;
	intReturn = atoi(strConvert.c_str());
	return(intReturn);
}
void main()
{
	ifstream myfile("g1.txt");
   ofstream opens("g2.txt");
   string line;
   int cases=0;
   char words[500][500],letters[500][500],answers[500][500];
   int L,D,N,r=0,c=0,f=0,m;
   getline(myfile,line,' ');
   L=change(line);
   getline(myfile,line,' ');
   D=change(line);
   getline(myfile,line,'\n');
   N=change(line);
   for(int i=0;i<D;i++)
   {
   	getline(myfile,line,'\n');
 		for(int j=0;j<L;j++)
      {
   		words[i][j]=line[j];
      }
      words[i][L]='\0';
   }
   for(int q=0;q<N;q++)
   {
   	cases=0;
   	r=0;
   	getline(myfile,line,'\n');
      f=0;
      m=line.size();
      while(f!=m)
      {
	      if(line[f]=='(')
   	   {
      		while(line[f]!=')')
         	{
            	f++;
               if(line[f]!=')')
               {
         			letters[r][c]=line[f];
	           	   c++;

               }
   	      }
            letters[r][c]=NULL;
            f++;
      	   r++;
            c=0;
	      }
   	   else
      	{
      		letters[r][c++]=line[f];
            letters[r][c]=NULL;
            r++;
            c=0;
            f++;
	      }
	   }
      for(int s=0;s<D;s++)
      {
      	f=0;
         for(int k=0;k<L;k++)
         {
         	for(int a=0;a<strlen(letters[k]);a++)
            {
            	if(words[s][k]==letters[k][a])
               {
               	f++;
                  break;
               }
            }
         }
      if(f==L)
      	cases++;
      }
   opens<<"Case #"<<q+1<<": "<<cases<<"\n";
	}
   getch();
}
