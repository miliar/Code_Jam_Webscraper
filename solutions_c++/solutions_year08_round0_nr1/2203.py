#include<string>
#include<algorithm>
#include<map>
#include<math.h>
#include<string.h>
#include<ctype.h>
#include<vector>
#include<string>
#include<algorithm>
#include <utility>
#include<sstream>
#include<limits.h>
#define dbg(x) cout<<"$"<<x<<endl;
using namespace std;
 
#define sz(a) int((a).size()) 
#define pb push_back 
#define all(c) (c).begin(),(c).end() 
#define REP(i,n) for(int _n=n, i=0;i<_n;++i)
#define FOREACH(it,c) for(typeof((c).begin()) it=(c).begin();it!=(c).end();++it)

typedef vector<int> vi; 
typedef vector<vi> vvi; 
typedef pair<int,int> ii; 

#define present(c,x) ((c).find(x) != (c).end()) 
#define cpresent(c,x) (find(all(c),x) != (c).end()) 



#include<iostream.h>
#include<conio.h>


int main()
{
  int n;
  cin>>n;
  
  vector<string> result(n);
  REP(i,n)
  {
                 int steps=0;
                 int s;  cin>>s;
                 cin.ignore();
                 vector<string> engines(s);
                 vector<string> stored;
                 REP(j,s)
                 {
                   getline(cin,engines[j],'\n');
                   
                 }
                 
                 int q;cin>>q;
                 cin.ignore();
                 vector<string> queries(q);
                 REP(j,q)
                 {
                         getline(cin,queries[j],'\n');       
                 }
                 int c=0;
                 REP(j,sz(queries))
                 {
                    
                     if(find(all(stored),queries[j])!=stored.end())continue;
                     else
                     {
                         
                          //dbg(steps);
                             if(sz(stored)==sz(engines)-1)
                             {
                                                        steps++;
                                                        stored.clear();
                                                        stored.pb(queries[j]);
                             }
                             else
                             {
                              stored.pb(queries[j]);
                             }
                     }              
                 }
                 int y=i+1;
                 char f[10];
                // cout<<(char)y<<"hi"<<endl;
                 result[i]="Case #" ;
                 result[i]+=itoa(y,f,10);
                 result[i] += ":";
                 result[i] += " ";
                 result[i] +=itoa(steps,f,10);
  }
      
      REP(i,sz(result))
      {
              cout<<result[i]<<endl;
      }
      getch();
      
}
