#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <algorithm>
#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <string>
#include <cstring>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>

using namespace std;

int case_number;
#define gout case_number++, printf("Case #%d: ",case_number), cout
#define F(i,n) for((i)=0;(i)<(n);(i)++)

int score;
void repeat()
{
     int P,N;
     int i,x,j,temp,match,val,score;
     vector <int> M;
     vector <int> t;
     vector <vector<int> > d;
     cin>>P;
     score = 0;
     N = int(pow(2.0,double(P)));
     F(i,N)
     {
           cin>>x;
           M.push_back(x);
     }
     j=N/2;
     while(j>0)
     {
               t.clear();
               F(i,j)
               {
                     cin>>x;
                     t.push_back(x);
               }
               d.push_back(t);
               j=j/2;
     }
     
     //F(i,N)
           //cout<<M[i];
     F(i,P+1)
     {
                     F(j,N)
                     {
                             if(M[j] == i)
                             {
                                     temp = P - i;
                                     match = int(pow(2.0, double(i+1)));
                                     val = j/match;
                                     //cout<<"i="<<i<<endl;
                                     while(temp > 0 )
                                     {
                                                val = j/match;
                                                //cout<<"tmep"<<temp<<"j="<<j<<endl;
                                                if(d[P-temp][val])
                                                {
                                                                  score +=  d[P-temp][val];
                                                                  d[P-temp][val]=0;
                                                                  //cout<<"P-temp"<<P-temp<<"val"<<val;
                                                }
                                                else
                                                    break;
                                                match  = match*2;
                                                temp--;
                                     }
                             }
                     }
     }
     gout<<score<<endl;
}

int main(int argc, char *argv[])
{
    int i,T;
    case_number = 0;
    cin>>T;
    F(i,T)
          repeat();
}
