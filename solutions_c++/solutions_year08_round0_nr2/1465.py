/*
/* Author: Giacomo Spigler
/* Contest: Google CODEJam 2008, Qualification Round
/* Date: 27/07/2008
*/

#include <iostream>
#include <math.h>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;


typedef struct train_ {
  int sh, sm; //departure
  int eh, em; //arrival
  int st, et;
  int station;
};


typedef struct train {
  int station; //0 A   1 B
  int time; //(from which time it will be free)
};


int main() {
  int n;

  vector<train_> t;

  scanf("%d", &n);

  for(int ccc=0; ccc<n; ccc++) {
    int T, na, nb;

    t.clear();

    scanf("%d", &T);
    scanf("%d %d", &na, &nb);


    for(int i=0; i<na; i++) {
      train_ tmp;
      scanf("%d:%d %d:%d", &tmp.sh, &tmp.sm, &tmp.eh, &tmp.em);
      tmp.em+=T;
      tmp.st=tmp.sh*60+tmp.sm;
      tmp.et=tmp.eh*60+tmp.em;
      tmp.station=0;
      t.push_back(tmp);
    }

    for(int i=0; i<nb; i++) {
      train_ tmp;
      scanf("%d:%d %d:%d", &tmp.sh, &tmp.sm, &tmp.eh, &tmp.em);
      tmp.em+=T;
      tmp.st=tmp.sh*60+tmp.sm;
      tmp.et=tmp.eh*60+tmp.em;
      tmp.station=1;
      t.push_back(tmp);
    }


    if(na==0 || nb==0) {
      printf("Case #%d: %d %d\n", ccc+1, na, nb);
      continue;
    }


    //test every number of trains
    for(int i=0; i<100; i++) {
      vector<train> trains(201);

      for(int k=0; k<i; k++) {
        trains[k].station=0;
        trains[k].time=0;
/*
        train tmp;
        tmp.station=0;
        tmp.time=0;
        trains.push_back(tmp);*/
      }


     for(int j=0; j<100; j++) {
       for(int k=0; k<i; k++) {
         trains[k].station=0;
         trains[k].time=0;
       }

       for(int k=0; k<j; k++) {
         trains[k+i].station=1;
         trains[k+i].time=0;
/*
         train tmp;
         tmp.station=1;
         tmp.time=0;
         trains.push_back(tmp);*/
       }


       vector<train_> t2(t.size());
       for(int p=0; p<t.size(); p++) {
         t2[p].station=t[p].station;
         t2[p].st=t[p].st;
         t2[p].et=t[p].et;
       }



       //now we have trains.. loop until we cannot satisfy a request (search for first free train in a given station to match the first travel to accomodate)

       //I, J : number of trains in A, B

       int ok=1;
       while(ok==1) {
         //find first train (if station==-1, it's yet done)
         train_ best;
         int minindext=0;
         int mintime=2000;
         for(int k=0; k<t2.size(); k++) {
           if(t2[k].station!=-1) {
             if(t2[k].st < mintime) {
               mintime=t2[k].st;
               best=t2[k];
               minindext=k;
             }

           }
         }

         if(mintime==2000) {
           ok=2;
         }

         if(ok!=2) {
           //find first train available at that location
           train bestT;
           int minindextrain=0;
           mintime=2000;
           for(int k=0; k<i+j; k++) {
             if(trains[k].station==best.station) {
               if(trains[k].time<mintime) {
                 mintime=trains[k].time;
                 bestT=trains[k];
                 minindextrain=k;
               }

             }
           }

//printf("%d %d %d\n", i, j, mintime);
           if(mintime==2000 || bestT.time>best.st) {
             ok=0;
           } else {
//printf("%d %d     %d:%d   %d %d:%d\n", i, j,  bestT.time/60, bestT.time%60, best.station, best.st/60, best.st % 60);
//printf("\n\n");

             //do the travel
             //t[minindext]  trains[minindextrain]
             t2[minindext].station=-1;
             trains[minindextrain].station=1-trains[minindextrain].station;
             trains[minindextrain].time = t2[minindext].et;
           }

         }

       }


       if(ok==2) {
         printf("Case #%d: %d %d\n", ccc+1, i, j);
         i=1000;
         j=1000;
       }




      }

    }






  }


  return 0;
}

