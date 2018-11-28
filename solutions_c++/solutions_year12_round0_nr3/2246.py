using namespace std;
#include <algorithm>
#include <iostream>
#include <iterator>
#include <sstream>
#include <fstream>
#include <cassert>
#include <climits>
#include <cstdlib>
#include <cstring>
#include <string>
#include <cstdio>
#include <vector>
#include <cmath>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
int main()
{
int t,a,b;
cin>>t;int q=1;
while(q<=t)
{
   cin>>a>>b;
   int r=a,len=0;while(r!=0){r=r/10;len++;}
   int c_num,cnt=0;
   while(a<b)
   {
     set<int> w;        
     for(int x=1;x<len;x++)
     {
      int pwer1=(int)pow((double)10,x);         
      int pwer2=(int)pow((double)10,(len-x));   
      if(a%pwer1==0)continue;
      c_num=(a%pwer1)*pwer2+(a/pwer1);
      if(c_num>a && c_num<=b){w.insert(c_num);}
      }
      cnt+=w.size();
     a++;
   }
  cout<<"Case #"<<q<<": "<<cnt<<'\n';
q++;   
}
return 0;
}

