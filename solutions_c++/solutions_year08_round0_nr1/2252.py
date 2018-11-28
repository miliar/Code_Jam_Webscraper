#include<conio.h>
#include<iostream.h>
#include<string.h>
#include<fstream.h>
#include<vector>
using namespace std;

int Converter (vector<string> Sequence,vector<string> SearchEng,int seqlen,int slen)
	{
   long int count=1,Maincount=0,i,k,j,z;
   vector<string> temp1;
   for(i=0,j=1;j<seqlen;i++,j++)
      {
      strcpy(temp1[i],Sequence[i]);
      if(Sequence[i]!=Sequence[j])
			{
         for(k=0;k<=i;k++)
         	{
            if (strcmp(Sequence[j],temp1[k]))
               {
               if(k==i)
               	{
                  count=count+1;
                  }
               }
            else
            	break;
            }
         }
      if (count==slen)
      	{
         Maincount=Maincount+1;
         strcpy(temp1[0],Sequence[j]);
         for(z=1;z<1001;z++)
      		strcpy(temp1[z],"");
         count=1;
         }
      }
   return Maincount;
	}

int main()
     {
     clrscr();
   long int totalCases=0,SearchNo=0,IterationNo=0;
   vector<string> Iteration,Search;
   long int Maincount=0,i,j,k;
   ifstream fin;
   ofstream fout;
   fin.open("C:\\temp\\data.in",ios::in);
   fout.open("C:\\temp\\output.txt",ios::out);
   fin>>totalCases;
   for(i=1;i<=totalCases;i++)
   	{
      fin>>SearchNo;
      for(j=-1;j<SearchNo;j++)
         	{
            fin.getline(search[j],100);
            }
      fin>>IterationNo;
      for(k=-1;k<IterationNo;k++)
      		{
      	   fin.getline(Iteration[k],100);
            }
   	Maincount=Converter(Iteration,search,IterationNo,SearchNo);
      fout<<"Case #"<<i<<": "<<Maincount<<"\n";
      }
   fin.close();
   fout.close();
   getch();
   return 0;
   }