#include <algorithm>
#include <string>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
using namespace std;

#define pi 3.1415926535897932384626433832795028841971
#define mp make_pair
#define x first
#define y second
#define FOR(i,a,b) for (long _n(b), i(a); i < _n; i++)
#define CL(a) memset((a),0,sizeof(a))
#define VI vector <int>

int GCD(int a,int b)
{
  if (a==0) return b;
  else return GCD(b%a,a);
}

int main ()
{
  freopen ("input.txt","r",stdin);
  freopen ("output.txt","w",stdout);

    int t,a,b;
    long long n;
    cin >>t;
    FOR(i,0,t)
    {
      cin >>n>>a>>b;
      if ((n<(100/(GCD(a,100))))||((b==100)&&(a!=100))||((b==0)&&(a!=0)))
	cout << "Case #"<<i+1<<": "<<"Broken"<<endl;
	else 
	cout << "Case #"<<i+1<<": "<<"Possible"<<endl;	  
    }




  return 0;
}