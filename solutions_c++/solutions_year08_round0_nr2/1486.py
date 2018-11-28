#include<stdio.h>
#include<string.h>
#include<string>
#include<vector>

using namespace std;

struct node {
       int dep,arr;       
};

vector<node> fromA,fromB;
int main() {
    
    freopen("b.in","r",stdin);
    freopen("b.out","w",stdout);
    
    int test;
    int kase=1;
    int na,nb;
    int turn;
    scanf("%d",&test);
    while (test--) {
          scanf("%d",&turn);
          scanf("%d %d",&na,&nb);
          fromA.clear();
          fromB.clear();
          int i;
          int a,b,c,d;
          for (i=0;i<na;i++) {
              scanf("%d:%d %d:%d",&a,&b,&c,&d);
              node tempn;
              tempn.dep = a*60+b;
              tempn.arr = c*60+d;
              fromA.push_back(tempn);
          }
          for (i=0;i<nb;i++) {
              scanf("%d:%d %d:%d",&a,&b,&c,&d);
              node tempn;
              tempn.dep = a*60+b;
              tempn.arr = c*60+d;
              fromB.push_back(tempn);
          }
          int starta=0, startb=0;
          int ata=0,atb=0;
          for(i=0;i<=23*60+59;i++) {
            int j;
            for (j=0;j<na;j++) {
                if ( fromA[j].arr + turn == i )
                 atb++;      
            }
            for (j=0;j<nb;j++)
               if( fromB[j].arr + turn == i )
                   ata++;
            for( j=0;j<na;j++)
                 if ( fromA[j].dep == i ) {
                    if ( ata == 0 )
                       ata=1, starta++;
                    ata--;
                 }
           for ( j=0;j<nb;j++)
               if ( fromB[j].dep == i ) {
                  if ( atb == 0 )
                     atb=1,startb++;
                  atb--;
               }      
          }
         printf("Case #%d: %d %d\n",kase++,starta,startb);    
    }
    return 0;
}
