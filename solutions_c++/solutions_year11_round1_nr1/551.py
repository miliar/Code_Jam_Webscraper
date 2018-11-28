#include<iostream>
#include<vector>
#include<cmath>
#include<cstdlib>
#include<set>
#include<algorithm>
#include<queue>
#include<stack>
#include<list>
#include<sstream>
#include<limits.h>
#include<math.h>
#include<map>
using namespace std;	

#define LIMIT 0.00000000001
#define pb push_back
#define p_f pop_front
#define REP(i,n) for(int i=0;i<(int)n;i++)
#define REPI(i,a,n) for(int i=(int)a;i<(int)n;i++)
#define REPD(i,a,n) for(int i=(int)a;i>=(int)n;i--)
#define PI 3.1415926535897932384626433832795

/*template<typename T> void swap(T& left, T& right)
{
  T tmp(left);
  left = right;
  right = tmp;
}*/

long long gcd(long long a, long long b){
	if(b==0)
		return a;
	return gcd(b, a%b);
}


int main(){

	int numCases;
	cin>>numCases;
	
	for(int kase=1;kase<=numCases;kase++){
		long long N,pd,pg;
		cin>>N>>pd>>pg;
		long long hcf = gcd(100, pd);
//		cout<<hcf<<endl;
		if(N>= 100/hcf){
			if( (pg==100 && pd!=100) || (pg==0 && pd!=0) )
				cout<<"Case #"<<kase<<": "<<"Broken\n";
			else
				cout<<"Case #"<<kase<<": "<<"Possible\n";
		}
		else
			cout<<"Case #"<<kase<<": "<<"Broken\n";
	}
	return 0;
}
