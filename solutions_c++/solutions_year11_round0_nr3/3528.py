/*
This program is develpoed by Ratan Dhorawat.
*/

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
#define N 1002
//int candy[N];
using namespace std;

int main()
{
 
 int TT,T=0;
 cin>>TT;
 while(TT--)
 {
            T++;
 int cn,tmp;
 cin>>cn;
 int x,sum,minv;
 cin>>tmp;
 x=tmp;
 sum=tmp;
 minv=tmp;
 for(int i=1;i<cn;i++)
 {
      cin>>tmp;
      x ^= tmp;
      sum+=tmp;
      minv=min(tmp,minv);
      
 }
 cout<<"Case #"<<T<<": ";
 if(x)
 cout<<"NO\n";
 else
 cout<<sum-minv<<endl;
 }
 //system("pause");
 return 0;
}
