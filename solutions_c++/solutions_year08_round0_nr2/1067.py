#include<iostream>
#include<vector>
#include<sstream>
using namespace std ;
int turn,na,nb ;
string a1[105],a2[105],b1[105],b2[105] ;

vector<int> g[502] ;
int matchL[502],matchR[502] ;
bool visited[502] ;
bool bpm(int u)
{
 for(int i=0;i<g[u].size();i++) 
  if(!visited[g[u][i]])
  {
   visited[g[u][i]] = true ;
   if(matchR[g[u][i]] < 0 || bpm(matchR[g[u][i]]))
   {
    matchR[g[u][i]] = u ;
    matchL[u] = g[u][i] ;
    return true ;
   }
  }
 return false ;     
}

bool check(string t1,string t2)
{
 int i,j,k ;
 for(i=0;i<t1.size();i++) if(t1[i] == ':') t1[i] = ' ' ;    
 for(i=0;i<t2.size();i++) if(t2[i] == ':') t2[i] = ' ' ;    
 int h1,m1,h2,m2 ;
 istringstream iss1(t1) ; iss1 >> h1 >> m1 ;
 istringstream iss2(t2) ; iss2 >> h2 >> m2 ;
 m1 += turn ; h1 +=  m1/60 ; m1 %= 60 ;
 if(h1 > h2 || h1 == h2 && m1 > m2) return false ;
 return true ;
}

main()
{
 int i,j,k,runs ;

 freopen("a.in","r",stdin) ;
 freopen("out.txt","w",stdout) ;
 cin >> runs ;
 for(int t=1;t<=runs;t++)
 {
  cin >> turn >> na >> nb ;
  for(i=0;i<na;i++) cin >> a1[i] >> a2[i] ;
  for(i=0;i<nb;i++) cin >> b1[i] >> b2[i] ;
  for(i=0;i<500;i++) g[i].clear() ;
  for(i=0;i<na;i++)
   for(j=0;j<nb;j++)
   { 
    if(check(a2[i],b1[j]))
     g[i].push_back(na+nb+na+j) ;
    if(check(b2[j],a1[i]))
     g[na+j].push_back(na+nb+i) ;
   }
/*  
  for(i=0;i<na+nb;i++)
  {
   cout << i << ": " ;
   for(j=0;j<g[i].size();j++) cout << g[i][j] << " " ;
   cout << endl ;                   
  }
*/
  memset(matchL,255,sizeof matchL) ;
  memset(matchR,255,sizeof matchR) ;
  int ctotal = 0 ;
  for(i=0;i<na+nb;i++)
  {
   memset(visited,0,sizeof visited) ;                   
   if(bpm(i)) ctotal ++ ;
  }
  int ca = 0,cb = 0 ;
  for(i=0;i<na;i++) if(matchR[na+nb+i] == -1) ca ++ ;
  for(i=0;i<nb;i++) if(matchR[na+nb+na+i] == -1) cb ++ ;
  printf("Case #%d: %d %d\n",t,ca,cb) ;
 }
// while(1) ;
}
