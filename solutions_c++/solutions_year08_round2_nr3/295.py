#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
#include "math.h"
#include <string>
#include <sys/types.h>
#include <vector>
#include <map>
#include <list>
#include <deque>
#include <set>
using namespace std;

inline FILE *checked_fopen( const char *file_name,
                            const char *mode_str, int exit_code=1 )
{
   FILE *file;

   if( (file=fopen(file_name, mode_str))==NULL )
   {
      printf( "Can't open file %s in %s mode",
                          file_name, mode_str );
   }

   return file;
}
struct item
{
  int rp;
  int num;
};
 
int main(int argc, char *argv[]) {
    if(argc<2){fprintf(stderr,"usage: %s infile\n",
            argv[0]);exit(1);}
//init...
    char infile[200];
    char outfile[30]="./jamout2.3.txt";
    strcpy(infile,argv[1]);

    FILE *fin =  checked_fopen(infile , "r");
    FILE *fout = checked_fopen(outfile, "w");
//processing...
    char line[5000];
    if (fgets(line,5000,fin) == NULL ){
      fprintf(stderr,"Serious problem with input");
      exit(1);
    }
    char *pch=strstr(line,"\n");
    if (pch!=NULL){(*pch)='\0';}
    int cases=atoi(line);
    int casenum=0;
    while(casenum!=cases){
      casenum++;
      fgets(line,5000,fin);
      pch=strstr(line,"\n");
      (*pch)='\0';
      int K=atoi(line);
      fgets(line,5000,fin);
      pch=strstr(line," ");
      (*pch)='\0';
      pch+=1;
      int N=atoi(line);
      int n=0;
      map<int,int> nmap;
      vector<int> nset;
      while(n!=N-1){
	n++;
	nset.push_back(atoi(pch));
	if(n!=N-1){
	  pch=strstr(pch," ");
	  (*pch)='\0';
	  pch+=1;
	}else{
	  pch=strstr(pch," ");
	  (*pch)='\0';
	  pch+=1;
	  char *pch2=strstr(pch,"\n");
	  if (pch2!=NULL){(*pch2)='\0';}
	  nset.push_back(atoi(pch));
	}
      }
      deque<item> itd;
      int k=0;
      while(k!=K){
	k++;
	item tempit;
	tempit.rp=k;
	tempit.num=0;
	itd.push_back(tempit);
      }
      int counter=0;
      while(itd.size()!=0){
	counter++;
	if( counter==(K+1-itd.size()) ) {
	  nmap[itd.front().rp]=counter;
	  itd.pop_front();
	  counter=0;
	}else{
	  itd.push_back(itd.front());
	  itd.pop_front();
	}	
      }
      char outline[5000];
      sprintf(outline,"Case #%i:",casenum);
      for(vector<int>::iterator it=nset.begin();it!=nset.end();it++){
	char ctmp[50];
	sprintf(ctmp," %i",nmap[(*it)]);
	strcat(outline,ctmp);
      }
      char ctmp2[5]="\n";      
      strcat(outline,ctmp2);
      fprintf(fout,outline);
    }
    fclose(fin);
    fclose(fout);
}
      






