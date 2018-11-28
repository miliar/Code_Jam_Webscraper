#include <conio.h>
#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <math.h>
#include <utility>
#include <sstream>
#include <fstream>
using namespace std;

FILE * fin,* fout;
int N,L,D;
int main()
{
 	fin=fopen("D:/Documents and Settings/Arun/Desktop/Anup/codejam/qual/A-small.in","r");
    fout=fopen("D:/Documents and Settings/Arun/Desktop/Anup/codejam/qual/A-small.out","w");
    
	 fscanf(fin,"%d %d %d\n",&L,&D,&N);
	 
	 char d[5000][15];
	 for(int i=0;i<D;i++)
	  {fscanf(fin,"%s\n",d[i]);d[i][L]='\0';}
	  

 for(int i=1;i<=N;i++)
 {fprintf(fout,"Case #%d: ",i);
  char msg[500],a[15][24];
  int pos1=0,pos2,x,cnt=0;
  string s;
  fscanf(fin,"%s\n",msg);
  s=msg;
  
	 for(int j=0;j<L;j++)
	  if(s.substr(pos1,1) =="(")
	    {pos2=(s.substr(pos1)).find(")");
	     x=s.copy(a[j],pos2-1,pos1+1);
	    a[j][x]='\0';
	    
	     pos1=pos1+pos2+1;
		 
		 }
      else
        {x=s.copy(a[j],1,pos1);a[j][x]='\0';pos1++;}
        
     for(int j=0;j<D;j++)
     {int found=0;
      for(int k=0;k<L;k++)
         {string s1;
          s1=a[k];
          if(s1.find(d[j][k]) != string::npos)
            {found=1;}
          else
            {found=0;break;}
         }
      if(found == 1)
        cnt++;
     }		  

  fprintf(fout,"%d\n",cnt);

 }
 getch();
fclose(fin);
    fclose(fout);
return 0;
}


