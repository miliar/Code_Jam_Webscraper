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

int stoi(string s)
{
    SS ss(s);
    int ret;
    ss>>ret;
    RET ret;
}


int test,test_num=1;
long long int ans;

ifstream fin("A-large.in");
ofstream fout("output.txt");

string input,uniq_order_input="";
int uniq_cnt=0,input_ln;


void toDecimal(string n, int b)
{
   long long int result=0,n_ln=input_ln-1;
   long long int multiplier=1;
   if(b==1)
       b=2;
  // cout<<n<<" "<<b<<endl;
   while(n_ln>=0)
   {
      if((n[n_ln]>='0')&&(n[n_ln]<='9'))        
            result+=(n[n_ln]-'0')*multiplier;
      else
            result+=(n[n_ln]-'a'+10)*multiplier;
      multiplier*=b;
      n_ln--;
   }
   ans=result;
   return ;
}

void find_min_value(int base)
{
     int cur_base=0,flag=0,cnt_flag=0;
     bool visited[1001];
     SET(visited,0);
     FOR(i,base)
     {
                FOR(j,input_ln)
                {
                          if((input[j]==uniq_order_input[i])&&(!visited[j]))
                          {
                                    if((cur_base==0)&&(j==0))
                                    {
                                              flag=1;
                                              cur_base=1;               
                                              cnt_flag=1;
                                    }
                                    if((cnt_flag)&&(cur_base==1)&&(!flag))
                                          cur_base++;
                                    if(cur_base>=10)
                                         input[j]='a'+(cur_base-10);
                                    else
                                         input[j]=('0'+cur_base);                       
                                    visited[j]=1;
                          }     
                }
                cur_base++;
                if(flag)
                {
                     flag=0;   
                     cur_base=0;
                }
    //            cout<<"Finding in "<<i<<" "<<input<<endl;
     }
     toDecimal(input,uniq_cnt);
     
}

int main()
{
      fin>>test;
      while(test)
      {
                 uniq_order_input="";
                 fin>>input;
                 map<char,bool> input_chars;
                 uniq_cnt=0;
                 input_ln=SZ(input);
                 FOR(i,input_ln)
                 {
                       if((input_chars.count(input[i]))==0)
                       {
                              input_chars[input[i]]=1;
                              uniq_cnt++;
                              uniq_order_input+=input[i];                             
                       }
                 }
                 find_min_value(uniq_cnt);
                 fout<<"Case #"<<test_num<<": "<<ans<<endl;
                 test--;
                 test_num++;
      }
      return 0;
}
