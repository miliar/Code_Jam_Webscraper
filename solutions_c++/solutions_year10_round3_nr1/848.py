#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <queue>
#include <map>
#include <string>
#include <vector>

using namespace std;

#undef SMALL

vector< pair<int , int> > vpi;

bool comp(pair<int , int> a , pair<int , int> b){
      return a.first < b.first;
}

int main(){
      #ifdef SMALL
      freopen("a-small.in" , "rt" , stdin);
      freopen("a-small.out" , "wt" , stdout);
      #else
      freopen("a-large.in" , "rt" , stdin);
      freopen("a-large.out" , "wt" , stdout);
      #endif

      int tst , kase = 1 , n , i , ai , bi;
      scanf("%d" , &tst);
      while(tst--){
            scanf("%d" , &n);
            for(i = 0;i<n;i++){
                  scanf("%d%d" , &ai , &bi);
                  vpi.push_back(make_pair(ai , bi));
            }
            sort(vpi.begin() , vpi.end() , comp);

            int ret = 0 , j;
            for(i = 0;i<n;i++){
                  for(j = i+1;j<n;j++)
                        if(vpi[i].second > vpi[j].second)
                              ret ++;
            }
            printf("Case #%d: %d\n" , kase++ , ret);
            vpi.clear();
      }
      return 0;
}
