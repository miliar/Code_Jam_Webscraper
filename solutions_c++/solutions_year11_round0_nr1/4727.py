#include <iostream>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <stack>
#include <bitset>
#include <algorithm>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cstring>
#include <climits>
using namespace std;

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> pii; 

#define				pb	push_back
#define	 present(x, c)	((c).find(x) != (c).end()) 			// used for map and set. //
#define		forn(i, n)	for(int i = 0; i < n; i++)
#define             S   scanf
#define             P   printf

int idx=1;
void proc()
{
                int n,i,u,j,x,y,b,o,p;
                char ch;
                int time;
                vector<char> moves;
                vi O;
                vi B;
                time=0;
              cin>>n;
              for(i=0;i<n;i++)
              {
                              cin>>ch;
                              moves.pb(ch);
                              if(ch=='B') { cin>>p; B.pb(p); }
                              if(ch=='O') { cin>>p; O.pb(p); }
                                             
              }
              int bs=B.size();
              int os=O.size();
              x=0;y=0;
              b=1;o=1;
              for(i=0;i<moves.size();i++)
              {
                                         if(moves[i]=='B')
                                         {
                                                          while(b!=B[x])
                                                          {
                                                                        time++;
                                                                        if(x<bs){
                                                                        if(B[x]>b) b++;
                                                                        if(B[x]<b) b--;
                                                                        }
                                                                        
                                                                        if(y<os){
                                                                        if(O[y]>o) o++;
                                                                        if(O[y]<o) o--;
                                                                        } 
                                                          }
                                                          time++;
                                                          if(y<os){
                                                          if(O[y]>o) o++;
                                                          if(O[y]<o) o--;
                                                          }
                                                          x++;
                                                          
                                         }
                                         if(moves[i]=='O')
                                         {
                                                          while(o!=O[y])
                                                          {
                                                                        time++;
                                                                        if(x<bs){
                                                                        if(B[x]>b) b++;
                                                                        if(B[x]<b) b--;
                                                                        }
                                                                        
                                                                        if(y<os){
                                                                        if(O[y]>o) o++;
                                                                        if(O[y]<o) o--;
                                                                        } 
                                                          }
                                                          time++;
                                                          if(x<bs){
                                                          if(B[x]>b) b++;
                                                          if(B[x]<b) b--;
                                                          }
                                                          y++;
                                                          
                                         }
                                      
              }
              printf("Case #%d: %d\n",idx++,time);
}

int main()
{
    int t;
    cin>>t;
    while(t--)
    {
              proc();
    }


  return 0;
}
