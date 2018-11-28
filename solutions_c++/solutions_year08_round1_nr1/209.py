#define Llong long long
#include <algorithm>
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <queue>
#include <set>
#include <map>
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <cmath>


#define fill_(x,v) memset(x,v,sizeof(x))
#define for_(i,a,b) for (__typeof(b) i=(a); i<(b); i++)
#define min(x,y) (((x)>(y)) ? (y) :(x))
#define max(x,y) (((y)>(x)) ? (y) :(x))
#define mL 200
using namespace std;

ifstream inp("D:\\googleCodeJam\\A\\A-small-attempt0.in");
ofstream onp("D:\\googleCodeJam\\A\\small.out" , ios::out);

template <class T> void outp (vector <T> D, long long n = 0 )
{ if ( n == 0 ) n = D.size();
  cout<<endl;
  for ( long long i = 0; i < n; i++ )	  cout<<D[i]<<" ";
  cout<<endl;
}

int main()
{
long long N;
inp >> N;

 for ( long long nN = 0; nN < N; nN++) {
       long long n,m, i;
		   inp >> n;
		   vector <int> X, Y;
		   X.clear();
		   Y.clear();
		   for ( i = 0; i < n; i ++)
		   {inp >> m; X.push_back(m); }
		   for ( i = 0; i < n; i ++)
		   {inp >> m; Y.push_back(m); }
		   sort (X.begin(), X.end());
		   sort (Y.begin(), Y.end());
		   
		   long long sum = 0;
		   for ( i = 0; i < n; i ++)
			   sum += X[i] * Y[n - 1 - i];
		onp<<"Case #"<< nN+1 <<": "<< sum<<endl;;
	 }
 onp.close();	 
 return 1;
 
}