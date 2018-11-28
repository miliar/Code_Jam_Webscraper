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
 int t,c=1;
 cin>>t;
 while(c<=t)
  { 
     int n,s,p,cnt=0,x;    
     cin>>n>>s>>p;
     while(n--)
     {
         vector<int> w;      
         cin>>x;
         if(x==0 && p==0){cnt++;continue;}
         if(x==0 && p>0){continue;}
         w.push_back(x/3);
         x=x-x/3;
         if(!(x%2==0)){w.push_back(x/2+1);w.push_back(x/2);}
         if(x%2==0){if(x/2>=p){w.push_back(x/2);w.push_back(x/2);}
                    if((x/2+1)==p && s>0){w.push_back(x/2+1);w.push_back(x/2-1);s--;}
                    else {w.push_back(x/2);w.push_back(x/2);}
                   }
                         
         int max=*max_element(w.begin(),w.end());          
         if(max>=p)cnt++;
         w.erase(w.begin(),w.end());
     }
 cout<<"Case #"<<c<<": "<<cnt<<'\n';    
 c++;
 }
return 0;
}
