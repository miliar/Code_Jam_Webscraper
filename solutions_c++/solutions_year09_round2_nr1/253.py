#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <iostream>
#include <sstream>
#include <memory>
#include <cctype>
#include <vector>
#include <string>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <iomanip>
using namespace std;

#define FOR( i , n ) for (int i = 0; i < n ; i++ )
#define debug(x) cout << #x" = " << x << "\n"
#define FORIT( i , c ) for ( __typeof((c).begin())  i  = (c).begin() ; (i) != (c).end() ; (i)++ )


double todouble(string s){
 stringstream ss(s);
 double ret;
 ss>>ret;
 return ret;
}

queue <string> ent;


void proc(string s){
  int i =0;
  while(i < s.size())
    {
    if(s[i]==' ') {i++;continue;}
    if(s[i]=='(') {
       ent.push("(");
       i++;
       continue;       
       }
    if(s[i]==')') {
       ent.push(")");
       i++;
       continue;       
       }
    if(s[i]=='0') {
      string cur = "0.";
      i+=2;
      while(s[i]>= '0' && s[i]<= '9' && i < s.size())
       cur += s[i++];
      ent.push(cur);
      continue;       
     }
    if(s[i]=='1') {
      string cur = "1.";
      i+=2;
      while(s[i]>= '0' && s[i]<= '9' && i < s.size())
       cur += s[i++];
      ent.push(cur);
      continue;       
     }
    string cur = "";
    while(s[i]>='a'&&s[i]<='z'&&i<s.size())
      cur+=s[i++];
    ent.push(cur);  
    }
}

double prob[5000];
string feat[5000];
int foui[5000];
int fnon[5000];
bool temfeat[5000];
vector <string> ftest;

int c;
int narbre(){
  ent.pop();
  int cur = c++;
  prob[cur] = todouble(ent.front()); 
  ent.pop();
  string s = ent.front();
  temfeat[cur]=0;
  if(s==")"){ ent.pop(); return cur;}
  temfeat[cur]=1;
  feat[cur] = ent.front();
  ent.pop();
  foui[cur] = narbre();
  fnon[cur] = narbre();
  ent.pop();
  return cur;
}


bool TEM(string s){
  FOR(i,ftest.size())
   if(ftest[i]==s) return true;
   return false;
}

double testa(int u){
  if (!temfeat[u]) return prob[u];
  if (TEM(feat[u]))
    return prob[u] * testa(foui[u]);
  return prob[u] * testa(fnon[u]);

}


int main() {
  int ca;
  cin>>ca;
  string s;
  getline(cin, s);
  
  FOR(cas, ca)
    {
      while(!ent.empty())
      ent.pop();
      getline(cin, s);
      stringstream ss(s);
      int L;
      ss>>L;
      FOR(i,L)
             {
          //   cout<<"a";
             getline(cin, s);
             proc(s);
             } 
      c=0;
      /*while(!ent.empty())
       {
       cout<<ent.front()<<"-";
       ent.pop();
       }
      */
      narbre();
      getline(cin, s);
      stringstream s2(s);
      int A;
      s2>> A;     
      cout<<"Case #"<<cas+1<<": "<<endl;
      FOR(a,A){
               getline(cin, s);
               stringstream s3(s);
               double p;
               s3>>s>>p;

               ftest.clear();
               while(s3>>s)
                 ftest.push_back(s);
               double ret = testa(0);               
               cout.setf(ios::fixed);
               cout<<setprecision(7)<< ret <<endl;
//               cout<<ret<<endl;
               }
      
      
      
      
    }
 return 0;
}
