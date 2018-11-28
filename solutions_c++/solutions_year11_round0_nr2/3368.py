#include <iomanip>
#include <stdio.h>
#include <map>
#include <set>
using namespace std;
int main(){
  FILE *in = fopen("small","r");
  FILE *out = fopen("small.out","w");
  int n;
  fscanf(in,"%d", &n);
  for (int i = 0; i < n; i++){
    map<pair<char,char>, char> change;
    map<pair<char,char>,bool> oposed;
    char fr1,fr2,to;
    int tmpn;
    fscanf(in," %d ",&tmpn);
    for (int j = 0; j < tmpn; j++){
      fscanf(in," %c%c%c ",&fr1,&fr2,&to);
      change[pair<char,char>(fr1,fr2)]=to;
      change[pair<char,char>(fr2,fr1)]=to;
    }
    fscanf(in," %d ",&tmpn);
    for (int j = 0; j < tmpn; j++){
       fscanf(in," %c%c ",&fr1,&fr2);
       oposed[pair<char,char>(fr1,fr2)]=true;
       oposed[pair<char,char>(fr2,fr1)]=true;
    } 
    fscanf(in," %d ",&tmpn);
    char line[200]="";
    int wh=0;
    for(int j = 0; j < tmpn; j++){
      fscanf(in,"%c",&fr1);
      line[wh]=fr1; wh++;
      if (wh > 1) if (change.find(pair<char,char>(line[wh-1],line[wh-2])) != change.end()){
        line[wh-2]=change[pair<char,char>(line[wh-1],line[wh-2]) ];
        wh--;
      }
      for(int k = 0; k < wh-1; k++){
        if(  oposed.find(pair<char,char>(line[wh-1],line[k])) != oposed.end()){
          wh=0;
        }
      }
    }
    printf("Case #%i: [",i+1);
     for(int k = 0; k < wh; k++){
       printf("%c",line[k]);
       if (k !=wh-1)printf(", ");
     }
     printf("]\n");
 
  }

}
