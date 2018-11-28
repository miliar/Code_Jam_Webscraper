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
//A == 1
//B == 2
//road == 0
class Train
{
public:
  int station;
  Train(int station){this->station=station;}
  map<int,int> trips;
  int whereat(int mtime){
    if(trips.size()==0){return station;}
    for(map<int,int>::iterator it=trips.begin();it!=trips.end();it++){
      if((mtime<(it->second)) && (mtime>=(it->first))){ return 0;}
    }
    return station;
  }
};
 
int main(int argc, char *argv[]) {
    if(argc<2){fprintf(stderr,"usage: %s infile\n",
            argv[0]);exit(1);}
//init...
    char infile[200];
    char outfile[30]="./jamout1.2.txt";
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
    int casenum=0;
    while(casenum!=cases){
      casenum++;
      fgets(line,150,fin);
      pch=strstr(line,"\n");
      (*pch)='\0';
      int ta=atoi(line);
      fgets(line,150,fin);
      pch=strstr(line,"\n");
      (*pch)='\0';
      char *pch2=strstr(line," ");
      (*pch2)='\0';
      pch2+=1;
      int na=atoi(line);
      int nb=atoi(pch2);
      map<int,deque<int> > amap;
      map<int,deque<int> > bmap;
      map<int,deque<int> > daymap;
      int ca=0;
      while(ca!=na){
	ca++;
	fgets(line,150,fin);
	pch=strstr(line,"\n");
	if(pch!=NULL){(*pch)='\0';}
	pch2=strstr(line," ");
	(*pch2)='\0'; pch2+=1;
	char *pchh=strstr(line,":");
	(*pchh)='\0'; pchh+=1;
	char *pchh2=strstr(pch2,":");
	(*pchh2)='\0'; pchh2+=1;
	int beg=(atoi(line)*60)+atoi(pchh);
	int end=(atoi(pch2)*60)+atoi(pchh2);
	if(amap.find(beg)!=amap.end()){
	    amap[beg].push_back(end);
	  }
	else{
	deque<int> tl;
	tl.push_back(end);
	amap[beg]=tl;
	}
	if(daymap.find(beg)!=daymap.end()){
	    daymap[beg].front()=((daymap[beg].front())+1);
	  }
	else{
          deque<int> tv;
	  tv.push_back(1);
	  tv.push_back(0);
	  daymap[beg]=tv;
	}
      }
      int cb=0;
      while(cb!=nb){
	cb++;
	fgets(line,150,fin);
	pch=strstr(line,"\n");
	if(pch!=NULL){(*pch)='\0';}
	pch2=strstr(line," ");
	(*pch2)='\0'; pch2+=1;
	char *pchh=strstr(line,":");
	(*pchh)='\0'; pchh+=1;
	char *pchh2=strstr(pch2,":");
	(*pchh2)='\0'; pchh2+=1;
	int beg=(atoi(line)*60)+atoi(pchh);
	int end=(atoi(pch2)*60)+atoi(pchh2);
	if(bmap.find(beg)!=bmap.end()){
	    bmap[beg].push_back(end);
	  }
	else{
	deque<int> tl;
	tl.push_back(end);
	bmap[beg]=tl;
	}
	if(daymap.find(beg)!=daymap.end()){
	    daymap[beg].back()=((daymap[beg].back())+1);
    	  }
	else{
          deque<int> tv;
	  tv.push_back(0);
	  tv.push_back(1);
	  daymap[beg]=tv;
	}
      }
      vector<Train> trains;
      int atrains=0;
      int btrains=0;

      for(map<int,deque<int> >::iterator it=daymap.begin();it!=daymap.end();it++){
        int aloop=0;
	while(aloop!=((it->second).front())){
	  aloop+=1;
	  bool solved1=false;
	  for(vector<Train>::iterator tit=trains.begin();tit!=trains.end();tit++){
	    if(((*tit).whereat((it->first)))==1){
	      (*tit).trips[it->first]=((amap[it->first].front())+ta);
	      amap[it->first].pop_front();
	      (*tit).station=2;
	      solved1=true;
	      break;
	    }
	  }
	  if(solved1==false){
	    Train temptr(1);
	    temptr.trips[it->first]=((amap[it->first].front())+ta);
	    amap[it->first].pop_front();
	    temptr.station=2;
	    trains.push_back(temptr);
	    atrains+=1;
	  }
	}
	int bloop=0;
	while(bloop!=((it->second).back())){
	  bloop+=1;
	  bool solved1=false;
	  for(vector<Train>::iterator tit=trains.begin();tit!=trains.end();tit++){
	    if(((*tit).whereat((it->first)))==2){
	      (*tit).trips[it->first]=((bmap[it->first].front())+ta);
	      bmap[it->first].pop_front();
	      (*tit).station=1;
	      solved1=true;
	      break;
	    }
	  }
	  if(solved1==false){
	    Train temptr(2);
	    temptr.trips[it->first]=((bmap[it->first].front())+ta);
	    bmap[it->first].pop_front();
	    temptr.station=1;
	    trains.push_back(temptr);
	    btrains+=1;
	  }
	}
       	
	
      }

      char outline[150];
      sprintf(outline,"Case #%i: %i %i\n",casenum,atrains,btrains);
      fprintf(fout,outline);
      trains.clear();
    }
    fclose(fin);
    fclose(fout);
}
      






