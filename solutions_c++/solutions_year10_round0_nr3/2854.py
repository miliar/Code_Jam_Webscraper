#include <vector>
#include <list>
#include <map>
#include <set>
#include <queue>
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
#include <cstring>
#include <ctime>

using namespace std;
void print ( int kase ,  int yes )
{
 	 cout <<"Case #"<<kase<<": ";
	  cout <<yes;
	  cout <<"\n";
 	 return ;
}
int main ()
{
 	freopen ("c-small.in","r",stdin);
 	freopen("c-small.out","w",stdout);
 	int T ,kase = 0; 
 	for ( scanf("%d",&T) ; T ;T-- )
 	{
	 	int R,K,N; cin >> R >> K >>N;
	 	queue<int> Q;
	 	for ( int i = 0; i < N ;i++ ) 
	 	{
		 	int t ; cin >>t ; Q.push(t);
		}
		int cnt = 0 ;
		for ( int i = 0 ; i < R ;i++ )
		{
		 	queue <int> Q1;
		 	int sum = 0 ;
		 	while ( !Q.empty()) 
		 	{
			 	  int t = Q.front();
			 	  if ( sum + t > K ) break;
			 	  sum += t; Q.pop();
			 	  Q1.push(t);
		  }
		  cnt += sum;
		  while ( !Q1.empty() ) 
		  {
		   		Q.push(Q1.front());Q1.pop();
		  }
      }
      print(++kase , cnt);
   }
   return 0;
}
