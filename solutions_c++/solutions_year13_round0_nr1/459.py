#include <iostream> 
#include <sstream> 
#include <string> 
#include <vector> 
#include <queue> 
#include <set> 
#include <map> 
#include <cstdio> 
#include <cstdlib> 
#include <cctype> 
#include <cmath> 
#include <list> 
#include <numeric>
#include <regex.h>  
using namespace std; 
 
typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef vector<string> vs; 
typedef vector<vs> vvs;
#define pb push_back 
#define sz(v) ((int)(v).size()) 
 
int main()
{
  int i=0,j=0,k=0; char buf[100000]="";

  int run, runs;
  scanf("%d", &runs);
  for(run=1;run<=runs;run++) {
    vs veld;
    for(j=0;j<4;j++) {
      scanf("%s",buf);
      veld.pb(buf);
    }
    printf("Case #%d: ", run);
  
    int x=0,o=0,dot=0;
    bool xwon=false, owon=false, full=true;
 
    //row
    for(j=0;j<4;j++) {
      x=0;o=0;
      for(i=0;i<4;i++) {
        if(veld[j][i]=='.') full=false;
        if(veld[j][i]=='T') { x++; o++; }
        if(veld[j][i]=='X') x++;
        if(veld[j][i]=='O') o++;
      }
      if(x==4) xwon=true;
      if(o==4) owon=true;
    }

    //col
    for(j=0;j<4;j++) {
      x=0;o=0;
      for(i=0;i<4;i++) {
        if(veld[i][j]=='.') full=false;
        if(veld[i][j]=='T') { x++; o++; }
        if(veld[i][j]=='X') x++;
        if(veld[i][j]=='O') o++;
      }
      if(x==4) xwon=true;
      if(o==4) owon=true;
    }

    //dia
      x=0;o=0;
      for(i=0;i<4;i++) {
        if(veld[i][i]=='.') full=false;
        if(veld[i][i]=='T') { x++; o++; }
        if(veld[i][i]=='X') x++;
        if(veld[i][i]=='O') o++;
      }
      if(x==4) xwon=true;
      if(o==4) owon=true;  

      x=0;o=0;
      for(i=0;i<4;i++) {
        if(veld[i][3-i]=='.') full=false;
        if(veld[i][3-i]=='T') { x++; o++; }
        if(veld[i][3-i]=='X') x++;
        if(veld[i][3-i]=='O') o++;
      }
      if(x==4) xwon=true;
      if(o==4) owon=true;  
  
  
    if(xwon) printf("X won\n");
    else if(owon) printf("O won\n");
    else if(full) printf("Draw\n");
    else printf("Game has not completed\n");
  }






  return 0;
}
