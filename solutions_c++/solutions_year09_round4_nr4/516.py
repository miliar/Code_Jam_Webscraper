#include <algorithm> 
#include <string> 
#include <vector> 
#include <cmath> 
#include <sstream> 
#include <iostream> 
#include <cstdio> 
#include <set> 
#include <map> 
#include <utility> 
#include <cstdlib> 
#include <locale> 
#include <bitset> 
#include <numeric> 
using namespace std; 

#define all(x) (x).begin(),(x).end() 
#define rall(x) (x).rbegin(),(x).rend() 
#define clear(x,v) memset((x),v,(x).size()) 
#define pb push_back 

#define UNI(x) do{ sort(all(x)) ; (x).erase(unique(all(x)),(x).end()); } while(0) 

typedef stringstream ss; 
typedef vector<int> vi ;  
typedef vector<string> vs ;

bool check(string s, int n)
{
	for(int i = n+1 ; i< s.size() ;i++)
		if(s[i] == '1') 
			return false; 
	return true; 
}

double dis(int x1,int y1, int x0,int y0)
{
	double ret = sqrt(double((x0-x1)*(x0-x1) + (y0-y1)*(y0-y1))) ; 
	return ret ;
}

int main()
{
	int N ; 
	cin>>N ; 

	for(int t = 1 ; t <= N ; t++)
	{				
		double ret = 0 ; 
		int k ; cin>> k ; 

		vector<double> x(k), y(k), r(k) ; 
		for(int i = 0 ;i < k ; i++)
			cin>>x[i]>>y[i]>>r[i]; 

		
		if(k==1)
		{
			ret = r[0] ;
		}
		else if(k == 2)
		{
			double min1 = dis(x[0],y[0],x[1],y[1])+ r[0]+r[1] ; 
			min1 /= 2.0 ; 
			double min2 = max(r[0],r[1]) ; 
			ret =  min(min1,min2) ; 

		}
		else if(k== 3)
		{
			double dis1 = dis(x[0],y[0],x[1],y[1]) ; 
			double dis2 = dis(x[2],y[2],x[1],y[1]) ; 
			double dis3 = dis(x[0],y[0],x[2],y[2]) ;

			double min1 = max(dis1 + r[0]+r[1] , r[2]) ; 
			double min2 = max(dis2 + r[2]+r[1] , r[0]) ; 
			double min3 = max(dis3 + r[0]+r[2] , r[1]) ; 

			ret = min(min(min1,min2), min3) ; 
			ret /= 2.0; 

		}

		printf("Case #%d: %f\r\n", t,ret ) ; 
	}

	return 0 ;
}