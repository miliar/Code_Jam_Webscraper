#include <vector>
#include <list>
#include <map>
#include <set>
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
#include <queue>
using namespace std;
bool com(string s1,string s2)
{
 
 return s1>s2;
}
int main()
{
 string s,s2;
 int n,c=0;
 cin>>n;
 while(n--)
 {
 c++;
 cin>>s;
 s2=s;
 next_permutation(s.begin(),s.end());
 
 
   if(com(s,s2))
   cout<<"Case #"<<c<<": "<<s<<endl;
  else
  {
   
    while(s[0]=='0')s.erase(s.begin());
	while(s2.size()>=s.size())
    s.insert(1,"0");
    cout<<"Case #"<<c<<": "<<s<<endl;
   }
 
  
 }
 return 0;
}