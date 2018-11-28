#include <cstdio> 
#include <vector> 
#include <iostream> 
#include <string> 
#include <sstream> 
#include <algorithm> 
#include <map> 
#include <cmath> 
#include <cstdlib> 
using namespace std; 
#define sz size() 
#define pb push_back 
#define all(a) a.begin(),a.end() 
#define FOR(i,s,n) for(int i=s;i<n;++i) 

#define FORZ(i,n) FOR(i,0,n) 
#define inf (INT_MAX/2) 
typedef pair<int,int> ii; 
map<int,vector<int> > dp;
int googlers[50];

bool is_recycled(string a, string b) {
  string tmp = a + a.substr(0,a.length()-1);
  size_t found = tmp.find(b);
  return found != string::npos; 
}

string toString(int n) {
  string ret = "";
  if(n == 0) 
    ret = '0';
  while (n > 0) {
    ret += '0' + n%10 ;
    n /= 10;
  }
  return ret;
}


int find_recycledpairs(int A, int B) {
  int tot = 0;
  FOR(i,A,B+1)
    FOR(j,i+1,B+1) {
      string istr = toString(i);
      string jstr = toString(j);
      if(istr.length() == jstr.length() && 
          is_recycled(istr,jstr))
        ++tot;
    }
      
  return tot;
}

int main() {
  int t,c; 
  scanf("%d\n", &t);
  FOR(c,1,t+1) { 
   int A,B;
    scanf("%d %d", &A, &B);
    int tot = find_recycledpairs(A,B);
    cout << "Case #" << c << ": " << tot ;
    //cout << " " << is_recycled("123","122"); 
    if( c != t)
      cout << endl;
  }
}
