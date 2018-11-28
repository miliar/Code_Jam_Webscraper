#include<stdio.h>

int sta[1440],stb[1440];

int min(int a, int b) {
  if (a<b) {
    return a;
  } else {
    return b;
  }
}


int main() {
  int i,j,k;
  int total,T,NA,NB;
  int dep,arr,reza,rezb;
  char a,b,c;
  
  FILE *f,*fo;
  f=fopen("input2.txt","r+");
  fo=fopen("output2.txt","w+");
  
  fscanf(f,"%d",&total);
  
  for (k=0;k<total;k++) {
      
    for (i=0;i<1440;i++) {
      sta[i]=0;
      stb[i]=0;
    }
      
    // 3 reading parts
    fscanf(f,"%d",&T);
    fscanf(f,"%d",&NA);
    fscanf(f,"%d",&NB);
    
    if (NA>0) {
    for (i=0;i<NA;i++) {
      // first the new row is read
      fscanf(f,"%c",&c);
      fscanf(f,"%c",&a);
      fscanf(f,"%c",&b);
      
      dep=((a-'0')*10+(b-'0'))*60;
      fscanf(f,"%c",&c);
      fscanf(f,"%c",&a);
      fscanf(f,"%c",&b);
      
      dep=dep+((a-'0')*10+(b-'0'));
    
      // first the new row is read
      fscanf(f,"%c",&c);
      fscanf(f,"%c",&a);
      fscanf(f,"%c",&b);
      arr=((a-'0')*10+(b-'0'))*60;
      
      fscanf(f,"%c",&c);
      fscanf(f,"%c",&a);
      fscanf(f,"%c",&b);
      
      arr=arr+((a-'0')*10+(b-'0'));
      
      for (j=dep;j<1440;j++) {
        sta[j]--;
      }
      
      if ((arr+T)<1440) {
        for (j=(arr+T);j<1440;j++) {
          stb[j]++;
        }
      }
      
    }
    }
    
    if (NB>0) {
    for (i=0;i<NB;i++) {
      // first the new row is read
      fscanf(f,"%c",&c);
      fscanf(f,"%c",&a);
      fscanf(f,"%c",&b);
      
      dep=((a-'0')*10+(b-'0'))*60;
      fscanf(f,"%c",&c);
      fscanf(f,"%c",&a);
      fscanf(f,"%c",&b);
      
      dep=dep+((a-'0')*10+(b-'0'));
    
      // first the new row is read
      fscanf(f,"%c",&c);
      fscanf(f,"%c",&a);
      fscanf(f,"%c",&b);
      
      arr=((a-'0')*10+(b-'0'))*60;
      fscanf(f,"%c",&c);
      fscanf(f,"%c",&a);
      fscanf(f,"%c",&b);
      
      arr=arr+((a-'0')*10+(b-'0'));
      
      for (j=dep;j<1440;j++) {
        stb[j]--;
      }
      
      if ((arr+T)<1440) {
        for (j=(arr+T);j<1440;j++) {
          sta[j]++;
        }
      }
      
    }
    }
    
    // the result part
    reza=0;
    for (i=0;i<1440;i++) {
      reza=min(reza,sta[i]);
    }
    reza=0-reza;
    
    rezb=0;
    for (i=0;i<1440;i++) {
      rezb=min(rezb,stb[i]);
    }
    rezb=0-rezb;
    
    fprintf(fo,"Case #%d: %d %d\n",k+1,reza,rezb);
    
  }
  
  
  
  fclose(f);
  fclose(fo);
  
  return 0;
}
