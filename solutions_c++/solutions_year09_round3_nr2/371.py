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

int main()
{

	int N ; 
	cin>> N ; 

	for(int n = 1 ; n <= N ; n++)
	{
		int tt ; 
		cin>> tt ; 

		double x=0,y=0,z=0,vx=0,vy=0,vz=0 ; 
		for(int i = 0 ; i < tt ; i++)
		{
			double x_,y_,z_,vx_,vy_,vz_ ; 
			cin>>x_>>y_>>z_>>vx_>>vy_>>vz_ ; 

			x+= x_ ; 
			y+= y_ ; 
			z+= z_ ; 
			vx+= vx_ ; 
			vy+= vy_ ; 
			vz+= vz_ ; 
		}

		double a = (vx*vx) + (vy*vy) + (vz*vz) ; 
		double b = 2.0 * (vx*x + vy*y + vz*z) ; 
		double c = x*x + y*y + z*z ; 

		double t =0; 
		double d =0;
		if(a <=  0.0000000001 || vx*x+vy*y +vz*z >= 0)
		{
			t = 0 ; 			
			d =  sqrt(a*t*t + b*t + c) / (double)tt; 
		}
		else
		{
			t = -1.0* (vx*x+vy*y +vz*z) / a ; 
			if(a*t*t + b*t + c <=  0.0000000001)
				d = 0; 
			else
				d =  sqrt(a*t*t + b*t + c) / (double)tt; 
		}

		/*
		cout<<a*t*t + b*t + c<<endl;
		cout<<vx*x+vy*y +vz*z<<endl;
		cout<<x<<y<<z<<vx<<vy<<vx<<endl ;
		cout<<a<<" "<<b<<" "<<c<<" "<<tt<<endl ;
*/
		printf("Case #%d: %.8f %.8f\n", n,d,t) ; 
	}
	return 0 ; 
}