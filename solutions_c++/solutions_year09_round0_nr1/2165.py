#include <vector>
#include <list>
#include <map>
#include <set>
#include <fstream>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
using namespace std;

#define RET return
#define FOR(i,n) for(int i=0;i<(int)n;++i)
#define SZ(n) ((int)n.size())

#define FORN(i,start,end) for(int i=start;i<end;++i)
#define FORD(i,n) for(int i=(int)n;i>=0;--i)
#define SET(a,n) memset(a,n,sizeof(a))
#define foreach(it,x) for(__typeof(x.begin()) it=x.begin();it!=x.end();++it)
#define PB push_back

typedef vector<string> VS;
typedef vector<int> VI;
typedef stringstream SS;

ifstream fin("A-large.in");
ofstream fout("output.txt");

int test,num_test=1,L,D,ans=0;

bool valid_string(string str,string reg_ex)
{
     int reg_ln=SZ(reg_ex),reg_index=0;
     FOR(i,L)
     {
           if(reg_ex[reg_index]=='(')
           {
                  string possible="";
                  while((reg_index<reg_ln)&&(reg_ex[reg_index]!=')'))
                  {
                          possible+=reg_ex[reg_index];
                          reg_index++;                                          
                  }
                  if(possible.find(str[i])==string::npos)
                             RET 0;
                  reg_index++;
           }
           else if(reg_ex[reg_index]==str[i])
           {
                 reg_index++;
                 continue;
           }
           else
                 RET 0;  
     }
     RET 1;
}

int main()
{
      fin>>L>>D>>test;
      string input;
      VS input_array;
      FOR(i,D)
     {
             fin>>input;
             input_array.PB(input);
     }
      while(test)
      {
                 ans=0;
                 fin>>input;
                 FOR(i,D)
                 {
                        if(valid_string(input_array[i],input))
                                 ans++;
                 }
                 fout<<"Case #"<<num_test<<": "<<ans<<endl;
                 num_test++;
                 test--;
      }
      return 0;
}
