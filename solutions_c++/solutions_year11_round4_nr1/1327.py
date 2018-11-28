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

#define LIMIT 0.00000001
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

typedef struct node{
	double S;
	double E;
	int W;
} node;

bool compare(node a, node b){
	if(a.W<b.W)
		return true;
	return false;
}

int main(){

	int numCases;
	cin>>numCases;
	
	for(int kase=1;kase<=numCases;kase++){
		int X,S,R,t,N;
		cin>>X>>S>>R>>t>>N;
		node arr[1010];
		
		int way=0;
		REP(i, N){
			cin>>arr[i].S>>arr[i].E>>arr[i].W;
			way+= arr[i].E- arr[i].S;
		}
		double noway = X-way;

		sort( arr, arr+N, compare);
		
		double runTime = t;	
		double time = noway/R;
		double minTime = min( time, runTime);
		noway-=minTime*R;
		runTime-=minTime;
		double ans= minTime + noway/S;
	

		REP(i, N){
			noway = arr[i].E - arr[i].S;
			time = noway/(R+arr[i].W);
			minTime = min( time, runTime);
			noway-=minTime*(R+arr[i].W);
			runTime-=minTime;
			ans+= minTime + noway/(S+arr[i].W);
		}


		cout<<"Case #"<<kase<<": ";
		printf("%.8lf\n", ans);
	}
	return 0;
}
