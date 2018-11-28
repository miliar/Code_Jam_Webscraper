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
#include <fstream>
#define pb push_back
using namespace std;

int main(){
int t;
cin>>t;int pp=1;
string s;
getline(cin,s);
while(t--)
 {
 getline(cin,s);
 string chk=s;
   int sz=s.size();
   next_permutation(s.begin(),s.end());
   while(s[0]=='0')s.erase(s.begin());
   int sz2=s.size();
   if(s.size() == sz && s > chk )
    {
	  cout<<"Case #"<<pp<<": "<<s<<endl;
	  }
	  else
	   {
	 while(sz2<=sz)
	  { 
	     s.insert(s.begin()+1,'0');
		 sz2++;
		 
		 }
		  cout<<"Case #"<<pp<<": "<<s<<endl;
	 
	 }
  
   pp++;
   }
   

return 0;
}
