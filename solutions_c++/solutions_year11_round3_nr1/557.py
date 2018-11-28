#include <iostream>
#include <algorithm>
#include <vector>
#include <cmath>
#include <cstdio>
#include <string>
#include <stack>
#include <queue>
#include <set>
#include <map>
#include <string.h>
#include <cassert>

using namespace std;

#define GI ({int t;scanf("%d",&t);t;})
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define pb push_back
#define sz size()
#define INF (int)1e9

typedef long long LL;
typedef vector<int> VI;
typedef vector<string> VS;
typedef vector<vector<int> > VVI;
typedef pair<int,int> PII;

int main()
{
 int testcases,r,c,temp = 1,mammy;
 scanf("%d",&testcases);
 for(int tc=1;tc<=testcases;tc++) {
 scanf("%d %d",&r,&c);
 char pappu[r][c];
 for(int i = 0; i < r; i++)
 for(int j = 0; j < c; j++)
 cin>>pappu[i][j];


           printf("Case #%d: \n",tc);          
           mammy = 1;
           for(int i = 0; i < r; i++)
           {  for(int j = 0; j < c; j++)      {                if(pappu[i][j] == '#' )           {
                                      if(pappu[i][j+1] == '#' && pappu[i+1][j] == '#' && pappu[i+1][j+1]== '#')
                                      {
                                                   pappu[i][j] = '/';                                                   pappu[i][j+1] = '\\';
                                                   pappu[i+1][j] = '\\';
                                                   pappu[i+1][j+1] = '/';                                                         }
                                      else
                                       {   
                                           mammy = 0;                                    break;
                        }
                           }
                   }
                   if(mammy == false)
                           break;
           }     
           if(mammy)
           {
                   for(int i = 0; i < r; i++)                    {
                                  for(int j = 0; j < c; j++)                                          cout<<pappu[i][j];
                                  cout<<endl;
                    }  
           }
           else
               cout<<"Impossible"<<endl;
}

return 0;
} 
