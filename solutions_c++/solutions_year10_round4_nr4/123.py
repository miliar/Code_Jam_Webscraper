#include <iostream>
#include <vector>
#include <math.h>
using namespace std;
int main(){
	int T,m,n,t;
	int i,j,k;
	double cx,cy;
	double x1,x2,y1,y2,x,y,z;
	double r1,r2,d,f,d1,d2,A;
	double pi = M_PI;
	
	cin>>T;
	t = 1;
	while(T--){
		cin>>n>>m;
		vector<double> ans;
		cin>>x1>>y1>>x2>>y2;
		
		for(i=0;i<m;i++){
			cin>>cx>>cy;
			
			r1 = sqrt(((cx-x1)*(cx-x1)) + ((cy-y1)*(cy-y1)));
			r2 = sqrt(((cx-x2)*(cx-x2)) + ((cy-y2)*(cy-y2)));
		
			double AB = sqrt(((x1-x2)*(x1-x2)) + ((y1-y2)*(y1-y2)));
			if(fabs(AB - (r1+r2)) < 1e-6)
				ans.push_back(0);
			else{
				d = max(r1,r2) - min(r1,r2);
				A =  pi * min(r1*r1,r2*r2);
				
				if(fabs(AB-d) < 1e-6)
					ans.push_back(A);
				else{
					f = ((r2*r2) + (AB*AB) - (r1*r1))/(2*r2*AB);
					d1 = 2*acos(f);
					
					f = ((r1*r1) + (AB*AB) - (r2*r2))/(2*r1*AB);
					d2 = 2*acos(f);
					
					A = ((d1*r2*r2) + (d2*r1*r1)) - ((sin(d1)*r2*r2) + (sin(d2)*r1*r1));
					A = A/2;
					ans.push_back(A);
				}
			}
		}
		
		printf("Case #%d:",t);
		t++;
		
		for(i=0;i<ans.size();i++)
			printf(" %0.7lf",ans[i]);
		cout<<endl;
	}
	return 0;
}