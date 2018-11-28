#include <stdio.h>
#include <stdlib.h>
//destination pointa 0 pointb1
int clock_int (int h, int m) {
    return h*60+m;
}

int main () {
    FILE* fin;
    FILE* fout;
    fin = fopen ("2.in","r");
    fout = fopen ("2.out","w");
    int location[101]; // location of the trains
    int timefree[101]; // by wat time avaiable
    int n,nc,temp_c,temp_min,i,c,t1,t2,t; //n number of cases, nc n counter, i c counters, t1t2t temps
    int rest; //resttime
    int astart[101],aend[101],bstart[101],bend[101],na,nb,total,min_start,min_loc,min_end,min_c,nbus,useused,bus0,bus1;
    
    fscanf (fin,"%d",&n);
    for (nc=0;nc<n;nc++) {
        //clean
        for (i=0,nbus=0,bus0=0,bus1=0;i<101;i++) {
            location[i]=-1;
            timefree[i]=-1;    
        }
        //end clean
        fscanf (fin,"%d %d %d",&rest,&na,&nb);
        for (i=0;i<na;i++) {
            fscanf (fin,"%d:%d",&t1,&t2);
            astart[i]=clock_int(t1,t2);
            fscanf (fin,"%d:%d",&t1,&t2);
            aend[i]=clock_int(t1,t2);
        }
        for (i=0;i<nb;i++) {
            fscanf (fin,"%d:%d",&t1,&t2);
            bstart[i]=clock_int(t1,t2);
            fscanf (fin,"%d:%d",&t1,&t2);
            bend[i]=clock_int(t1,t2);
        }
        for (total=na+nb,i=0;i<total;i++) {
            min_start=1500;
            //loc 0
            for (c=0;c<na;c++) {
                if (astart[c]!=-1) {
                   if (min_start>astart[c]) {
                      min_start=astart[c];
                      min_c=c;
                      min_loc=0;
                      min_end=aend[c];                   
                   }                   
                }    
            }
            //loc 1
            for (c=0;c<nb;c++) {
                if (bstart[c]!=-1) {
                   if (min_start>bstart[c]) {
                      min_start=bstart[c];
                      min_c=c;
                      min_loc=1;
                      min_end=bend[c];
                   }                   
                }    
            }
            // found earliest trip, check bus avaiable
            for (c=0,useused=0,temp_min=1500;c<nbus;c++) {
                if (timefree[c]!=-1 && location[c]!=-1) {
                     if (min_loc==location[c] && timefree[c]<=min_start) {
                        useused=1;
                        if (timefree[c]<temp_min) {
                           temp_min=timefree[c];
                           temp_c=c;
                        }
                     }
                }
            }
            if (useused==1) {
               timefree[temp_c]=min_end+rest;
               if (location[temp_c]==1) location[temp_c]=0;
               else if (location[temp_c]==0) location[temp_c]=1;               
            }
            // if cant use used bus, need new bus!
            else if (useused==0) {
               timefree[nbus]=min_end+rest;
               if (min_loc==1) {
                  location[nbus]=0;
                  bus1++;
                  nbus++;
               }
               else if (min_loc==0) {
                    location[nbus]=1;
                    bus0++;
                    nbus++;
               }
            }
            if (min_loc==0) astart[min_c]=-1;
            else if (min_loc==1) bstart[min_c]=-1;              
        }
        fprintf (fout,"Case #%d: %d %d\n",nc+1,bus0,bus1);      
    }
    system ("pause");
}
