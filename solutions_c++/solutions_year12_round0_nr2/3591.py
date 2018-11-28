#include<iostream>
#include<fstream>


int main()
{
	using namespace std;
	ifstream fin;
	fin.open("data.in",ios::in);
	ofstream fout;
	fout.open("data.out",ios::out);

 int testcases;
 fin>>testcases;
 for(int i=0;i<testcases;i++)
 {
 	fout<<"Case #"<<(i+1)<<": ";
      int n,score,p,high=0;
      fin>>n>>score>>p;

      int googler[101];
      for(int j=0;j<n;j++)
      {
	      fin>>googler[j];
	      if(googler[j]/3 >=p)
	       {
		       	googler[j]=0;
       			high++;
       		}
       else if(googler[j]/3==p-1 && googler[j]%3>=1)
       {
	       googler[j]=0;
	       high++;
       }
     }
      while(!fin.eof() && score!=0)
      {
        for(int k=0;k<n;k++)
        {
         if(googler[k]!=0)
         {
           if ( ( (googler[k]/3)==p-2) && ((googler[k]%3) ==2) || (googler[k]/3)==p-1)
           {
            googler[k]=0;
            score--;
            high++;
           }
         }
        }

      }

     fout<<high;
     fout<<endl;
 }

}

