#include <stdio.h>
#include <algorithm>
#include <stdlib.h>
using namespace std;

int bil[2000];
int sum;
int n;

bool cf(const long long a,const long long b){
     return a>b;     
}

int main(){
     int i,j,k,a,b,c,ind;
     
     scanf("%d",&n);
     for (i=0;i<n;i++){
          memset(bil,0,sizeof(bil));
          if (i>0) printf("\n");
          scanf("%d %d %d",&a,&b,&c);
          for (j=0;j<c;j++){
               scanf("%d",&bil[j]);    
          }    
          sort(bil,bil+c,cf);
          ind=0;
          sum=0;
          for (j=1;j<=a;j++)
               for (k=0;k<b;k++,ind++) sum+=(j*bil[ind]);
          printf("Case #%d: %d",i+1,sum);  
     }
     
     return 0;    
}
