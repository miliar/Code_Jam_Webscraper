#include <iostream>
#include <iomanip>
#include <vector>
#include <list>
#include <string>
#include <queue>
#include <set>
#include <map>
#include <algorithm>
#include <bitset>
#include <limits>
#include <iterator>
#include <sstream>

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <ctime>
#include <cassert>

using namespace std;

#define FOR(i, a, b) for (int i = (a), _b = (b); i != _b; ++i)
#define REP(i, N) FOR(i, 0, N)
#define REPK(K) REP(_crazyName, K)

#define ALL(x) (x).begin(), (x).end()
#define RALL(x) (x).rbegin(), (x).rend()

#define OR ||
#define AND &&

#define sz() size()
#define len() length()
#define mp(a, b) make_pair(a, b)
#define pb(x) push_back(x)

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<string> VS;
typedef long long LL;

int main()
{

 int N;
 int cnt = 0;
 cin>>N;
 
 cnt =1;
 while(cnt<=N)   
    {
                string word;
                cin>>word;
                
                vector <char> list;
                map <char, long > setval;
                
                for(int i=0;i<word.length();i++)
                {
                        int j;
                        for( j=0;j<list.size();j++)
                        {if(list[j] == word[i])break;}
                        if(j==list.sz()){list.pb(word[i]);setval[word[i]] = 0;}
              }
                
                //cout<<list.sz()<<endl;
                if(list.sz() == 1){cout<<"Case #"<<cnt<<": "<<int(pow(double(2),double(word.length()))-1)<<endl;cnt++;continue;}
                vector <int> vals;
                 
                long mul = 1;
                long power = list.sz();         
                for(int i=word.length()-1;i>=0;i--)
                {
                        setval[word[i]] += mul;
                        //cout<<word[i]<<":"<<setval[word[i]]<<endl;
                        mul *= power;
                }
                vector < pair <int , char> > bigl;
                for(int l=0;l<list.sz();l++)
                bigl.pb(mp(-setval[list[l]], list[l]));
                
                sort(bigl.begin(), bigl.end());
                
                long total = 0;
                map <char, int> used;

                for(int i=0;i<list.sz();i++)
                used[list[i]] = -1;
                vector <int> iused(list.sz(), -1);
                
                for(int i=0;i<bigl.size();i++)
                {
                        //cout<<bigl[i].second<<endl;
                      if(bigl[i].second == word[0])
                           {
                             iused[1] = i;
                             //cout<<"set first "<<1<<" with "<<bigl[i].second<<endl;
                             total += setval[bigl[i].second]*1;
                             continue;  
                           }
                      for(int j=0;j<iused.sz();j++)
                      {
                           if(iused[j] == -1)
                           {
                                       //cout<<"set "<<j<<" with "<<bigl[i].second<<endl;
                                       iused[j] = i;
                                       total += setval[bigl[i].second]*j;
                                       break;
                           }
                           else
                           {
                               continue;    
                           }
                      }
                }
                //cout<<word<<endl;
                cout<<"Case #"<<cnt<<": "<<total<<endl;
                //for(int i=0;i<iused.size();i++)
                        
     cnt++;     
    }
    
    //system("pause");
}


/*
 if(word[0] != bigl[i].second)         //first letter is in word..then dont assign 0
                            {

                                if(used[bigl[i].second] == -1)
                                {
                                total += -bigl[i].first*j;
                                cout<<-bigl[i].first<<":"<<j<<endl;
                                used[bigl[i].second] = j;
                                }
                                else
                                total += -bigl[i].first*used[bigl[i].second];
                                
                            }
                            else
                            {
                                continue;
                            }*/
