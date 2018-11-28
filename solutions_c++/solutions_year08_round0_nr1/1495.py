#include "stdio.h"
#include "stdlib.h"
#include "unistd.h"
#include "math.h"
#include <string>
#include <sys/types.h>
#include <vector>
#include <map>
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
    char infile[200];
    char outfile[30]="./jamout1.1.txt";
    strcpy(infile,argv[1]);

    FILE *fin =  checked_fopen(infile , "r");
    FILE *fout = checked_fopen(outfile, "w");
//processing...
    char line[150];
    if (fgets(line,150,fin) == NULL ){
      fprintf(stderr,"Serious problem with input");
      exit(1);
    }
    char *pch=strstr(line,"\n");
    if (pch!=NULL){(*pch)='\0';}
    int cases=atoi(line);
    fprintf(stderr,"Number of cases:%i\n",cases);
    int casenum=0;
    while(casenum!=cases){
      casenum++;
      fprintf(stderr,"Case:%i\n",casenum);
      fgets(line,150,fin);
      pch=strstr(line,"\n");
      (*pch)='\0';
      int engines=atoi(line);
      fprintf(stderr,"Engines:%i\n",engines);
      int engine=0;
      map<string,int> simap;
      map<int,string> ismap;
      while(engine!=engines){
	engine++;
	fgets(line,150,fin);
	pch=strstr(line,"\n");
	(*pch)='\0';
	string temp=line;
	simap[temp]=engine;
	ismap[engine]=temp;
      }
      fgets(line,150,fin);
      pch=strstr(line,"\n");
      (*pch)='\0';
      int queries=atoi(line);
      fprintf(stderr,"Number of queries:%i\n",queries);
      int query=0;
      deque<int> raw;
      while(query!=queries){
	query++;
	fgets(line,150,fin);
	pch=strstr(line,"\n");
	if(pch!=NULL){	(*pch)='\0';}
	string temp=line;
	raw.push_back(simap[temp]);
      }
      //end of input
      int switches=0;
      while(raw.size()!=0){
	set<int> knot;
	while((knot.size()!=engines) && (raw.size()!=0)){
	  knot.insert(raw.front());
	  if(knot.size()!=engines){
	    raw.pop_front();
	  }
	}
	if(knot.size()==engines){
	  switches++;
	}
	knot.clear();
      }
      char outline[150];
      sprintf(outline,"Case #%i: %i\n",casenum,switches);
      fprintf(stderr,"%s",outline);
      fprintf(fout,outline);
      simap.clear();
      ismap.clear();      
    }
    fclose(fin);
    fclose(fout);
}
      






