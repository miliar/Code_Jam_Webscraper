#include <cstdlib>
#include <iostream>
#include <map>
#include <set>
#include <cmath>
#include <queue>
#include <vector>
#include <string>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cassert>
#include <numeric>
#include <algorithm>
#include <iostream>
#include <sstream>
#include <ctime>

using namespace std;

bool cmp( int  a, int  b ) {
   return a > b;
 }   

int main(int argc, char *argv[])
{
    int n;
    cin>>n;
    for(int i=1;i<=n;i++)
    {  int m,s;
       cin>>m;
       vector<int> A1,A2;
       for(int j=1;j<=m;j++)
        {  cin>>s;
           A1.push_back(s);}
       for(int j=1;j<=m;j++)
        {  cin>>s;
           A2.push_back(s);}
       sort(A1.begin(),A1.end());
       sort(A2.begin(),A2.end(),cmp);
      int sum=0;
      for(int j=1;j<=m;j++)
      { sum=sum+A1[j-1]*A2[j-1];}
      cout<<"Case #"<<i<<": "<<sum<<endl; 
        
    }

    return 0;
}
