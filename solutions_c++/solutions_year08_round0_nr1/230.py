#include<iostream>
#include<sstream>
#include<cstdio>
#include<algorithm>
#include<string>
#include<vector>
#include<cmath>
#include<set>
#include<map>
#include<stack>
#include<queue>
#include<numeric>
#include<functional>
#include<complex>

using namespace std;

#define FOR(i,n)  for(int i=0;i<(int)(n);i++)
#define SZ(x) ((int)(x).size())
bool exist[1256];
int main()
{
  int n , case_no=1; 
  cin>>n;
  while(n--)
    {
      int s,q;
      cin>>s;
      vector<string> name(s); 
      map<string,int> toindex;
      string line;
      getline(cin,line);
      FOR(i,s){
        getline(cin,line);
        name[i] = line;
        toindex[line] = i;
      }
      cin>>q;
      vector<int> data(q);
      getline(cin,line);
      FOR(i,q){
        getline(cin,line);
        data[i] = toindex[line];
      }
      int turn = 0 , cnt = 0;
      memset(exist , 0 , sizeof(exist));
      FOR(i,q){
        int p = data[i];
        if(!exist[p]){
          cnt++ ; 
          exist[p]=true;
        }
        if(cnt==s){
          cnt=1;
          memset(exist , 0 , sizeof(exist));
          exist[p]=true;
          turn++;
        }
      }
      printf("Case #%d: %d\n" , case_no++ , turn);
    }
  return 0 ;
}
