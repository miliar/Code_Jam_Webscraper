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
using namespace std;
#define ll long long 
typedef pair<long long,long long> pll;
int main()
{
    ll n,A,B,C,D,m,x0,y0;
    ll i,j,k,l;
    ll x,y;
    ll t;
    cin>>t;
    l=1;
    while(t--)
    {
    cin>>n>>A>>B>>C>>D>>x0>>y0>>m;
    vector<pll> pts;
    ll count=0;
    x=x0,y=y0;
    pts.push_back(pll(x,y));
    for(i=1;i<n;i++)
    {
       x=((A*x+B)%m);
       y=((C*y+D)%m);
       pts.push_back(pll(x,y));
    }
    sort(pts.begin(),pts.end());
    for(i=0;i<pts.size();i++)
    {
       for(j=i+1;j<pts.size();j++)
       {
       	   for(k=j+1;k<pts.size();k++)
       	   {
       	       if((pts[i].first+pts[j].first+pts[k].first)%3==0)
	       	       if((pts[i].second+pts[j].second+pts[k].second)%3==0)       	          
	       	        	++count;
	   }
       }
    }
    cout <<"Case #"<<l++<<": "<< count << endl;
    }    
   
}
