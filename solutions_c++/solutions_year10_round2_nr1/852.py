#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <algorithm>
#include <iostream>
#include <queue>
#include <map>
#include <string>

using namespace std;

#undef SMALL

map<string , int> mp;
char str[200];

int main(){
      #ifdef SMALL
      freopen("a-small.in" , "rt" , stdin);
      freopen("a-small.out" , "wt" , stdout);
      #else
      freopen("a-large.in" , "rt" , stdin);
      freopen("a-large.out" , "wt" , stdout);
      #endif

      int tst , kase = 1 , n , m , i , j;
      scanf("%d" , &tst);
      while(tst--){
            scanf("%d%d" , &n , &m);
            int ret = 0 , ln;
            gets(str);
            string s;
            for(i = 0;i<n;i++){
                  gets(str);
                  s= "" + '/';
                  ln = strlen(str);
                  str[ln] = '/';
                  for(j = 1;j<=ln;j++){
                        if(str[j] == '/'){
                              if(!mp[s]) mp[s] = 1;
                        }
                        s += str[j];
                  }
            }
            for(i = 0;i<m;i++){
                  gets(str);
                  s = "" + '/';
                  ln = strlen(str);
                  str[ln] = '/';
                  for(j = 1;j<=ln;j++){
                        if(str[j] == '/'){
                              if(!mp[s]){
                                    mp[s] = 1;
                                    ret++;
                              }
                        }
                        s += str[j];
                  }
            }
            printf("Case #%d: %d\n" , kase++ , ret);
            mp.clear();
      }
      return 0;
}
