#include <iostream>
#include <sstream>
#include <vector>
#include <string>
using namespace std;
typedef pair<int,int> pi;
vector<pi> A,B;
int mustNeeded[1000];
int T;
int toInt(string str)
{
   istringstream iss(str);
   int ret;iss>>ret;
   return ret;
}

int getMins(string str)
{
   return toInt(str.substr(0,2))*60+toInt(str.substr(3));
}

pi makep(int a, int b)
{
   return make_pair(a,b);
}

int solve(vector<pi> &a, vector<pi> &b)
{
    vector<int> arrival;
    for(int i=0;i<a.size();i++) arrival.push_back(a[i].second);
    vector<int> departure;
    for(int i=0;i<b.size();i++) departure.push_back(b[i].first);
    sort(arrival.begin(),arrival.end());
    sort(departure.begin(),departure.end());
    int j=0;
    int ret=b.size();
    for(int i=0;i<arrival.size();i++) {
      for(;j<departure.size();){
         if(arrival[i]+T<=departure[j]) {
            j++;
            ret--;
            break;
         }
         else {
            j++;
         }
      }
    }
    return ret;
}
int main()
{
      freopen("B-small-attempt4.in","r",stdin);
//freopen("test.in","r",stdin);
   freopen("test.out","w",stdout);
   
   int tc;cin>>tc;
   for(int caseCount=1;caseCount<=tc;caseCount++) {
      int na,nb,retA=0,retB=0;
      cin>>T;
      cin>>na>>nb;
      A.clear();B.clear();
      for(int i=0;i<na;i++) {
         string depstr,arrstr;
         cin>>depstr>>arrstr;
         A.push_back(makep(getMins(depstr),getMins(arrstr)));
      }
      
      for(int i=0;i<nb;i++) {
         string depstr,arrstr;
         cin>>depstr>>arrstr;
         B.push_back(makep(getMins(depstr),getMins(arrstr)));
      }
      
      retB=solve(A,B);retA=solve(B,A);
      cout<<"Case #"<<caseCount<<": "<<retA<<" "<<retB<<endl;
   }      
         
      
      
   return 0;
}
