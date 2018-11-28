#include<cstdio>
#include<string>
#define A 0
#define B 1
#define MAXTRIPS 110
#define NOTRIP -1

FILE* fin;
int numCases=0,totalA,totalB,N[2],T;


class trip{
public:
  int start,end;
  bool used;
  int nextcolor;
  trip(int color, int T){
    
    nextcolor=color;
    used=false;
    int hour,min;
    fscanf(fin,"%d:%d ",&hour,&min);
    start=60*hour+min;
    fscanf(fin,"%d:%d ",&hour,&min); 
    end=60*hour+min+T;
  }
  trip(int color=-1){
    nextcolor=color;
    used=true;
    start=24*60+100;
    end=-1;

  }

  bool valid(){
    return nextcolor!=-1;
  }

  void print(){
    printf("trip: start %d end %d used %d nextcolor %d\n",start,end,used,nextcolor);
  }
};

trip NOTRIPTRIP=trip();

trip sched[2][MAXTRIPS];

trip* nextTrip(trip tr){
  int color=tr.nextcolor,end=tr.end;
  trip* best=&NOTRIPTRIP;
  for(int i=0;i<N[color];i++)
    if(!sched[color][i].used&&sched[color][i].start>=tr.end
       &&sched[color][i].start<best->start)
      best=&sched[color][i];
  return best;
}

int earlyTrip(int color){
  int earlyStart=24*60+100;
  int best=NOTRIP;
  for(int i=0;i<N[color];i++)
    if(!sched[color][i].used&&sched[color][i].start<earlyStart){
      best=i;
      earlyStart=sched[color][best].start;
    }
  return best;
}

int main(int argc, char* argv[]){
  fin=fopen(argv[1],"r");

  FILE* fout=fopen (argv[2],"w");
  fscanf(fin, "%d\n",&numCases);
  for(int thisCase=1;thisCase<=numCases;thisCase++){
    totalA=totalB=0;
    fscanf(fin,"%d\n%d %d\n",&T,&N[A],&N[B]);
    for(int i=0;i<N[A];i++)
      sched[A][i]=trip(B,T);
    for(int i=0;i<N[B];i++)
      sched[B][i]=trip(A,T);
    int minA, minB;
    trip* initialTrip;
    for(;;){
      minA=earlyTrip(A);
      minB=earlyTrip(B);
      if(minA==NOTRIP&&minB==NOTRIP)
	break;
      if(minB==NOTRIP||sched[A][minA].start<sched[B][minB].start){
	initialTrip=&sched[A][minA];
	totalA++;
      }
      else{
	initialTrip=&sched[B][minB];
	totalB++;
      }
      //printf("Started at:");
      //initialTrip->print();
      for(trip* tr=initialTrip;(*tr).valid();tr=nextTrip(*tr)){
	//printf("And passed by: "); tr->print();
	tr->used=true;
      }
    }

    fprintf(fout,"Case #%d: %d %d\n",thisCase,totalA,totalB);
  }
  return 0;
}
