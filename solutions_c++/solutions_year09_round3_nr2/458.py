#include <iostream>
#include <vector>
#include <cmath>
using namespace std;
struct firefly{
	double x,y,z;
	double vx,vy,vz;
};

int main(){
	int m;
	cin>>m;
	for(int i = 0;i<m;i++){
		int n;
		cin>>n;
		vector<firefly*> swarm;
		double cx = 0;
		double cy = 0;
		double cz = 0;
		double cvx = 0;
		double cvy = 0;
		double cvz = 0;
		
		for(int j = 0;j<n;j++){
			firefly* ins = new firefly();
			cin>>ins->x;
			cin>>ins->y;
			cin>>ins->z;
			cin>>ins->vx;
			cin>>ins->vy;
			cin>>ins->vz;
			cx += ins->x;
			cy += ins->y;
			cz += ins->z;
			cvx += ins->vx;
			cvy += ins->vy;
			cvz += ins->vz;
			swarm.push_back(ins);
		}
		cx /= swarm.size();
		cy /= swarm.size();
		cz /= swarm.size();
		cvx /= swarm.size();
		cvy /= swarm.size();
		cvz /= swarm.size();
		
		double mint;
		if(cvx*cvx+cvy*cvy+cvz*cvz == 0){
			mint = 0;
		}
		else{
			mint = -(cvx*cx + cvy*cy+cvz*cz)/(cvx*cvx+cvy*cvy+cvz*cvz);
		}
		if(mint < 0)
			mint =0;
		double xx = cx + mint*cvx;
		double yy = cy + mint*cvy;
		double zz = cz + mint*cvz;
		double mindis = sqrt(xx*xx+yy*yy+zz*zz);
		
		cout<<"Case #"<<i+1<<": ";
		printf("%.9f ",mindis);
		printf("%.9f\n",mint);
	}
	return 0;
}

			
			
			
							
			