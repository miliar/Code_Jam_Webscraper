#include <stdio.h>
#include <string.h>
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

int main(int argc, char *argv[]) {
    if(argc<2){fprintf(stderr,"usage: %s infile\n",
            argv[0]);exit(1);}
//init...
    char infile[100];
    char outfile[30]="./jamout1.1.txt";
    strcpy(infile,argv[1]);

    FILE *fin =  checked_fopen(infile , "r");
    FILE *fout = checked_fopen(outfile, "w");
//processing...
    char big[16*5000];
    char line[5000];
    if (fgets(line,5000,fin) == NULL ){
      fprintf(stderr,"Serious problem with input");
      exit(1);
    }
    fprintf(stderr,"S");
    char *pch=strstr(line,"\n");
    if (pch!=NULL){(*pch)='\0';}
    pch=strstr(line," ");
    if (pch!=NULL){(*pch)='\0';}
    int L=atoi(line);
    char *pch2=strstr(pch+1," ");
    if (pch2!=NULL){(*pch2)='\0';}
    int D=atoi(pch+1);
    int N=atoi(pch2+1);
    fprintf(stderr,"L: %i D:%i N:%i", L, D, N);

    char line2[20];
    char* cursor=&big[0];
    fprintf(stderr,"S");
    int dlinenum=0;
    while(dlinenum!=D){
    	++dlinenum;
    	fgets(line2,L+2,fin);
    	strcpy(cursor, line2);
    	cursor+=16;
    }

    fprintf(stderr,"S");

    int casenum=0;
    while(casenum!=N){
      ++casenum;
      fgets(line,5000,fin);
      pch=strstr(line,"\n");
      (*pch)='\0';
      char* p=line;
      vector<set<char> > word;
      int l=1;
      bool block=false;
      while(l!=L+1){
    	  if(!block){
    		  if(*p=='('){
    			  block=true;
    			  set<char> temp;
    			  word.push_back(temp);
    		  } else {
    			  set<char> temp;
    			  temp.insert(*p);
    			  word.push_back(temp);
    			  ++l;
    		  }
    	  } else{
    		  if(*p==')'){
    			  block=false;
    			  ++l;
    		  } else{
    			  word[l-1].insert(*p);
    		  }
    	  }
    	  ++p;
      }

      int jee=0;
      dlinenum=0;

      while(dlinenum!=D){
    	  cursor=&big[dlinenum*16];
    	  ++dlinenum;
    	  bool good=true;
    	  l=0;
    	  while(l!=L){
    		  if(word[l].count(*cursor)==1){
    			 ++l;
    			 ++cursor;
    		  } else{
    			  good=false;
    			  break;
    		  }
    	  }
    	  if(good){
    		  ++jee;
    	  }
      }

      char outline[5000];
      sprintf(outline,"Case #%i: %i\n",casenum, jee);
      fprintf(fout,outline);
      fflush(fout);
    }
    fprintf(stderr,"S");
    fclose(fin);
    fclose(fout);
}







