#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>
#include <math.h>
using namespace std;

typedef pair<int,int> ii;

#define INF 2000000000
#define FOR(i,a,n) for(int i=a,_n=n; i<_n; i++)

int main(){
    freopen("input.in", "r", stdin);
    freopen("output.out", "w", stdout);
    int tcase = 1;
    int t; scanf("%d", &t);
    
    while (t--){
          int c, d, n;
          char s1[5], s3[105];
          map <string, char> invoke;
          map <string, int> hilang;
          vector <char> spell;
          
          scanf("%d", &c);
          FOR (i, 0, c){
              scanf("%s", s1);
              string temp; temp = s1[0]; temp+= s1[1];
              invoke[temp] = s1[2]; 
              temp = s1[1]; temp += s1[0];
              invoke[temp] = s1[2];   
          } 
          
          scanf("%d", &d);
          FOR (i, 0, d){
              scanf("%s", s1);
              string temp = s1;
              hilang[s1] = 1;
              reverse(temp.begin(), temp.end());
              hilang[temp] = 1;    
          }
          
          scanf("%d", &n);
          scanf("%s", s3);
          
          FOR (i, 0, n){
              spell.push_back(s3[i]);
              if ( spell.size() == 1 ) continue;
              
              int x = spell.size();
              string temp;
              temp = spell[x-1];
              temp += spell[x-2];
              //printf("temp = %s\n", temp.c_str());
              if ( invoke.count(temp) ){
                   //printf("di dalam invoke: temp = %c\n", invoke[temp]);
                 spell.pop_back(); spell.pop_back(); spell.push_back(invoke[temp]);     
              }
              
              bool bersih = false;
              FOR (j, 0, spell.size()-1){
                  if ( bersih ) break;
                  FOR (k, j+1, spell.size()){
                      temp = spell[j];
                      temp += spell[k];
                      if ( hilang.count(temp) ){
                         bersih = true;
                         spell.clear();     
                      }    
                  }    
              }    
          } 
          
          printf("Case #%d: [", tcase++);
          FOR (i, 0, spell.size() ){
              if ( i != 0 ) printf(", ");
               printf("%c", spell[i]); 
          }
          printf("]");
          puts("");                    
    }

    return 0;
}
