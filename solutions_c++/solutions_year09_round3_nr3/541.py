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

const int MAX=12;

int test,test_num=1;
int P,Q,Q_list[MAX],num;


ifstream fin("C-small-attempt0.in");
ofstream fout("output.txt");

int main()
{
      fin>>test;
      while(test)
      {
                 fin>>P>>Q;
                 FOR(i,Q)
                 {
                      fin>>num;   
                      Q_list[i]=num;
                 }
                 bool prison_cell[102];
                 int ans=INT_MAX;
                 string permu="";
                 FOR(i,Q)
                         permu+=('0'+i);
                 do
                 {
                         int cur_ans=0;
                         SET(prison_cell,0);                        
    //                     cout<<permu<<endl;
                         FOR(i,Q)
                         {
                              int released=Q_list[permu[i]-'0'];
                              prison_cell[released]=1;
//                              cout<<"Released "<<released<<endl;
                              int less=released-1,more=released+1;
                              while(less>0)
                              {
                                    if(prison_cell[less]==0)
                                       cur_ans++;
                                    else
                                        break;
                                    less--;
                              }
                              while(more<=P)
                              {
                                   if(prison_cell[more]==0)
                                       cur_ans++;
                                   else
                                       break;
                                    more++;
                              }
  //                            cout<<"Cur_ans= "<<cur_ans<<endl;
                         }  
                        ans=min(ans,cur_ans);
                 }while(next_permutation(permu.begin(),permu.end()));
                 fout<<"Case #"<<test_num<<": "<<ans<<endl;
                 test--;
                 test_num++;
      }
  //    cin>>test;
      return 0;
}
