#include <iostream>
#include <string>
#include <vector>
#include <map>

using namespace std;

int N,M,tc;
int nw,lg,ans;
string rs,ds;
map <string, int> dir;


int main()
{
 cin >> tc;
 for(int tt=0;tt<tc;tt++)
 {
  cin >> N >> M;
  ans = 0;  
  dir.clear();
    
  for(int i=0;i<N;i++)
  {
   cin >> rs;
   nw = 1;
   lg = rs.length();
   ds = "/";
   while(nw<lg)
   {
   while(nw<lg && rs[nw]!='/'){ds+= rs[nw]; nw++;} 
   //cout << ds << endl;
   //cout << nw << " " << lg << endl;
   map <string, int> ::iterator iter = dir.find(ds);
   if(iter==dir.end())
   {
    dir.insert(make_pair(ds,0));
   }
   
   if(nw<lg) {ds+= rs[nw]; nw++;}
   }
   }
  
  for(int i=0;i<M;i++)
  {
   cin >> rs;
   nw = 1;
   lg = rs.length();
   ds = "/";
   while(nw<lg)
   {
   while(nw<lg && rs[nw]!='/'){ds+= rs[nw]; nw++;} 
   map <string, int> ::iterator iter = dir.find(ds);
   if(iter==dir.end())
   {
    dir.insert(make_pair(ds,0));
    ans++;
   }
   if(nw<lg) {ds+= rs[nw]; nw++;}
   }
  }
  
  cout << "Case #" << tt+1 << ": ";
  cout << ans << endl;
 }
}
