#include<iostream>
#include<vector>
using namespace std;
int main() {
     int T, N, S, p, t, i, j,count,temp;
     vector<int> v;
     scanf("%d",&T);
     for(i=0; i<T; i++) {
          count=0;
          scanf("%d%d%d",&N,&S,&p);
          temp=S;
          for(j=0; j<N; j++) {
               scanf("%d",&t);
               v.push_back(t);
          }
          for(j=0; j<N; j++) {
               if(v[j]%3==1) {
                    if(v[j]/3>=p-1) {
                         count++;
                    }
               } else if(v[j]%3==0) {
                    if(v[j]/3>=p) {
                         count++;
                    } else if(v[j]/3==p-1 && temp>0 && v[j]>0) {
                         count++;
                         temp--;
                    }
               } else {
                    if(v[j]/3>=p-1) {
                         count++;
                    } else if(v[j]/3==p-2 && temp>0) {
                         count++;
                         temp--;
                    }
               }
          }
          printf("Case #%d: %d\n",i+1,count);
          v.clear();
     }
     return 0;
}
