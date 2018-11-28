//MADE BY lordmonsoon A.I.
#include<string>
#include<vector>
#include<algorithm>
#include<queue>
#include<map>
#include<set>
#include<cmath>
#include<cstdio>
#include<cstring>
#include<sstream>
#include<iostream>
#include<utility>
#include<bitset>

using namespace std;

#define pi pair<int,int>
#define vi vector<int>
#define vpi vector<pi>
#define fst first
#define snd second
#define pb push_back
#define SIZE(a) (int)(a.size())
#define LENGTH(a) (int)(a.length())
#define REP(i,n) for(int i=0;i<(n);i++)
#define REPD(i,n) for(int i=(n);i>=0;i--)
#define FOR(i,n,m) for(int i=(n);i<=(m);i++)
#define FORD(i,n,m) for(int i=(n);i>=(m);i--)
#define MIN(a,b) ((a)<(b) ? (a) : (b))
#define MAX(a,b) ((a)<(b) ? (b) : (a))
#define ABS(a) ( (a)<0 ? -(a) : (a))
#define STRUMIEN(A,B) istringstream A(B)
#define SORT(A) sort(A.begin(),A.end())


////////////////////////////////////////////////////////////////////////////////

int t,n;
char bufor[10000],m;
vpi PT;

bool checkV(int x,int y)
{
      bool gut = false, gut2 = false;
      REP(i,SIZE(PT)) 
      {
            if(PT[i].fst == x && PT[i+1].fst == x + 1 && PT[i].snd <= y) gut = true;
            else if(PT[i].fst == x + 1 && PT[i+1].fst == x && PT[i].snd <= y) gut = true;

            if(PT[i].fst == x && PT[i+1].fst == x + 1 && PT[i].snd >= y+1) gut2 = true;
            else if(PT[i].fst == x + 1 && PT[i+1].fst == x && PT[i].snd >= y+1) gut2 = true;
      }
      return gut2 && gut;
}

bool checkP(int x,int y)
{
      bool gut = false, gut2 = false;
      REP(i,SIZE(PT)-1) 
      {
            if(PT[i].snd == y && PT[i+1].snd == y + 1 && PT[i].fst <= x) gut = true;
            else if(PT[i].snd == y + 1 && PT[i+1].snd == y && PT[i].fst <= x) gut = true;

            if(PT[i].snd == y && PT[i+1].snd == y + 1 && PT[i].fst >= x+1) gut2 = true;
            else if(PT[i].snd == y + 1 && PT[i+1].snd == y && PT[i].fst >= x+1) gut2 = true;
      }
      return gut2 && gut;
}

int main()
{
      scanf("%d",&t);
      FOR(t2,1,t)
      {
            long long area = 0;
            scanf("%d",&n);
            PT.clear();
            int x = 0, y = 0,dir = 0;
            PT.pb(pi(0,0));
            REP(i,n)
            {
                  int cnt;
                  scanf(" %s %d ",bufor,&cnt);
                  m = strlen(bufor);
                  while(cnt>0)
                  {
                        cnt--;
                        REP(j,m)
                        {
                              if(dir == 0)
                              {
                                    if(bufor[j] == 'F') {y++;PT.pb(pi(x,y));}
                                    else if(bufor[j] == 'L') {dir = 3;}
                                    else dir = 1;
                              }
                              else if(dir == 1)
                              {
                                    if(bufor[j] == 'F') {x++;PT.pb(pi(x,y));}
                                    else if(bufor[j] == 'L') {dir = 0;}
                                    else dir = 2;
                              }
                              else if(dir == 2)
                              {
                                    if(bufor[j] == 'F') {y--;PT.pb(pi(x,y));}
                                    else if(bufor[j] == 'L') {dir = 1;}
                                    else dir = 3;
                              }
                              else if(dir == 3)
                              {
                                    if(bufor[j] == 'F') {x--;PT.pb(pi(x,y));}
                                    else if(bufor[j] == 'L') {dir = 2;}
                                    else dir = 0;
                              }
                        }
                  }
            }
//            REP(i,SIZE(PT)) printf("%d %d\n",PT[i].fst,PT[i].snd);
            long long first = 0;
            REP(i,SIZE(PT)-1) first += PT[i].fst * PT[i+1].snd - PT[i].snd * PT[i+1].fst;
            if(first<0) first = -first;first/=2;
            long long second = 0;
            FOR(i,-101,101) FOR(j,-101,101) if(checkP(i,j) || checkV(i,j)) second++;
            printf("Case #%d: %I64d\n",t2,second-first);
      }
      return 0;
}
