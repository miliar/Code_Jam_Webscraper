#include <stdio.h>
#include <vector>
#include <iostream>
 
using namespace std;

struct transit {
  int source;
  int start;
  int end;
};

int main() {
  int i,j,k;
  vector< vector<int> > gotime;
  vector<transit> info;
  int n;
  FILE *fp;
  FILE *fp2;

  fp = fopen("b.in","r");
  fp2 = fopen("b.out","w");
  fscanf(fp,"%d",&n);
  
  for(int cases = 1;cases <= n;cases++) {
    gotime.resize(2);
    gotime[0].resize(0);
    gotime[1].resize(0);
    
    info.resize(0);
    
    int na,nb,t;
    int treqd[2] = {0,0};
    fscanf(fp,"%d",&t);
    fscanf(fp,"%d %d",&na,&nb);
    
    for(i = 0;i < na;i++) {
      int h1,m1,h2,m2;
      fscanf(fp,"%d:%d %d:%d",&h1,&m1,&h2,&m2);
      j = h1*100+m1;
      k = h2*100+m2;
      
      transit temp;
      temp.source = 0;
      temp.start = j;
      temp.end = k;
      info.push_back(temp);
    }
    
    for(i = 0;i < nb;i++) {
      int h1,m1,h2,m2;
      fscanf(fp,"%d:%d %d:%d",&h1,&m1,&h2,&m2);
      j = h1*100+m1;
      k = h2*100+m2;

      transit temp;
      temp.source = 1;
      temp.start = j;
      temp.end = k;
      info.push_back(temp);
    }
    
    /*
    printf("For case %d\n",n);
    for(i = 0;i < info.size();i++)    
      printf("from %d leaves %d arrives %d\n",info[i].source,info[i].start,info[i].end);
    */

    for(i = 0;i < info.size();i++) {
      int sm = i;
      for(j = i+1;j < info.size();j++)
	if(info[j].start < info[sm].start)
	  sm = j;
      
      transit temp;
      temp.source = info[sm].source;
      temp.start = info[sm].start;
      temp.end = info[sm].end;
      info[sm].source = info[i].source;
      info[sm].start = info[i].start;
      info[sm].end = info[i].end;
      info[i].source = temp.source;
      info[i].start = temp.start;
      info[i].end = temp.end;
    }
    
    /*
    printf("Sorted list\n");
    for(i = 0;i < info.size();i++) 
      printf("from %d leaves %d arrives %d\n",info[i].source,info[i].start,info[i].end);
    */
    
   
    for(i = 0;i < info.size();i++) {
      int s = info[i].source,d = !info[i].source;
      
      if(gotime[s].size() == 0 || gotime[s][0] > info[i].start) 
	treqd[s]++;
      else {
	for(j = 0;j < gotime[s].size()-1;j++)
	  gotime[s][j] = gotime[s][j+1];
	gotime[s].resize(gotime[s].size()-1);
      }
      
      gotime[d].push_back(info[i].end+t);
      sort(gotime[d].begin(),gotime[d].end());
    }
    
    fprintf(fp2,"Case #%d: %d %d\n",cases,treqd[0],treqd[1]);
  }
  
  fclose(fp);
  fclose(fp2);
  
  return 0;
}
