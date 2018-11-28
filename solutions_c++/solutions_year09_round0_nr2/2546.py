#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>
#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REP(i,a) for(int i=0;i<(a);i++)
#define ALL(i) i.begin(),i.end()
#define rALL(i) i.rbegin(),i.rend()
#define PB push_back

typedef vector<int> vi;
typedef vector<vector<int> > vvi;

template<class T> string i2a(T x) {ostringstream oss; oss<<x; return oss.str();}


int h, w;

vector<string> label;



//North, West, East, South.


int dx[]={0,-1,1,0};
int dy[]={-1,0,0,1};

bool isin(vector< vector<int> > a, int r, int c)
{
     REP(i,a.size()) if(a[i][0] == r && a[i][1] == c) return true;
     return false;     
}


bool ok(int r, int c)
{
     if(r>=0 && r<h && c>=0 && c<w) return true;
     return false;     
}


//find sinks
bool isSink(vector<vector<int> > map, int r, int c)
{
     int val =map[r][c];// map[r][c];
     REP(i,4) 
     {
              if(ok(r + dy[i], c + dx[i]))
              {
                      int cur = map[r + dy[i]][c + dx[i]];
                      if(val > cur) return false;
              }        
     }     
     return true;
}


void godown(vector<vector<int> > map, vector<string> &label, int r, int c, int curr, int curc)
{

     //printf("r=%d c=%d\n",r,c);
     int val = map[r][c];
     int minr=-1, minc=-1;
     label[r][c] = label[curr][curc];
     //if(r == 0 && c == 0) { label[curr][curc] = label[r][c]; return; }
     REP(i,4) 
     {
              if(ok(r + dy[i], c + dx[i]))
              {
                      int cur = map[r + dy[i]][c + dx[i]];
                      if(val > cur) { val = cur; minr = r + dy[i]; minc = c + dx[i];}
              }        
     }          
     if(minc == -1 && minr == -1) return;
      godown(map, label, minr, minc, curr, curc); 
     return ;
}

void godown2(vector<vector<int> > map, vector<string> &label, int r, int c, int curr, int curc)
{
     int val = map[r][c];
     int minr=-1, minc=-1;
     //label[r][c] = label[curr][curc];
     if(label[r][c]!='.') { label[curr][curc] = label[r][c]; return; }
     //if(r == 0 && c == 0) { label[curr][curc] = label[r][c]; return; }
     REP(i,4) 
     {
              if(ok(r + dy[i], c + dx[i]))
              {
                      int cur = map[r + dy[i]][c + dx[i]];
                      if(val > cur) { val = cur; minr = r + dy[i]; minc = c + dx[i];}
              }        
     }          
     if(minc == -1 && minr == -1) return;
      godown2(map, label, minr, minc, curr, curc); 
     return ;      
}


int main()
{
   
   freopen("b-small-x.in","r",stdin);
   freopen("B-small.out","w",stdout);
   
   
   int n;
   scanf("%d",&n);
  string alpha="abcdefghijklmnopqrstuvwxyz";
  
   REP(k,n)
   {
          
           scanf("%d %d",&h,&w);
           
           vector<vector<int> > map;
           REP(i,h)
           {
                 vector<int> tmp;
                 REP(i,w) tmp.PB(0);
                 map.PB(tmp);                 
           }
           REP(i,h) REP(j,w) scanf("%d",&map[i][j]);
           
           label.clear();
           
           REP(i,h)
           {
            string tmp;
            REP(i,w) tmp.PB('.');
            label.PB(tmp);        
           }
           
           
           REP(i,label.size()) REP(j,label[i].size()) label[i][j]='.';
           
           label[0][0]='a';
           
           char c = 'a';
           
           

           
           

           
           godown(map, label, 0, 0, 0, 0);
           
           
           
           vector< vector<int> > sinks;
           REP(i,h)REP(j,w) if(isSink(map,i,j)) {
                                if(label[i][j]=='a') { c = 'b';  }
                                vector<int> tmp;
                                tmp.PB(i); tmp.PB(j); sinks.PB(tmp);
                            }


           REP(i,h)REP(j,w) if(isin(sinks, i, j) && label[i][j]=='.') label[i][j] = c++;           
           
           
           
           REP(i,label.size()) REP(j,label[i].size()) if(label[i][j]=='.') godown2(map, label, i, j, i, j);
           printf("Case #%d:\n", k+1);
           REP(i,label.size()) {
                               printf("%c",label[i][0]);
                               FOR(j,1,label[i].size()) printf(" %c",label[i][j]);
                               printf("\n");                    
           }

   }


    getchar();
    return 0;
}
