#include <cstdio>
#include <iostream>
#include <algorithm>
#include <set>
#include <map>
#include <stack>
#include <list>
#include <queue>
#include <deque>
#include <cctype>
#include <string>
#include <vector>
#include <sstream>
#include <iterator>
#include <cmath>
#include<stdio.h>

using namespace std;

typedef vector <int > VI;
typedef vector < VI > VVI;
typedef long long LL;
typedef long long ll;
typedef vector < LL > VLL;
typedef vector < double > VD;
typedef vector < string > VS;
typedef pair<int,int> PII;
typedef vector <PII> VPII;
typedef istringstream ISS;

#define ALL(x) x.begin(),x.end()
#define REP(i,n) for (LL i=0; i<n; ++i)
#define FOR(var,pocz,koniec) for (LL var=pocz; var<=koniec; ++var)
#define FORD(var,pocz,koniec) for (int var=pocz; var>=koniec; --var)
#define FOREACH(it, X) for(__typeof(X.begin()) it = X.begin(); it != X.end(); ++it)
#define PB push_back
#define PF push_front
#define MP(a,b) make_pair(a,b)
#define ST first
#define ND second
#define SIZE(x) (int)x.size()

#define AND &&
#define OR ||

struct point{ int x;int y;};

int main()
    {
    int C;
    long long A[1000];
    int M[1000], N[1000];
    
    cin>>C;
    for (int i=0;i<C;i++)
        {
        cin>>N[i]>>M[i]>>A[i];
        }
        
        
    long long Area;
    int break1,solved;
     point Gr[2601];
    for (int i=0;i<C;i++)
    {
   
     int count=0;
     for (int a=0;a<=M[i];a++)
         for (int b=0;b<=N[i];b++)
             {Gr[count].y=a;Gr[count++].x=b;}    
        
    break1=1,solved=0;
    if (M[i]*N[i]<A[i])
       {
       cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;
       continue;
       }
                       
    for (int p1=0;p1<count && break1 ;p1++)
        {
                 for (int p2=p1+1;p2<count && break1 ;p2++)
                     {
                              for (int p3=p2+1;p3<count && break1 ;p3++)
                                  {
                        
                                               Area=abs((Gr[p2].x*Gr[p3].y-Gr[p3].x*Gr[p2].y)-(Gr[p1].x*Gr[p3].y-Gr[p3].x*Gr[p1].y)+ (Gr[p1].x*Gr[p2].y-Gr[p2].x*Gr[p1].y));
                                               if (Area==A[i])
                                                  {
                                                  cout<<"Case #"<<i+1<<": "      <<Gr[p1].x<<" "
                                                                                 <<Gr[p1].y<<" "
                                                                                 <<Gr[p2].x<<" "
                                                                                 <<Gr[p2].y<<" "
                                                                                 <<Gr[p3].x<<" "
                                                                                 <<Gr[p3].y<<" "<<endl;
                                                  break1=0;                               
                                                  solved=1;
                                                  }
                                                  }
                                                  }
                                                  }
                                               if (solved==0)  
                                                   cout<<"Case #"<<i+1<<": IMPOSSIBLE"<<endl;    
                                               }                                               
                                                    

    }
