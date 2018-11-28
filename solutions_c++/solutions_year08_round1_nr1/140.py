#include <iostream>
#include <algorithm>

using namespace std;

int nt;
int i,j;
int n[1002];
int v1[802];
int v2[802];

int main(){
     freopen("a.in","r",stdin);
     freopen("a.out","w",stdout);
     scanf("%i", &nt);
     for(i=0;i<nt;i++){
          scanf("%i", &n[i]);
          for(j=0;j<n[i];j++){
               scanf("%i", &v1[j]);
          }
          for(j=0;j<n[i];j++){
               scanf("%i", &v2[j]);
          }
          sort(v1,v1+n[i]);
          sort(v2,v2+n[i]);
          int tmp;
          for(j=0;j<n[i]/2;j++){
               tmp=v2[j];
               v2[j]=v2[n[i]-j-1];
               v2[n[i]-j-1]=tmp;
          }
          int sum=0;
          for(j=0;j<n[i];j++)
               sum+=v1[j]*v2[j];
          printf("Case #%i: %i\n",i+1,sum);
     }
     
     fclose(stdin);
     fclose(stdout);
}
