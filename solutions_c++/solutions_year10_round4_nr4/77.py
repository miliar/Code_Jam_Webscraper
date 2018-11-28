#include <cstdio>
#include <cstring>
#include <cassert>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<double, double> point;

inline double sq(double lol){return lol*lol;}

int main(){
	int lz;
	scanf("%d", &lz);
	for(int cnt = 1; cnt <= lz; cnt++){
		int p, n;
		scanf("%d %d", &p, &n);
		assert(p==2);
		point A, B;
		scanf("%lf %lf %lf %lf\n", &A.first, &A.second, &B.first, &B.second);
		
		vector<point> aim(n);
		vector<double> ret(n);
		printf("Case #%d:", cnt); 
		for(int i = 0; i < n; i++){
			point tam;
			scanf("%lf %lf", &tam.first, &tam.second);
			double Arad = sqrt(sq(A.first-tam.first)+sq(A.second-tam.second));
			double Brad = sqrt(sq(B.first-tam.first)+sq(B.second-tam.second));
			
			double c = sqrt(sq(B.first-A.first)+sq(B.second-A.second));
			
			//printf(">> %lf %lf %lf\n", Arad, Brad, c);
			
			double CBA = acos((sq(Brad) + sq(c) - sq(Arad))/(2*Brad*c)); // cos(CBA) = (r1^2 + c^2 - r0^2)/(2*r1*c) 
			double CBD = 2*CBA; // CBD = 2(CBA)
			//printf("CBA: acos(%lf)\n", sq(Brad) + sq(c) - sq(Arad)/(2*Brad*c));
			
			double CAB = acos((sq(Arad) + sq(c) - sq(Brad))/(2*Arad*c));//cos(CAB) = (r0^2 + c^2 - r1^2)/(2*r0*c)

			double CAD = 2*(CAB);
			
			ret[i] = (1.0/2.0)*CBD*sq(Brad) - (1.0/2.0)*sq(Brad)*sin(CBD) + (1.0/2.0)*CAD*sq(Arad) - (1.0/2.0)*sq(Arad)*sin(CAD); 
			//	(1/2)(CBD)r1^2 - (1/2)r1^2*sin(CBD)
       	//+ (1/2)(CAD)r0^2 - (1/2)r0^2*sin(CAD)
       	printf(" %.7lf", ret[i]);
		}
		printf("\n");
		
	}
	return 0;
}
